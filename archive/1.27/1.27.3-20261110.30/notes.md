## `ghcr.io/pair-ai-platform/go:1.27.3-20261110.30`

Go 1.27.3 (runtime). Index digest `sha256:dcd495464f2a0d9a8d2bd1817d815440ada974168224a7b71377304f3ada1ff9`.
Tags: `1.27.3-20261110.30`, `1.27`, `1.27.3`, `latest`.

### What changed

No package changed; the image metadata did.

### SBOM and size

| Architecture | Packages (SBOM) | Compressed | Installed |
| :--- | :--- | :--- | :--- |
| x86_64 | 43 | 87.3 MB | 255.2 MB |
| aarch64 | 43 | 81.8 MB | 250.2 MB |

Main components: `ca-certificates-bundle 20261020-r0`, `git 2.56.0-r3`, `glibc-2.44 2.44-r15`, `go-1.27-upstream 1.27.3-r0`, `openssl-4.0-libcrypto 4.0.3-r8`, `openssl-4.0-libssl 4.0.3-r8`.
The SPDX SBOMs are attached to this release and to each image as signed attestations.

### Scans

| Architecture | Hardening profile, DISA GPOS SRG (applicable rules passed) | Not applicable | Vulnerabilities (C / H / M / L) |
| :--- | :--- | :--- | :--- |
| x86_64 | 85 / 91 (93.4%) | 107 | 0 / 2 / 0 / 0 |
| aarch64 | 85 / 91 (93.4%) | 107 | 0 / 2 / 0 / 0 |

### Vulnerabilities

| ID | Severity | Package | Installed | Comes from | Fixed upstream in | Architectures |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [CVE-2026-119586](https://nvd.nist.gov/vuln/detail/CVE-2026-119586) | High | `sqlite-libs` | 3.54.1-r0 | `sqlite-libs 3.54.1-r0` | no fix yet | x86_64, aarch64 |
| [CVE-2026-84243](https://nvd.nist.gov/vuln/detail/CVE-2026-84243) | High | `glibc-2.44` | 2.44-r15 | `glibc-2.44 2.44-r15` | no fix yet | x86_64, aarch64 |

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
cosign verify ghcr.io/pair-ai-platform/go:1.27.3-20261110.30 \
  --certificate-identity-regexp '^https://github.com/Pair-AI-Platform/go/.github/workflows/build.yml@' \
  --certificate-oidc-issuer https://token.actions.githubusercontent.com
gh attestation verify oci://ghcr.io/pair-ai-platform/go:1.27.3-20261110.30 --repo Pair-AI-Platform/go
```
