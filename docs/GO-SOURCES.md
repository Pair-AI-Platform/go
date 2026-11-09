# Where Go comes from

| Image | Go package | Source | Verification |
| :--- | :--- | :--- | :--- |
| `go:1.27`, `go:1.27-dev` | `go-1.27` | Wolfi (`packages.wolfi.dev`) | Wolfi repository RSA key |
| `go:1.26`, `go:1.26-dev` | `go-1.26` | Wolfi (`packages.wolfi.dev`) | Wolfi repository RSA key |
| `go:1.25`, `go:1.25-dev` | `go-1.25-upstream` | Official binaries from [go.dev](https://go.dev/dl/), packaged here by melange | Google Linux Signing Authority PGP key + SHA-256 |

## Why Go 1.25 comes from go.dev

In accordance with Wolfi / Chainguard lifecycle policy, only active upstream Go releases
are maintained in the public Wolfi OS repository (`packages.wolfi.dev/os`). Older releases
(such as `go-1.25` and earlier) are transitioned to Chainguard's commercial/enterprise repository.
As a result, the public Wolfi package remains pinned at `1.25.12-r1` and receives no subsequent security
fixes or patch updates. Chainguard's commercial packages require a private subscription and are not
accessible in public open-source builds.

The official Go project at Google publishes binaries for all supported and maintenance lines for
both `linux-amd64` and `linux-arm64` on the day of release.

## How the package is built and verified

[`melange/go-1.25-upstream.yaml`](../melange/go-1.25-upstream.yaml), natively on `x86_64` and `aarch64`,
for every build:

1. Downloads `go<version>.linux-<arch>.tar.gz`, `go<version>.linux-<arch>.tar.gz.asc`, and
   `go<version>.linux-<arch>.tar.gz.sha256` from `https://dl.google.com/go/`.
2. Verifies the detached PGP signature with `gpgv` against the official Google Linux Packages
   Signing Authority key ([`go-release-keys.kbx`](../melange/go-1.25-upstream/go-release-keys.kbx),
   primary key `EB4C1BFD4F042F6DDDCCEC917721F63BD38B4796`). The build halts immediately if the
   signature is missing or invalid.
3. Validates the tarball against the cryptographic SHA-256 checksum issued by Google.
4. Packages the Go compiler binary (`/usr/lib/go/bin/go`), the formatting tool (`/usr/lib/go/bin/gofmt`),
   the standard library source and packages, and symlinks them to `/usr/bin/go` and `/usr/bin/gofmt`.
5. Executes automated tests verifying the binary runs, reports the correct version, and responds to commands.

The package is signed with the repository's APK key (`keys/go-packages.rsa.pub`, private half in
the `MELANGE_SIGNING_KEY` secret). The build is reproducible: identical versions yield identical packages.

## How it is kept current

[Renovate](../renovate.json) tracks dependencies and opens pull requests automatically:

| What | Renovate source | Rule |
| :--- | :--- | :--- |
| Go version | `golang-version` datasource (the release list of go.dev) | Newest `1.25.x` patch release; automerged once all images build, test and scan |
| Signing keys | `scripts/update-go-release-keys.sh` | Refreshes the keyring whenever Google adds or rotates release signing subkeys |

Merging the pull request triggers the release workflow, publishing the updated `go:1.25` and `go:1.25-dev`
images with updated SBOMs, provenance, and vulnerability scans.

## If Wolfi moves another line

`go-1.26` and `go-1.27` are in public Wolfi today. When `go-1.28` is released and Wolfi transitions
`go-1.26` to Chainguard's commercial repository, the identical upstream packaging strategy applies:
copy `melange/go-1.25-upstream.yaml` to `melange/go-1.26-upstream.yaml`, update the version and rules,
and adjust `apko/go-1.26*.apko.yaml` to depend on `go-1.26-upstream`.
