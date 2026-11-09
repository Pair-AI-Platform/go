#!/usr/bin/env python3
"""Lists the images to build, one entry per apko/go-<version>[-dev].apko.yaml.

    scripts/plan.py <image-repository>        # e.g. ghcr.io/pair-ai-platform/go

Prints a JSON list for a GitHub Actions matrix. Each entry has the config path, the family (the
floating tag, e.g. "1.27" or "1.27-dev"), the flavor, the Go version, and whether the image
needs packages built in this repository by melange (melange/*.yaml).
"""
import json
import pathlib
import re
import sys

# The runtime and dev images of this line also get `latest` and `latest-dev`
LATEST_VERSION = "1.27"

image = sys.argv[1]

# Packages built here by melange; images that list one are built with the local repository
local_packages = set()
for recipe in pathlib.Path("melange").glob("*.yaml"):
    m = re.search(r"^package:\n  name: (\S+)", recipe.read_text(), re.M)
    if m:
        local_packages.add(m.group(1))

entries = []
for config in sorted(pathlib.Path("apko").glob("go-*.apko.yaml")):
    m = re.fullmatch(r"go-(\d+\.\d+)(-dev)?\.apko\.yaml", config.name)
    if not m:
        sys.exit(f"unexpected config name: {config.name}")
    ver, dev = m.group(1), bool(m.group(2))
    family = f"{ver}-dev" if dev else ver
    entries.append({
        "config": str(config),
        "image": image,
        "family": family,
        "flavor": "dev" if dev else "runtime",
        "major": ver,
        "latest": ver == LATEST_VERSION,
        "local": any(re.search(rf"^\s+- {re.escape(p)}(=|$)", config.read_text(), re.M) for p in local_packages),
    })
print(json.dumps(entries))

