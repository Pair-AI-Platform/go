# Go Images on Wolfi

[![SLSA Build L3](https://img.shields.io/badge/SLSA-Build%20L3-orange?style=for-the-badge)](#slsa-build-level-3)
[![Signed with Sigstore](https://img.shields.io/badge/signed-Sigstore%20keyless-purple?style=for-the-badge)](#verify)

Minimal, non-root Go container images for `linux/amd64` and `linux/arm64`, built with
[apko](https://github.com/chainguard-dev/apko) from [Wolfi](https://github.com/wolfi-dev) packages and
verified upstream binaries. Every image is rebuilt every two hours and published again only when its content changed. Every version is:

- **tested** on both architectures with functional, compiler and CGO integration checks;
- **scanned** with OpenSCAP against a hardening profile derived from the DISA General Purpose
  Operating System SRG, and for known vulnerabilities with Grype;
- **signed** keyless with Sigstore;
- **attested** with its SBOM, its scan results and SLSA Build Level 3 provenance.

These images ship Go and its toolchain. Cryptography profiles (for example FIPS 140-3) are
chosen per application and per contract, and are provided separately: see [Cryptography](#cryptography).

## Alignment at a glance

| Area | Aligned with | Evidence in every release |
| :--- | :--- | :--- |
| **Hardening** | OpenSCAP profile derived from the DISA General Purpose Operating System SRG (not an official DISA STIG for containers) | Rules passed out of the applicable ones (about 94% on `go:1.27`), the full report, a signed attestation; see [Security scans](#security-scans) |
| **🇸🇦 Saudi Arabia** | NCA ECC-2:2024 1-6-2-2, 1-6-3-2, 1-6-3-5, 2-1, 2-2-3-3, 2-10-3 · NCA CCC-2:2024 2-3-P-1-3, 2-3-P-1-7, 2-9-T-1-1, 4-1-P-1-2 · NCA CSCC-1:2019 2-3-1-1, 2-3-1-7 · SAMA CSF 3.3.8, 3.3.17 | Minimal non-root baseline, STIG and vulnerability results, SBOM, signatures, provenance |
| **🇰🇼 Kuwait** | CBK CORF 5.3.1.2–5.3.1.5 (hardening against recognized benchmarks), 5.8.1.3 (SBOM), 5.13 (vulnerability and patch management) · NCSC NBCC PR-1, ID-2 | Same, plus rebuilds every two hours |
| **🇦🇪 UAE** | UAE IA Regulation v1.1 T3.2.1, T5.5.4, T7.5.1, T7.7.1, T7.8.1 (superseded by the IA Standard v2.x, 2025; mapping to v2 follows) | Same; the scans use the SCAP formats (XCCDF, OVAL, CVE, CVSS) T7.7 names |
| **🇶🇦 Qatar** | NCSA National Vulnerability Management Guidelines v1.0 (Jan 2026) §6.5 (3–7 days for actively exploited, 14–30 days for CVSS ≥ 7.0), §6.8(b) | Hourly check for fixes, vulnerabilities per release |
| **🇧🇭 Bahrain · 🇴🇲 Oman** | CBB OM-5.5.18, OM-5.5.25, OM-5.5.27, Appendix C · ITA Basic Security Controls 5.5, 5.6, 5.8 | Same |
| **🔐 Cryptography** | FIPS 140-3, CMVP #4985 (security policy §11.1) · 🇸🇦 NCA NCS-1:2020 MODERATE · NCA ECC-2:2024 2-8-3 · NCA DCC-1:2022 2-5-1-2 · SAMA CSF 3.3.9 · 🇰🇼 CBK CORF 5.3.1.3(i), 5.7.1.3, 8.1.4.5 · 🇶🇦 Qatar National Cryptographic Standard v1.0 Tables 1, 2, 4, 5, 7, 10 · 🇦🇪 UAE IA Regulation v1.1 T7.4.1 · 🇧🇭 CBB OM Appendix C (Data Security 1–2) | Compatible with system cryptographic policies or [khatm](https://github.com/Pair-AI-Platform/khatm) when required |

The clause-by-clause table, with links to every document, is in
[Gulf cybersecurity rules at the container level](#gulf-cybersecurity-rules-at-the-container-level).

## Images

`ghcr.io/pair-ai-platform/go:<tag>`. The numbers come from the newest release of each image
and update with every release; click a badge for the details on the image's page:

- **Hardening profile:** rules passed out of the applicable ones, with the full OpenSCAP report.
- **Vulnerabilities:** counts by severity (Critical / High / Medium / Low); the page lists every
  CVE with the affected package and the version that fixes it.
- **SBOM:** packages on amd64 / arm64; the page lists every package with its version and license,
  and links each architecture's SPDX file.
- **Size:** compressed. Each image's [GitHub releases](../../releases) have the same numbers for both
architectures, plus what changed.

| Image | Go line | Hardening profile (x86_64) | Vulnerabilities | SBOM | Size | Newest release |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `go:1.27` · `latest` | Current stable | [![GPOS SRG profile](https://img.shields.io/endpoint?url=https://pair-ai-platform.github.io/go/badges/1.27-stig.json)](https://pair-ai-platform.github.io/go/images/1.27.html#stig) | [![CVEs](https://img.shields.io/endpoint?url=https://pair-ai-platform.github.io/go/badges/1.27-vulns.json)](https://pair-ai-platform.github.io/go/images/1.27.html#vulnerabilities) | [![SBOM](https://img.shields.io/endpoint?url=https://pair-ai-platform.github.io/go/badges/1.27-sbom.json)](https://pair-ai-platform.github.io/go/images/1.27.html#sbom) | ![size](https://img.shields.io/endpoint?url=https://pair-ai-platform.github.io/go/badges/1.27-size.json) | [![release](https://img.shields.io/endpoint?url=https://pair-ai-platform.github.io/go/badges/1.27-release.json)](https://pair-ai-platform.github.io/go/images/1.27.html) |
| `go:1.27-dev` · `latest-dev` | Current stable (CGO) | [![GPOS SRG profile](https://img.shields.io/endpoint?url=https://pair-ai-platform.github.io/go/badges/1.27-dev-stig.json)](https://pair-ai-platform.github.io/go/images/1.27-dev.html#stig) | [![CVEs](https://img.shields.io/endpoint?url=https://pair-ai-platform.github.io/go/badges/1.27-dev-vulns.json)](https://pair-ai-platform.github.io/go/images/1.27-dev.html#vulnerabilities) | [![SBOM](https://img.shields.io/endpoint?url=https://pair-ai-platform.github.io/go/badges/1.27-dev-sbom.json)](https://pair-ai-platform.github.io/go/images/1.27-dev.html#sbom) | ![size](https://img.shields.io/endpoint?url=https://pair-ai-platform.github.io/go/badges/1.27-dev-size.json) | [![release](https://img.shields.io/endpoint?url=https://pair-ai-platform.github.io/go/badges/1.27-dev-release.json)](https://pair-ai-platform.github.io/go/images/1.27-dev.html) |
| `go:1.26` | Previous stable | [![GPOS SRG profile](https://img.shields.io/endpoint?url=https://pair-ai-platform.github.io/go/badges/1.26-stig.json)](https://pair-ai-platform.github.io/go/images/1.26.html#stig) | [![CVEs](https://img.shields.io/endpoint?url=https://pair-ai-platform.github.io/go/badges/1.26-vulns.json)](https://pair-ai-platform.github.io/go/images/1.26.html#vulnerabilities) | [![SBOM](https://img.shields.io/endpoint?url=https://pair-ai-platform.github.io/go/badges/1.26-sbom.json)](https://pair-ai-platform.github.io/go/images/1.26.html#sbom) | ![size](https://img.shields.io/endpoint?url=https://pair-ai-platform.github.io/go/badges/1.26-size.json) | [![release](https://img.shields.io/endpoint?url=https://pair-ai-platform.github.io/go/badges/1.26-release.json)](https://pair-ai-platform.github.io/go/images/1.26.html) |
| `go:1.26-dev` | Previous stable (CGO) | [![GPOS SRG profile](https://img.shields.io/endpoint?url=https://pair-ai-platform.github.io/go/badges/1.26-dev-stig.json)](https://pair-ai-platform.github.io/go/images/1.26-dev.html#stig) | [![CVEs](https://img.shields.io/endpoint?url=https://pair-ai-platform.github.io/go/badges/1.26-dev-vulns.json)](https://pair-ai-platform.github.io/go/images/1.26-dev.html#vulnerabilities) | [![SBOM](https://img.shields.io/endpoint?url=https://pair-ai-platform.github.io/go/badges/1.26-dev-sbom.json)](https://pair-ai-platform.github.io/go/images/1.26-dev.html#sbom) | ![size](https://img.shields.io/endpoint?url=https://pair-ai-platform.github.io/go/badges/1.26-dev-size.json) | [![release](https://img.shields.io/endpoint?url=https://pair-ai-platform.github.io/go/badges/1.26-dev-release.json)](https://pair-ai-platform.github.io/go/images/1.26-dev.html) |
| `go:1.25` | Extended maintenance | [![GPOS SRG profile](https://img.shields.io/endpoint?url=https://pair-ai-platform.github.io/go/badges/1.25-stig.json)](https://pair-ai-platform.github.io/go/images/1.25.html#stig) | [![CVEs](https://img.shields.io/endpoint?url=https://pair-ai-platform.github.io/go/badges/1.25-vulns.json)](https://pair-ai-platform.github.io/go/images/1.25.html#vulnerabilities) | [![SBOM](https://img.shields.io/endpoint?url=https://pair-ai-platform.github.io/go/badges/1.25-sbom.json)](https://pair-ai-platform.github.io/go/images/1.25.html#sbom) | ![size](https://img.shields.io/endpoint?url=https://pair-ai-platform.github.io/go/badges/1.25-size.json) | [![release](https://img.shields.io/endpoint?url=https://pair-ai-platform.github.io/go/badges/1.25-release.json)](https://pair-ai-platform.github.io/go/images/1.25.html) |
| `go:1.25-dev` | Extended maintenance (CGO) | [![GPOS SRG profile](https://img.shields.io/endpoint?url=https://pair-ai-platform.github.io/go/badges/1.25-dev-stig.json)](https://pair-ai-platform.github.io/go/images/1.25-dev.html#stig) | [![CVEs](https://img.shields.io/endpoint?url=https://pair-ai-platform.github.io/go/badges/1.25-dev-vulns.json)](https://pair-ai-platform.github.io/go/images/1.25-dev.html#vulnerabilities) | [![SBOM](https://img.shields.io/endpoint?url=https://pair-ai-platform.github.io/go/badges/1.25-dev-sbom.json)](https://pair-ai-platform.github.io/go/images/1.25-dev.html#sbom) | ![size](https://img.shields.io/endpoint?url=https://pair-ai-platform.github.io/go/badges/1.25-dev-size.json) | [![release](https://img.shields.io/endpoint?url=https://pair-ai-platform.github.io/go/badges/1.25-dev-release.json)](https://pair-ai-platform.github.io/go/images/1.25-dev.html) |

Go 1.26 and 1.27 come from the public Wolfi repository (`packages.wolfi.dev`). Go 1.25 comes from the
official `go.dev` binaries, signature-verified and packaged locally via Melange, because Wolfi moved
non-latest Go versions to Chainguard's commercial repository; see [Where Go comes from](docs/GO-SOURCES.md).

| Flavor | Contents |
| :--- | :--- |
| runtime (`go:1.27`) | Go compiler and toolchain, git, bash, busybox, CA certificates, and time zones. Runs as `nonroot` (1000:1000) in `/app`. Minimal attack surface without C compiler tooling. |
| development (`go:1.27-dev`) | The standard runtime plus `build-base` (GCC, G++, make, binutils), `pkgconf`, Python 3, and OpenSSH client for CGO compilation and native C library dependencies. |

```dockerfile
# Multi-stage build example
FROM ghcr.io/pair-ai-platform/go:1.27-dev AS build
WORKDIR /app
COPY go.mod go.sum ./
RUN go mod download
COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -ldflags="-w -s" -o /app/server ./cmd/server

# Ship on minimal runtime or distroless
FROM ghcr.io/pair-ai-platform/go:1.27
COPY --from=build /app/server /app/server
ENTRYPOINT ["/app/server"]
```

The default entrypoint is `/usr/bin/go`. Running `docker run ghcr.io/pair-ai-platform/go:1.27 version`
executes `go version`. For shell interaction, override entrypoint with `--entrypoint bash`.

---

## Tags and versions

| Tag | Example | Moves? |
| :--- | :--- | :--- |
| Release | `1.27.3-20261109.1`, `1.27.3-dev-20261109.1` | Never. One per published version, with its own [GitHub release](../../releases) |
| Patch | `1.27.3`, `1.27.3-dev` | To the newest release of that Go patch release |
| Minor and major | `1.27`, `1.27-dev` | To the newest release of that line |
| `latest`, `latest-dev` | | To the newest release of the Current stable line (1.27) |

Every run takes each image through these steps; a version exists for users only after the last one:

| Step | What happens | If it fails |
| :--- | :--- | :--- |
| 1. Build and test | apko builds the image natively on x86_64 and aarch64; functional, compiler, CGO, hardening-profile and vulnerability scans run on each | Nothing is published |
| 2. Compare | Both architectures are built together; each must be byte for byte the image tested in step 1. If the result equals the image under the floating tag (`1.27`), nothing changed and the run stops here for that image | Nothing is published |
| 3. Publish by digest | The image is pushed to GHCR without any tag | Untagged, invisible to users; the cleanup deletes it |
| 4. Sign, attest, verify | Sigstore signatures; SBOM, hardening-profile, vulnerability and SLSA provenance attestations; all verified | Still untagged |
| 5. Tag | The release tag (`1.27.3-20261109.1`) and the floating tags move to the new digest | A re-run of the failed job tags it |
| 6. Release | A GitHub release with the changes, the scan results, the SBOMs and the OpenSCAP report, created only if the tag exists on that digest; the badges are updated | A re-run of the failed job creates it |
| 7. Keep five | The five newest versions of each image stay, in GHCR and as GitHub releases | Never fails a release; runs again next time |

- **Only changed images are published.** The builds are reproducible: the same packages give the
  same digest. An hourly check starts a build as soon as Wolfi ships a new version of something
  inside an image, and the build publishes only the images whose digest changed.
- **Release tags never move and never point to an image without its evidence.** Floating tags
  always point to a kept, signed version.
- **Retention: five versions per image.** GHCR and the GitHub releases keep the five newest versions
  of each image (`1.25`, `1.25-dev`, `1.26`, `1.27`, …).
- **The evidence outlives the image.** For every version ever published, release records, SBOMs and
  OpenSCAP reports are preserved in GitHub Pages archive and Rekor.

---

## Security scans

### Hardening profile (OpenSCAP, DISA GPOS SRG)

This is not an official DISA STIG for containers: DISA publishes none. Each image is scanned on both
architectures with OpenSCAP against the content that Wolfi
publishes in the `chainguard-security-guide` package (Apache-2.0): the `xccdf_basic_profile_.check`
profile of `ssg-chainguard-gpos-ds.xml`, which is based on the DISA General Purpose Operating System
SRG. The scanner is built from the Wolfi packages `openscap` and `chainguard-security-guide`.

A typical run on `go:1.27` passes over 93% of applicable rules. The rules that do not pass,
and why:

| Rule | Why it does not pass | Where it is handled |
| :--- | :--- | :--- |
| SV-203649, SV-203739, SV-203750, SV-203751, SV-203776 | They require FIPS-validated cryptography. These images use Wolfi's standard baseline | A cryptography profile, when the contract requires one |
| SV-263659 (approved trust anchors) | The rule reads `SSL_CERT_FILE` from the running processes, and an image scan has no running processes | The image sets `SSL_CERT_FILE`, and the image tests check that the CA bundle matches its checksum stamp |

### Vulnerabilities (Grype)

Each image is scanned with [Grype](https://github.com/anchore/grype) on both architectures, and
the counts per severity are in the badges, the GitHub releases and a signed attestation.

### Image tests

On both architectures, before anything is published:

- **Both flavors:**
  - Go compiler toolchain runs as 1000:1000 in writable `/app` and `/go`.
  - `SSL_CERT_FILE` is set, and the CA bundle loads and matches its checksum stamp.
  - Can compile, format and run a pure Go program.
  - `bash`, `sh`, and `git` are verified operational.
- **Runtime images:** no GCC/Clang compiler installed to maintain a minimal surface.
- **Development images:** GCC, G++, make, pkgconf, and CGO compilation (`import "C"`) pass tests.

---

## Verify

| Evidence | Attached to | Verify with |
| :--- | :--- | :--- |
| Sigstore signature (keyless, logged in Rekor) | the index and each platform image | `cosign verify` |
| SPDX SBOM | each platform image | `cosign verify-attestation --type spdxjson` |
| Hardening-profile results (OpenSCAP) | each platform image | `cosign verify-attestation --type https://github.com/Pair-AI-Platform/go/attestations/stig/v1` |
| Vulnerability scan | each platform image | `cosign verify-attestation --type https://github.com/Pair-AI-Platform/go/attestations/vulnerabilities/v1` |
| SLSA v1 build provenance | the index | `gh attestation verify` |

```sh
IMAGE=ghcr.io/pair-ai-platform/go:1.27
WORKFLOW=Pair-AI-Platform/go/.github/workflows/build.yml

cosign verify "$IMAGE" \
  --certificate-identity-regexp "^https://github.com/$WORKFLOW@" \
  --certificate-oidc-issuer https://token.actions.githubusercontent.com

gh attestation verify "oci://$IMAGE" --repo Pair-AI-Platform/go --signer-workflow "$WORKFLOW"

oras discover --format tree "$IMAGE"
```

---

## SLSA Build Level 3

| Requirement | How it is met |
| :--- | :--- |
| Provenance exists and is complete | `actions/attest-build-provenance` records the source commit, workflow, inputs and runner for every published image |
| Provenance is authentic | Signed through Sigstore with the build workflow's OIDC identity and logged in Rekor; checked again before the image is tagged |
| Hosted, ephemeral build platform | GitHub-hosted runners: `ubuntu-24.04` (x86_64) and `ubuntu-24.04-arm` (aarch64), with no emulation |
| Isolated build, provenance not forgeable by it | Building, signing and attesting run inside the reusable workflow `.github/workflows/build.yml`, whose identity signs the provenance; callers can only pass `publish: true/false` |

---

## Gulf cybersecurity rules at the container level

### Saudi Arabia 🇸🇦

| Document | Clause | Requirement | What the images provide | Stays with the operator |
| :--- | :--- | :--- | :--- | :--- |
| [NCA ECC-2:2024](https://cdn.nca.gov.sa/api/files/public/upload/86e09090-44e4-481f-bc28-355673607654_ECC--2024-EN.pdf) | 1-6-2-2, 1-6-3-5 | "Reviewing secure configuration and hardening and updates packages before launching" | OpenSCAP results and package changes in every release | The review before go-live |
| | 1-6-3-2 | "Using trusted and licensed sources for software development tools and libraries" | Wolfi packages, signatures, SLSA provenance | Verifying signatures on admission |
| | 2-1 | Accurate and updated inventory of assets | SPDX SBOM per architecture | Loading SBOMs into the inventory |
| | 2-2-3-3 | Least privilege | Non-root (1000:1000), minimal surface in runtime images | Pod security context, RBAC |
| | 2-3-3-3, 2-10-3 | Patch management; periodic vulnerability assessment, classification by severity, tested patches | Rebuilds every two hours, Grype results per release | Classification, remediation targets, testing, redeploying |
| [NCA CCC-2:2024](https://cdn.nca.gov.sa/api/files/public/upload/6d5408a3-d8e6-4e96-963b-2c7198e5b7c2_CCC-2-2024-EN-.pdf) | 2-3-P-1-3 | "technical system configurations adhering to the minimum functionality principle" | Minimal packages, separated runtime and dev variants | The provider's configuration standard |
| | 2-3-P-1-7 | "Detection and prevention of unauthorized changes to software programs" | Signatures and digests | Admission policy, read-only root filesystem |
| | 2-9-P-1-1, 2-9-T-1-1 | Vulnerability assessments (monthly or quarterly) | Results per release | Scanning running workloads on that schedule |
| | 4-1-P-1-2 | Security documentation for supplied equipment and services | SBOM, provenance, scan reports | Keeping them |
| [NCA CSCC-1:2019](https://cdn.nca.gov.sa/api/files/public/upload/f15af01c-dc59-4281-95e2-03a770655937_Critical-Systems-Cybersecurity-Controls.pdf) | 2-3-1-1 | Whitelisting of software allowed to execute | Minimal file set | Admission allowlist of digests |
| | 2-3-1-6, 2-3-1-7 | Review hardening every six months; remove default passwords | OpenSCAP report every release; no accounts with passwords | The six-monthly review |
| | 2-9-1-3 | "Immediately remediating for critical vulnerabilities" | Automated rebuilds every two hours | Emergency redeploys |
| [SAMA Cyber Security Framework](https://rulebook.sama.gov.sa/sites/default/files/en_net_file_store/SAMA_EN_3837_VER1.pdf) | 3.3.8 (6)(a),(d),(f),(g) | Configuration parameters, approved software, application whitelisting, vulnerability and patch management | Minimal, signed images | The infrastructure standard |
| | 3.3.17 (3)(b),(d),(f) | Scan frequency, mitigation timelines, patch deployment | Results per release | The timelines (SAMA sets none) |

### Kuwait 🇰🇼

| Document | Clause | Requirement | What the images provide | Stays with the operator |
| :--- | :--- | :--- | :--- | :--- |
| [CBK CORF v1.0](https://www.cbk.gov.kw/en/images/corf-170113_v10_tcm10-170113.pdf) | 5.3.1.2 | Configuration standards "based on global best practices (such as NIST, Center for Internet Security (CIS) benchmarks)" | OpenSCAP results against DISA GPOS SRG-derived profile | Choosing and justifying the benchmark |
| | 5.3.1.3 (a,b,c,e,f) | Only supported software, minimum components, up-to-date updates, no unnecessary services, no unneeded accounts | Minimal, non-root, rebuilt every two hours | Approving versions, network policy |
| | 5.3.1.4, 5.3.1.5 | Quarterly checks against configuration standards; testing before go-live | OpenSCAP results per release | Quarterly checks of running systems |
| | 5.8.1.3 | "all software … accompanied by an up-to-date Software Bill of Materials (SBOM)" | SPDX SBOM per architecture, signed | SBOMs for the application layers added on top |
| | 5.13.1.2, 5.13.2.2–5.13.2.4 | Assessments for missing updates and baselines; risk-based patching; emergency patches immediately | Automated rebuilds, results per release | Vulnerability management process |

### UAE 🇦🇪

| Document | Clause | Requirement | What the images provide | Stays with the operator |
| :--- | :--- | :--- | :--- | :--- |
| UAE IA Regulation v1.1 | T3.2.1 | "define minimum security configurations" | Standard hardened images with OpenSCAP results | Drift monitoring |
| | T5.2.2, T5.5.4 | Restrict privileges and utility programs | Non-root; separate runtime and dev tooling | Runtime privileges |
| | T7.5.1 | "operational systems should only hold approved executable code, and not development code or compilers" | Distinct runtime vs development image tags | Deploying only runtime images |
| | T7.7.1 | Identify vulnerabilities before production, with tools based on CVE, CCE, OVAL, CPE, CVSS, XCCDF | Grype (CVE, CVSS) and OpenSCAP (XCCDF, OVAL) on every build | Remediation plan and timeline |
| | T7.8.1 | Check every delivered product's compliance with security requirements | Signatures, provenance and attestations | Verifying on receipt |

### Bahrain 🇧🇭 and Oman 🇴🇲

| Document | Clause | Requirement | What the images provide | Stays with the operator |
| :--- | :--- | :--- | :--- | :--- |
| [CBB Rulebook Vol. 1, OM](https://cbben.thomsonreuters.com/sites/default/files/net_file_store/Vol_1_OM_April_2023.pdf) | OM-5.5.18 (d),(h) | Security testing at development and after deployment; list of whitelisted applications and components | Build-time scans; SBOM as component list | Post-deployment testing |
| | OM-5.5.25, OM-5.5.27 | Monthly or weekly assessments; patches in risk-based timeframes | Results per release; rebuilds every two hours | Cadence and timeframes |
| | Appendix C | Integrity checking of software; baseline configuration with least functionality; quarterly scans | Signatures; minimal baseline; scans | Change control |
| [ITA Basic Security Controls v1.0](https://www.moheri.gov.om/userupload/Policy/Basic%20Security%20Controls%20Guidelines.pdf) | 5.5, CM.2–CM.8, 5.6, 5.8 | Baseline configurations, least functionality, component inventory, scheduled scanning, patch management | Hardened baseline, SBOM, scans, rebuilds | Schedules and change management |

### Qatar 🇶🇦

| Document | Clause | Requirement | What the images provide | Stays with the operator |
| :--- | :--- | :--- | :--- | :--- |
| NCSA – National Vulnerability Management Guidelines v1.0 | §6.5 | Remediation times: 3-7 Days for actively exploited; 14-30 Days for CVSS ≥ 7.0 | Hourly check for Wolfi fixes; rapid rebuild and publish cycle | Redeploying within those windows |
| | §6.8(b) | Active scanning of all critical assets | Scan per release, per architecture | Scanning running workloads |

---

## How updates reach the images

| What | How |
| :--- | :--- |
| Packages inside images (`go-1.27`, `go-1.26`, glibc, ...) | Not pinned. Every hour, `wolfi-watch.yml` resolves which Wolfi versions each image would get; as soon as anything changes, it starts the release. The build every two hours stays as a safety net |
| apko, OpenSCAP and Grype images, oras, cosign, GitHub Actions | Pinned by digest or version. [Renovate](renovate.json) opens a pull request, automerged once tests pass |
| Go 1.25 (official go.dev binaries) | Renovate tracks go.dev releases; pull requests automerge after images build and test ([details](docs/GO-SOURCES.md)) |
| A new Go line | Add `apko/go-<version>.apko.yaml` and `-dev.apko.yaml` |

## Build locally

Needs Docker, curl and cosign. Tools come from their GitHub releases, verified.

```sh
scripts/install-tools.sh ./bin apko
./bin/apko build scanner/stig-scanner.apko.yaml stig-scanner:local scanner.tar --arch x86_64
./bin/apko build apko/go-1.27.apko.yaml test:1.27 image.tar --arch x86_64
```
