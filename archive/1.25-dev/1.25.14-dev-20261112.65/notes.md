## `ghcr.io/pair-ai-platform/go:1.25.14-dev-20261112.65`

Go 1.25.14 (dev). Index digest `sha256:afa7c6209b40e2100d2945e67c90ca9714e8a83f9eaa9d4021533935e55db43a`.
Tags: `1.25.14-dev-20261112.65`, `1.25-dev`, `1.25.14-dev`.

### What changed

No package changed; the image metadata did.

### SBOM and size

| Architecture | Packages (SBOM) | Compressed | Installed |
| :--- | :--- | :--- | :--- |
| x86_64 | 76 | 268.7 MB | 731.3 MB |
| aarch64 | 76 | 251.7 MB | 781.8 MB |

Main components: `binutils 2.47-r4`, `ca-certificates-bundle 20261020-r0`, `gcc 16.2.0-r3`, `git 2.56.1-r0`, `glibc-2.44 2.44-r16`, `glibc-2.44-dev 2.44-r16`, `go-1.25-upstream 1.25.14-r0`, `libstdc++ 16.2.0-r3`, `libstdc++-dev 16.2.0-r3`, `make 4.4.1-r15`, `openssl-4.0-libcrypto 4.0.3-r8`, `openssl-4.0-libssl 4.0.3-r8`.
The SPDX SBOMs are attached to this release and to each image as signed attestations.

### Scans

| Architecture | Hardening profile, DISA GPOS SRG (applicable rules passed) | Not applicable | Vulnerabilities (C / H / M / L) |
| :--- | :--- | :--- | :--- |
| x86_64 | 85 / 91 (93.4%) | 107 | 1 / 8 / 5 / 1 |
| aarch64 | 85 / 91 (93.4%) | 107 | 1 / 8 / 5 / 1 |

### Vulnerabilities

| ID | Severity | Package | Installed | Comes from | Fixed upstream in | Architectures |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [GO-2026-6612](https://go.dev/cl/847187) | Critical | `stdlib` | go1.25.14 | `go-1.25-upstream 1.25.14-r0` | 1.26.9 | x86_64, aarch64 |
| [GO-2026-6603](https://go.dev/cl/847185) | High | `stdlib` | go1.25.14 | `go-1.25-upstream 1.25.14-r0` | 1.26.9 | x86_64, aarch64 |
| [GO-2026-6605](https://go.dev/cl/847306) | High | `stdlib` | go1.25.14 | `go-1.25-upstream 1.25.14-r0` | 1.26.9, 1.27.2 | x86_64, aarch64 |
| [GO-2026-6607](https://go.dev/cl/847312) | High | `stdlib` | go1.25.14 | `go-1.25-upstream 1.25.14-r0` | 1.26.9, 1.27.2 | x86_64, aarch64 |
| [GO-2026-6608](https://go.dev/cl/847307) | High | `stdlib` | go1.25.14 | `go-1.25-upstream 1.25.14-r0` | 1.26.9, 1.27.2 | x86_64, aarch64 |
| [GO-2026-6610](https://go.dev/cl/835145) | High | `stdlib` | go1.25.14 | `go-1.25-upstream 1.25.14-r0` | 1.26.9 | x86_64, aarch64 |
| [GO-2026-6611](https://go.dev/cl/847186) | High | `stdlib` | go1.25.14 | `go-1.25-upstream 1.25.14-r0` | 1.26.9 | x86_64, aarch64 |
| [GO-2026-6613](https://go.dev/cl/847311) | High | `stdlib` | go1.25.14 | `go-1.25-upstream 1.25.14-r0` | 1.26.9, 1.27.2 | x86_64, aarch64 |
| [GO-2026-6617](https://go.dev/cl/847188) | High | `stdlib` | go1.25.14 | `go-1.25-upstream 1.25.14-r0` | 1.26.9 | x86_64, aarch64 |
| [CVE-2025-15367](https://nvd.nist.gov/vuln/detail/CVE-2025-15367) | Medium | `python-3.13` | 3.13.18_git20261030-r0 | `python-3.13 3.13.18_git20261030-r0` | no fix yet | x86_64, aarch64 |
| [CVE-2026-116566](https://nvd.nist.gov/vuln/detail/CVE-2026-116566) | Medium | `python-3.13` | 3.13.18_git20261030-r0 | `python-3.13 3.13.18_git20261030-r0` | no fix yet | x86_64, aarch64 |
| [GO-2026-6599](https://go.dev/cl/839866) | Medium | `stdlib` | go1.25.14 | `go-1.25-upstream 1.25.14-r0` | 1.26.9, 1.27.2 | x86_64, aarch64 |
| [GO-2026-6600](https://go.dev/cl/840925) | Medium | `stdlib` | go1.25.14 | `go-1.25-upstream 1.25.14-r0` | 1.26.9, 1.27.2 | x86_64, aarch64 |
| [GO-2026-6809](https://go.dev/cl/851047) | Medium | `stdlib` | go1.25.14 | `go-1.25-upstream 1.25.14-r0` | 1.26.10, 1.27.3 | x86_64, aarch64 |
| [CVE-2026-103995](https://nvd.nist.gov/vuln/detail/CVE-2026-103995) | Low | `python-3.13` | 3.13.18_git20261030-r0 | `python-3.13 3.13.18_git20261030-r0` | no fix yet | x86_64, aarch64 |
| [GO-2026-6859](https://go.dev/cl/862185) | Unknown | `stdlib` | go1.25.14 | `go-1.25-upstream 1.25.14-r0` | 1.26.11, 1.27.4 | x86_64, aarch64 |

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
cosign verify ghcr.io/pair-ai-platform/go:1.25.14-dev-20261112.65 \
  --certificate-identity-regexp '^https://github.com/Pair-AI-Platform/go/.github/workflows/build.yml@' \
  --certificate-oidc-issuer https://token.actions.githubusercontent.com
gh attestation verify oci://ghcr.io/pair-ai-platform/go:1.25.14-dev-20261112.65 --repo Pair-AI-Platform/go
```
