#!/usr/bin/env bash
# Refreshes melange/go-1.25-upstream/go-release-keys.kbx with Google's Linux Packages Signing Authority
# key (linux-packages-keymaster@google.com, EB4C1BFD4F042F6DDDCCEC917721F63BD38B4796).
set -euo pipefail

recipe="melange/go-1.25-upstream.yaml"
keyring="melange/go-1.25-upstream/go-release-keys.kbx"

[ -f "$recipe" ] || { echo "cannot find $recipe" >&2; exit 1; }

tmpd="$(mktemp -d)"
trap 'rm -rf "$tmpd"' EXIT

curl -fsSL --retry 3 https://dl.google.com/linux/linux_signing_key.pub | gpg --homedir "$tmpd" --import -q
cp "$tmpd/pubring.kbx" "$keyring"
echo "Refreshed Go release keys at $keyring"
