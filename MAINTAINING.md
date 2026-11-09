# Maintaining

## Repository setup

| Setting | Why |
| :--- | :--- |
| GitHub App `renovate(bot)-updater` installed on this repository, with Contents, Pull requests, Issues and Workflows read/write, Checks, Commit statuses and Dependabot alerts read | Renovate runs as this App, and `release.yml` uses it to create and delete release tags. With `GITHUB_TOKEN`, Renovate's pull requests would start no checks (so nothing automerges), and tags on commits whose workflow files differ from main would be refused |
| Secret `MELANGE_SIGNING_KEY`: the private half of `keys/go-packages.rsa.pub` | Signs the packages built here (Go 1.25). Its public key goes into the images, so it must not change; releases fail without it |
| Variable `RENOVATE_APP_CLIENT_ID` and secret `RENOVATE_APP_PRIVATE_KEY` (the App's `.pem`) | Turned into a short-lived installation token on every run |
| Package `go` → *Manage Actions access*: this repository with **Admin** role | Lets `GITHUB_TOKEN` push to the package and delete old versions |
| GitHub Pages from the `gh-pages` branch | Serves the status files behind the README badges and the STIG reports |
| Ruleset on `main` requiring the `PR` checks (`build / test (…)`) | Nothing merges, not even Renovate's automerge, unless every image builds, passes its tests and is scanned |

## Changing the images

- Image definitions are in `apko/`. A new Go line needs a runtime and a `-dev` file; the
  `latest` tags follow `LATEST_VERSION` in `scripts/plan.py`.
- Packages are not pinned on purpose: the release workflow takes the current Wolfi packages every two hours and
  publishes an image only when its digest changed.
- The images contain Go only. Cryptography profiles (FIPS 140-3, national TLS policies) are
  applied per application and contract from https://github.com/Pair-AI-Platform/khatm.

