## `ghcr.io/pair-ai-platform/go:1.27.4-20261113.80`

Go 1.27.4 (runtime). Index digest `sha256:46318898ca2b68d0607831e585889c40fbf5f8ff37d7b2688a8baebaa5c2bf48`.
Tags: `1.27.4-20261113.80`, `1.27`, `1.27.4`, `latest`.

### What changed

| Package | From | To |
| :--- | :--- | :--- |
| `glibc-2.44` | 2.44-r17 | 2.44-r18 |
| `glibc-2.44-locale-posix` | 2.44-r17 | 2.44-r18 |
| `ld-linux-2.44` | 2.44-r17 | 2.44-r18 |
| `libcrypt1-2.44` | 2.44-r17 | 2.44-r18 |

### SBOM and size

| Architecture | Packages (SBOM) | Compressed | Installed |
| :--- | :--- | :--- | :--- |
| x86_64 | 43 | 87.3 MB | 255.4 MB |
| aarch64 | 43 | 81.8 MB | 250.4 MB |

Main components: `ca-certificates-bundle 20261020-r0`, `git 2.56.1-r0`, `glibc-2.44 2.44-r18`, `go-1.27-upstream 1.27.4-r0`, `openssl-4.0-libcrypto 4.0.3-r8`, `openssl-4.0-libssl 4.0.3-r8`.
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
cosign verify ghcr.io/pair-ai-platform/go:1.27.4-20261113.80 \
  --certificate-identity-regexp '^https://github.com/Pair-AI-Platform/go/.github/workflows/build.yml@' \
  --certificate-oidc-issuer https://token.actions.githubusercontent.com
gh attestation verify oci://ghcr.io/pair-ai-platform/go:1.27.4-20261113.80 --repo Pair-AI-Platform/go
```
