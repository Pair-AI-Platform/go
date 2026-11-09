## `ghcr.io/pair-ai-platform/go:1.25.12-20261109.5`

Go 1.25.12 (runtime). Index digest `sha256:95e4f923c888082b8dc7ec7fc71fd4b1429635d2ca3d79f675ad222eea58257d`.
Tags: `1.25.12-20261109.5`, `1.25`, `1.25.12`.

### What changed

No package changed; the image metadata did.

### SBOM and size

| Architecture | Packages (SBOM) | Compressed | Installed |
| :--- | :--- | :--- | :--- |
| x86_64 | 43 | 77.3 MB | 221.9 MB |
| aarch64 | 43 | 72.8 MB | 218.7 MB |

Main components: `ca-certificates-bundle 20261020-r0`, `git 2.56.0-r3`, `glibc-2.44 2.44-r14`, `go-1.25-upstream 1.25.12-r0`, `openssl-4.0-libcrypto 4.0.3-r8`, `openssl-4.0-libssl 4.0.3-r8`.
The SPDX SBOMs are attached to this release and to each image as signed attestations.

### Scans

| Architecture | Hardening profile, DISA GPOS SRG (applicable rules passed) | Not applicable | Vulnerabilities (C / H / M / L) |
| :--- | :--- | :--- | :--- |
| x86_64 | 85 / 91 (93.4%) | 107 | 1 / 14 / 6 / 0 |
| aarch64 | 85 / 91 (93.4%) | 107 | 1 / 14 / 6 / 0 |

### Vulnerabilities

