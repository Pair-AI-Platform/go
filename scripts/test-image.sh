#!/usr/bin/env bash
# Functional and hardening checks for one single-platform Go image.
#
#   scripts/test-image.sh <image-ref> <runtime|dev>
set -euo pipefail

image="$1"
flavor="$2"
failed=0

pass() { printf '  ok    %s\n' "$1"; }
fail() { printf '  FAIL  %s\n' "$1"; failed=1; }
check() { local name="$1"; shift; if "$@" >/dev/null 2>&1; then pass "$name"; else fail "$name"; fi; }

gorun() { docker run --rm -i "$image" "$@"; }
config() { docker image inspect "$image" --format "$1"; }

echo "== $image ($flavor)"

check "go runs" docker run --rm "$image" version
check "runs as 1000:1000" docker run --rm --entrypoint sh "$image" -c '[ "$(id -u)" = "1000" ] && [ "$(id -g)" = "1000" ]'
check "working directory /app is writable" docker run --rm --entrypoint sh "$image" -c 'touch /app/.writable_check && rm /app/.writable_check'
check "GOPATH directory /go is writable" docker run --rm --entrypoint sh "$image" -c 'mkdir -p /go/pkg && touch /go/pkg/.writable_check && rm /go/pkg/.writable_check'
check "image user is 1000" test "$(config '{{.Config.User}}')" = "1000"
check "SSL_CERT_FILE is set" grep -qx 'SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt' \
  <<<"$(config '{{range .Config.Env}}{{println .}}{{end}}')"

# The CA bundle matches the checksum the ca-certificates package recorded (STIG SV-263659)
check "CA bundle matches its checksum stamp" docker run --rm --entrypoint sh "$image" -c '
  want="$(awk "{print \$1}" /etc/ssl/certs/.ca-certificates.crt.sha256)"
  got="$(sha256sum /etc/ssl/certs/ca-certificates.crt | awk "{print \$1}")"
  [ "$want" = "$got" ]'

# Shells availability
check "sh is available" docker run --rm --entrypoint sh "$image" -c "exit 0"
check "bash is available" docker run --rm --entrypoint bash "$image" --version
check "git is available" docker run --rm --entrypoint git "$image" --version

# Basic Go compilation & run
check "go can compile and run a pure program" docker run --rm --entrypoint sh "$image" -c '
  cd /app
  cat << "EOF" > main.go
package main
import "fmt"
func main() { fmt.Println("pair-ai-go-ok") }
EOF
  output="$(go run main.go)"
  [ "$output" = "pair-ai-go-ok" ]'

if [ "$flavor" = runtime ]; then
  # Runtime image must be minimal: no C compiler installed
  check "no C compiler in runtime" docker run --rm --entrypoint sh "$image" -c '! command -v gcc && ! command -v clang'
else
  # Development image: CGO and build tools
  for tool in gcc make pkg-config python3 bash; do
    check "$tool is available" docker run --rm --entrypoint sh "$image" -c "command -v $tool"
  done

  check "CGO compiles and runs with gcc" docker run --rm --entrypoint sh "$image" -c '
    cd /app
    cat << "EOF" > cgomain.go
package main
/*
#include <stdio.h>
int get_num() { return 42; }
*/
import "C"
import "fmt"
func main() {
    fmt.Printf("cgo-%d\n", int(C.get_num()))
}
EOF
    output="$(go run cgomain.go)"
    [ "$output" = "cgo-42" ]'
fi

if [ "$failed" -ne 0 ]; then
  echo "image checks failed for $image" >&2
  exit 1
fi
echo "all image checks passed"

