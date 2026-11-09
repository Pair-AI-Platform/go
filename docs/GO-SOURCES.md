# Where Go comes from

| Image | Go package | Source | Verification |
| :--- | :--- | :--- | :--- |
| `go:1.25` (`latest`), `go:1.25-dev` (`latest-dev`) | `go-1.25-upstream` | Official binaries from [go.dev](https://go.dev/dl/), packaged here by melange | Google Linux Signing Authority PGP key + SHA-256 |

## Why Go 1.25 (LTS) comes from go.dev

Pair-AI-Platform focuses on **LTS (Long Term Support)** runtime releases. In our platform roadmap,
Go 1.25 is designated as the target LTS baseline.

In accordance with Chainguard and Wolfi's commercial packaging lifecycle, Go 1.25 was moved out of
the public Wolfi OS repository (`packages.wolfi.dev/os`) into Chainguard's commercial/enterprise
repository (`apk.cgr.dev/chainguard`). Consequently, public Wolfi packages for Go 1.25 stopped
receiving security updates and bug fixes. Chainguard's commercial packages require paid enterprise
subscriptions and private authentication, making them unavailable for public community builds.

Rather than relying on unmaintained or private packages, we build an image equivalent to Chainguard's
Go container image, but source the compiler toolchain directly from the official Go website
([go.dev](https://go.dev/dl/) / [dl.google.com](https://dl.google.com/go/)).

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

## How Renovate keeps it current

[Renovate](../renovate.json) continuously monitors upstream releases and ensures Go 1.25 receives all
patch updates and security releases automatically:

| What | Renovate source | Rule |
| :--- | :--- | :--- |
| Go 1.25 version | `golang-version` datasource (queries `go.dev/dl/?mode=json`) | Newest `1.25.x` patch release; automerged once all images build, test and scan |
| Signing keys | `scripts/update-go-release-keys.sh` | Refreshes the keyring whenever Google adds or rotates release signing subkeys |

Whenever the Go team at Google publishes a new 1.25.x release (including CVE security fixes),
Renovate opens a pull request. Once CI passes (build, tests, STIG OpenSCAP scan, Grype scan),
it is automerged, triggering the release pipeline to publish updated `go:1.25` and `go:1.25-dev` images
with fresh SBOMs, SLSA Level 3 provenance, and signatures.