| ID | Severity | Package | Installed | Comes from | Fixed upstream in | Architectures |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [GO-2026-6612](https://go.dev/cl/847187) | Critical | `stdlib` | go1.25.12 | `go-1.25-upstream 1.25.12-r0` | 1.26.9 | x86_64, aarch64 |
| [CVE-2026-119586](https://nvd.nist.gov/vuln/detail/CVE-2026-119586) | High | `sqlite-libs` | 3.54.1-r0 | `sqlite-libs 3.54.1-r0` | no fix yet | x86_64, aarch64 |
| [CVE-2026-84243](https://nvd.nist.gov/vuln/detail/CVE-2026-84243) | High | `glibc-2.44` | 2.44-r14 | `glibc-2.44 2.44-r14` | no fix yet | x86_64, aarch64 |
| [GO-2026-5026](https://go.dev/cl/767220) | High | `stdlib` | go1.25.12 | `go-1.25-upstream 1.25.12-r0` | 1.25.13, 1.26.6, 1.27.0-rc.3 | x86_64, aarch64 |
| [GO-2026-5972](https://go.dev/issue/80405) | High | `stdlib` | go1.25.12 | `go-1.25-upstream 1.25.12-r0` | 1.25.13, 1.26.6, 1.27.0-rc.3 | x86_64, aarch64 |
| [GO-2026-6088](https://go.dev/issue/80481) | High | `stdlib` | go1.25.12 | `go-1.25-upstream 1.25.12-r0` | 1.25.13, 1.26.6, 1.27.0-rc.3 | x86_64, aarch64 |
| [GO-2026-6090](https://go.dev/issue/80528) | High | `stdlib` | go1.25.12 | `go-1.25-upstream 1.25.12-r0` | 1.25.13, 1.26.6, 1.27.0-rc.3 | x86_64, aarch64 |
| [GO-2026-6603](https://go.dev/cl/847185) | High | `stdlib` | go1.25.12 | `go-1.25-upstream 1.25.12-r0` | 1.26.9 | x86_64, aarch64 |
| [GO-2026-6605](https://go.dev/cl/847306) | High | `stdlib` | go1.25.12 | `go-1.25-upstream 1.25.12-r0` | 1.26.9, 1.27.2 | x86_64, aarch64 |
| [GO-2026-6607](https://go.dev/cl/847312) | High | `stdlib` | go1.25.12 | `go-1.25-upstream 1.25.12-r0` | 1.26.9, 1.27.2 | x86_64, aarch64 |
| [GO-2026-6608](https://go.dev/cl/847307) | High | `stdlib` | go1.25.12 | `go-1.25-upstream 1.25.12-r0` | 1.26.9, 1.27.2 | x86_64, aarch64 |
| [GO-2026-6610](https://go.dev/cl/835145) | High | `stdlib` | go1.25.12 | `go-1.25-upstream 1.25.12-r0` | 1.26.9 | x86_64, aarch64 |
| [GO-2026-6611](https://go.dev/cl/847186) | High | `stdlib` | go1.25.12 | `go-1.25-upstream 1.25.12-r0` | 1.26.9 | x86_64, aarch64 |
| [GO-2026-6613](https://go.dev/cl/847311) | High | `stdlib` | go1.25.12 | `go-1.25-upstream 1.25.12-r0` | 1.26.9, 1.27.2 | x86_64, aarch64 |
| [GO-2026-6617](https://go.dev/cl/847188) | High | `stdlib` | go1.25.12 | `go-1.25-upstream 1.25.12-r0` | 1.26.9 | x86_64, aarch64 |
| [GO-2026-6091](https://go.dev/issue/80435) | Medium | `stdlib` | go1.25.12 | `go-1.25-upstream 1.25.12-r0` | 1.25.13, 1.26.6, 1.27.0-rc.3 | x86_64, aarch64 |
| [GO-2026-6218](https://go.dev/cl/803681) | Medium | `stdlib` | go1.25.12 | `go-1.25-upstream 1.25.12-r0` | 1.25.13, 1.26.6, 1.27.0-rc.3 | x86_64, x86_64, aarch64, aarch64 |
| [GO-2026-6599](https://go.dev/cl/839866) | Medium | `stdlib` | go1.25.12 | `go-1.25-upstream 1.25.12-r0` | 1.26.9, 1.27.2 | x86_64, aarch64 |
| [GO-2026-6600](https://go.dev/cl/840925) | Medium | `stdlib` | go1.25.12 | `go-1.25-upstream 1.25.12-r0` | 1.26.9, 1.27.2 | x86_64, aarch64 |
| [GO-2026-6809](https://go.dev/cl/851047) | Medium | `stdlib` | go1.25.12 | `go-1.25-upstream 1.25.12-r0` | 1.26.10, 1.27.3 | x86_64, aarch64 |

*Comes from* is the Wolfi package that brings the affected code into the image; a library bundled inside the toolchain, for example, comes from that package. *Fixed upstream in* is the version of the affected code that fixes it; the image gets the fix when the package it comes from ships that version, and the next build after that publishes it.

Hardening-profile rules not passed (x86_64):

- `SV-203649r971535_rule`: The operating system must use mechanisms meeting the requirements of applicable federal laws, Executive orders, directives, policies, regulations, standards, and guidance for authentication to a cryptographic module.
- `SV-203739r987791_rule`: The operating system must implement NSA-approved cryptography to protect classified information in accordance with applicable federal laws, Executive Orders, directives, policies, regulations, and standards.
- `SV-203750r958912_rule`: The operating system must maintain the confidentiality and integrity of information during preparation for transmission.
- `SV-203751r958914_rule`: The operating system must maintain the confidentiality and integrity of information during reception.
- `SV-203776r959006_rule`: The operating system must implement NIST FIPS-validated cryptography for the following: to provision digital signatures, to generate cryptographic hashes, and to protect unclassified information requiring confidentiality and cryptographic protection in accordance with applicable federal laws, Executive Orders, directives, policies, regulations, and standards.
- `SV-263659r982563_rule`: The operating system must include only approved trust anchors in trust stores or certificate stores managed by the organization.

### Verify

```sh
cosign verify ghcr.io/pair-ai-platform/go:1.25.12-20261109.5 \
  --certificate-identity-regexp '^https://github.com/Pair-AI-Platform/go/.github/workflows/build.yml@' \
  --certificate-oidc-issuer https://token.actions.githubusercontent.com
gh attestation verify oci://ghcr.io/pair-ai-platform/go:1.25.12-20261109.5 --repo Pair-AI-Platform/go
```
