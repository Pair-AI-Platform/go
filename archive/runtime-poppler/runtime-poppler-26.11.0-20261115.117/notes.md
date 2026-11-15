## `ghcr.io/pair-ai-platform/go:runtime-poppler-26.11.0-20261115.117`

Go static runtime with poppler-utils 26.11.0. Index digest `sha256:9de79ad30af667272a41e0f12274567352373ad7918ae3a05905679f8c1cd690`.
Tags: `runtime-poppler-26.11.0-20261115.117`, `runtime-poppler`, `poppler`.

### What changed

| Package | From | To |
| :--- | :--- | :--- |
| `cairo` | 1.18.6-r1 | 1.18.6-r2 |
| `graphite2` | 1.3.15-r6 | 1.3.15-r7 |

### SBOM and size

| Architecture | Packages (SBOM) | Compressed | Installed |
| :--- | :--- | :--- | :--- |
| x86_64 | 56 | 27.0 MB | 66.8 MB |
| aarch64 | 56 | 25.1 MB | 70.5 MB |

Main components: `ca-certificates-bundle 20261020-r0`, `glibc-2.44 2.44-r19`, `libstdc++ 16.2.0-r4`, `openssl-4.0-libcrypto 4.0.3-r8`, `poppler 26.11.0-r0`, `poppler-utils 26.11.0-r0`.
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
cosign verify ghcr.io/pair-ai-platform/go:runtime-poppler-26.11.0-20261115.117 \
  --certificate-identity-regexp '^https://github.com/Pair-AI-Platform/go/.github/workflows/build.yml@' \
  --certificate-oidc-issuer https://token.actions.githubusercontent.com
gh attestation verify oci://ghcr.io/pair-ai-platform/go:runtime-poppler-26.11.0-20261115.117 --repo Pair-AI-Platform/go
```
