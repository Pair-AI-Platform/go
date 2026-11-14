## `ghcr.io/pair-ai-platform/go:runtime-poppler-26.11.0-20261114.85`

Go static runtime with poppler-utils 26.11.0. Index digest `sha256:3218d4a6cbbb3e64f79c10a97f74e88c16f81fb391686deebfcefbff7ad84eab`.
Tags: `runtime-poppler-26.11.0-20261114.85`, `runtime-poppler`, `poppler`.

### What changed

| Package | From | To |
| :--- | :--- | :--- |
| `glibc-2.44` | 2.44-r18 | 2.44-r19 |
| `glibc-2.44-locale-posix` | 2.44-r18 | 2.44-r19 |
| `ld-linux-2.44` | 2.44-r18 | 2.44-r19 |

### SBOM and size

| Architecture | Packages (SBOM) | Compressed | Installed |
| :--- | :--- | :--- | :--- |
| x86_64 | 50 | 25.0 MB | 62.5 MB |
| aarch64 | 50 | 23.2 MB | 65.4 MB |

Main components: `ca-certificates-bundle 20261020-r0`, `glibc-2.44 2.44-r19`, `libstdc++ 16.2.0-r3`, `openssl-4.0-libcrypto 4.0.3-r8`, `poppler 26.11.0-r0`, `poppler-utils 26.11.0-r0`.
The SPDX SBOMs are attached to this release and to each image as signed attestations.

### Scans

| Architecture | Hardening profile, DISA GPOS SRG (applicable rules passed) | Not applicable | Vulnerabilities (C / H / M / L) |
| :--- | :--- | :--- | :--- |
| x86_64 | 85 / 91 (93.4%) | 107 | 0 / 0 / 0 / 0 |
| aarch64 | 85 / 91 (93.4%) | 107 | 0 / 0 / 0 / 0 |

### Vulnerabilities

None found.

Hardening-profile rules not passed (x86_64):

- `SV-203649r971535_rule`: The operating system must use mechanisms meeting the requirements of applicable federal laws, Executive orders, directives, policies, regulations, standards, and guidance for authentication to a cryptographic module.
- `SV-203739r987791_rule`: The operating system must implement NSA-approved cryptography to protect classified information in accordance with applicable federal laws, Executive Orders, directives, policies, regulations, and standards.
- `SV-203750r958912_rule`: The operating system must maintain the confidentiality and integrity of information during preparation for transmission.
- `SV-203751r958914_rule`: The operating system must maintain the confidentiality and integrity of information during reception.
- `SV-203776r959006_rule`: The operating system must implement NIST FIPS-validated cryptography for the following: to provision digital signatures, to generate cryptographic hashes, and to protect unclassified information requiring confidentiality and cryptographic protection in accordance with applicable federal laws, Executive Orders, directives, policies, regulations, and standards.
- `SV-263659r982563_rule`: The operating system must include only approved trust anchors in trust stores or certificate stores managed by the organization.

### Verify

```sh
cosign verify ghcr.io/pair-ai-platform/go:runtime-poppler-26.11.0-20261114.85 \
  --certificate-identity-regexp '^https://github.com/Pair-AI-Platform/go/.github/workflows/build.yml@' \
  --certificate-oidc-issuer https://token.actions.githubusercontent.com
gh attestation verify oci://ghcr.io/pair-ai-platform/go:runtime-poppler-26.11.0-20261114.85 --repo Pair-AI-Platform/go
```
