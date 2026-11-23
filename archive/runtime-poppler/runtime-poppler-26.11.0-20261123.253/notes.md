## `ghcr.io/pair-ai-platform/go:runtime-poppler-26.11.0-20261123.253`

Go static runtime with poppler-utils 26.11.0. Index digest `sha256:cb38738f66d9ef1bd36cdf6a0da59d6985f3ce061dbb011b96f4dfda2ffef0de`.
Tags: `runtime-poppler-26.11.0-20261123.253`, `runtime-poppler`, `poppler`.

### What changed

| Package | From | To |
| :--- | :--- | :--- |
| `bash` | 5.3-r14 | 5.3-r15 |
| `busybox` | 1.38.0-r3 | 1.38.0-r4 |
| `ca-certificates-bundle` | 20261020-r0 | 20261020-r1 |
| `openssl-provider-legacy-allowed` | 4.1.0-r0 | 4.1.0-r1 |

### SBOM and size

| Architecture | Packages (SBOM) | Compressed | Installed |
| :--- | :--- | :--- | :--- |
| x86_64 | 56 | 27.0 MB | 67.0 MB |
| aarch64 | 56 | 25.1 MB | 70.6 MB |

Main components: `ca-certificates-bundle 20261020-r1`, `glibc-2.44 2.44-r24`, `libstdc++ 16.2.0-r5`, `openssl-4.0-libcrypto 4.0.3-r8`, `poppler 26.11.0-r0`, `poppler-utils 26.11.0-r0`.
The SPDX SBOMs are attached to this release and to each image as signed attestations.

### Scans

| Architecture | Hardening profile, DISA GPOS SRG (applicable rules passed) | Not applicable | Vulnerabilities (C / H / M / L) |
| :--- | :--- | :--- | :--- |
| x86_64 | 85 / 91 (93.4%) | 107 | 0 / 0 / 1 / 1 |
| aarch64 | 85 / 91 (93.4%) | 107 | 0 / 0 / 1 / 1 |

### Vulnerabilities

| ID | Severity | Package | Installed | Comes from | Fixed upstream in | Architectures |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [CVE-2026-115819](https://nvd.nist.gov/vuln/detail/CVE-2026-115819) | Medium | `glibc-2.44` | 2.44-r24 | `glibc-2.44 2.44-r24` | no fix yet | x86_64, aarch64 |
| [CVE-2026-100290](https://nvd.nist.gov/vuln/detail/CVE-2026-100290) | Low | `glibc-2.44` | 2.44-r24 | `glibc-2.44 2.44-r24` | no fix yet | x86_64, aarch64 |

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
cosign verify ghcr.io/pair-ai-platform/go:runtime-poppler-26.11.0-20261123.253 \
  --certificate-identity-regexp '^https://github.com/Pair-AI-Platform/go/.github/workflows/build.yml@' \
  --certificate-oidc-issuer https://token.actions.githubusercontent.com
gh attestation verify oci://ghcr.io/pair-ai-platform/go:runtime-poppler-26.11.0-20261123.253 --repo Pair-AI-Platform/go
```
