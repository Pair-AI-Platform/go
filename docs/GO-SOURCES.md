# Where Go comes from

| Image | Go package | Source | Verification |
| :--- | :--- | :--- | :--- |
| `go:1.27` (`latest`), `go:1.27-dev` (`latest-dev`) | `go-1.27-upstream` | Official binaries from [go.dev](https://go.dev/dl/), packaged here by melange | Google Linux Signing Authority PGP key + SHA-256 |
| `go:1.26`, `go:1.26-dev` | `go-1.26-upstream` | Official binaries from [go.dev](https://go.dev/dl/), packaged here by melange | Google Linux Signing Authority PGP key + SHA-256 |
| `go:1.25`, `go:1.25-dev` | `go-1.25-upstream` | Official binaries from [go.dev](https://go.dev/dl/), packaged here by melange | Google Linux Signing Authority PGP key + SHA-256 |

## Why all Go releases come directly from go.dev

Pair-AI-Platform focuses on trusted, independent and reproducible builds. Because Chainguard and Wolfi periodically restrict older releases, move packages to commercial-only repositories, or gate them behind private authentication, relying on upstream Chainguard repositories introduces fragility and vendor lock-in.

Rather than relying on external downstream distributions or private repositories, we build all Go container images directly from the official Go binaries published by the Go team at Google ([go.dev](https://go.dev/dl/) / [dl.google.com](https://dl.google.com/go/)).

## How the packages are built and verified

Each Melange recipe ([`melange/go-1.27-upstream.yaml`](../melange/go-1.27-upstream.yaml), [`melange/go-1.26-upstream.yaml`](../melange/go-1.26-upstream.yaml), [`melange/go-1.25-upstream.yaml`](../melange/go-1.25-upstream.yaml)) builds natively on `x86_64` and `aarch64`:

1. Downloads `go<version>.linux-<arch>.tar.gz`, `go<version>.linux-<arch>.tar.gz.asc`, and
   `go<version>.linux-<arch>.tar.gz.sha256` from `https://dl.google.com/go/`.
2. Verifies the detached PGP signature with `gpgv` against the official Google Linux Packages
   Signing Authority key ([`go-release-keys.kbx`](../melange/go-1.27-upstream/go-release-keys.kbx),
   primary key `EB4C1BFD4F042F6DDDCCEC917721F63BD38B4796`). The build halts immediately if the
   signature is missing or invalid.
3. Validates the tarball against the cryptographic SHA-256 checksum issued by Google.
4. Packages the Go compiler binary (`/usr/lib/go/bin/go`), the formatting tool (`/usr/lib/go/bin/gofmt`),
   the standard library source and packages, and symlinks them to `/usr/bin/go` and `/usr/bin/gofmt`.
5. Executes automated tests verifying the binary runs, reports the correct version, and responds to commands.

The packages are signed with the repository's APK key (`keys/go-packages.rsa.pub`, private half in
the `MELANGE_SIGNING_KEY` secret). The build is reproducible: identical versions yield identical packages.

## How Renovate keeps them current

[Renovate](../renovate.json) continuously monitors upstream releases and ensures all Go versions receive all
patch updates and security releases automatically:

| What | Renovate source | Rule |
| :--- | :--- | :--- |
| Go 1.27 version | `golang-version` datasource (queries `go.dev/dl/?mode=json`) | Newest `1.27.x` patch release; automerged once all images build, test and scan |
| Go 1.26 version | `golang-version` datasource (queries `go.dev/dl/?mode=json`) | Newest `1.26.x` patch release; automerged once all images build, test and scan |
| Go 1.25 version | `golang-version` datasource (queries `go.dev/dl/?mode=json`) | Newest `1.25.x` patch release; automerged once all images build, test and scan |
| Signing keys | `scripts/update-go-release-keys.sh` | Refreshes the keyring whenever Google adds or rotates release signing subkeys |

Whenever the Go team at Google publishes a new release (including CVE security fixes),
Renovate opens a pull request. Once CI passes (build, tests, STIG OpenSCAP scan, Grype scan),
it is automerged, triggering the release pipeline to publish updated images with fresh SBOMs, SLSA Level 3 provenance, and signatures.
