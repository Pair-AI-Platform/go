## `ghcr.io/pair-ai-platform/go:runtime-poppler-26.11.0-20261119.189`

Go static runtime with poppler-utils 26.11.0. Index digest `sha256:fb8d03166e14f0910c5e2c63ae88d67de7dac12921d488e2e940121f18f7fdae`.
Tags: `runtime-poppler-26.11.0-20261119.189`, `runtime-poppler`, `poppler`.

### What changed

| Package | From | To |
| :--- | :--- | :--- |
| `libbrotlicommon1` | 1.2.1-r3 | 1.2.1-r4 |
| `libbrotlidec1` | 1.2.1-r3 | 1.2.1-r4 |
| `libbrotlienc1` | 1.2.1-r3 | 1.2.1-r4 |
| `libx11-6` | 1.8.14-r4 | 1.8.14-r5 |
| `libx11-data` | 1.8.14-r4 | 1.8.14-r5 |
| `libxext6` | 1.3.7-r5 | 1.3.7-r6 |
| `libxrender1` | 0.9.13-r1 | 0.9.13-r2 |

### SBOM and size

| Architecture | Packages (SBOM) | Compressed | Installed |
| :--- | :--- | :--- | :--- |
| x86_64 | 56 | 27.0 MB | 66.8 MB |
| aarch64 | 56 | 25.0 MB | 70.5 MB |

Main components: `ca-certificates-bundle 20261020-r0`, `glibc-2.44 2.44-r23`, `libstdc++ 16.2.0-r5`, `openssl-4.0-libcrypto 4.0.3-r8`, `poppler 26.11.0-r0`, `poppler-utils 26.11.0-r0`.
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
cosign verify ghcr.io/pair-ai-platform/go:runtime-poppler-26.11.0-20261119.189 \
  --certificate-identity-regexp '^https://github.com/Pair-AI-Platform/go/.github/workflows/build.yml@' \
  --certificate-oidc-issuer https://token.actions.githubusercontent.com
gh attestation verify oci://ghcr.io/pair-ai-platform/go:runtime-poppler-26.11.0-20261119.189 --repo Pair-AI-Platform/go
```
