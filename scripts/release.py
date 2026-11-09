#!/usr/bin/env python3
"""Release records, notes and status badges for published Go images.

    scripts/release.py record <old-packages.txt> <new-packages.txt> <results-dir>
        Prints the record of one published image as JSON. The package files have one
        "<name> <version>" per line; <results-dir> holds results-<family>-<arch>/ from the test
        job. Reads FAMILY, FLAVOR, IMAGE, INDEX, RELEASE and FLOATING from the environment.

    scripts/release.py notes <record.json>
        Prints the release notes of one image as Markdown.

    scripts/release.py pages <record-dir> <site-dir>
        Writes the status of one image into the GitHub Pages site, from the release record and the
        SBOMs and OpenSCAP reports next to it:
          images/<family>.html          the image page: vulnerabilities, SBOM per architecture, OpenSCAP
          archive/<family>/<release>/   the same evidence for every release, kept after the image is deleted
          sbom/<family>/sbom-<arch>.spdx.json, reports/<family>/stig-<arch>.html
          status/<family>.json and the shields.io endpoint badges
          badges/<family>-{stig,vulns,sbom,size,release}.json
"""
import html
import json
import os
import pathlib
import shutil
import sys

ARCHES = ["x86_64", "aarch64"]
# Shown in the release notes as the main components of each image
KEY_PREFIXES = ("go-", "glibc-", "openssl-", "ca-certificates", "libstdc++", "git", "binutils", "gcc", "make")
SEVERITIES = ["Critical", "High", "Medium", "Low", "Negligible", "Unknown"]


def read_packages(path):
    packages = {}
    for line in pathlib.Path(path).read_text().splitlines():
        if line.strip():
            name, version = line.split(" ", 1)
            packages[name] = version
    return packages


def record(old_path, new_path, results):
    old, new = read_packages(old_path), read_packages(new_path)
    family = os.environ["FAMILY"]
    scans = {}
    go_ver = None
    for arch in ARCHES:
        base = pathlib.Path(results) / f"results-{family}-{arch}"
        image = json.loads((base / "image.json").read_text())
        go_ver = go_ver or image.get("go") or image.get("node")
        scans[arch] = {
            "digest": image["digest"],
            "sbom": {"packages": image["packages"], "spdx_packages": image["sbom_spdx_packages"]},
            "size": image["size"],
            "stig": json.loads((base / "stig" / "summary.json").read_text()),
            "vulnerabilities": json.loads((base / "vuln" / "summary.json").read_text()),
        }
    return {
        "family": family,
        "flavor": os.environ["FLAVOR"],
        "image": os.environ["IMAGE"],
        "release": os.environ["RELEASE"],
        "floating": os.environ["FLOATING"].split(),
        "digest": os.environ["INDEX"],
        "go": go_ver,
        "first_release": not old,
        "key_packages": [
            f"{n} {new[n]}" for n in sorted(new)
            if n.startswith(KEY_PREFIXES) and not n.endswith(("-locale-posix", "-legacy-allowed"))
        ],
        "packages": {
            "added": sorted(f"{n} {v}" for n, v in new.items() if n not in old),
            "removed": sorted(f"{n} {v}" for n, v in old.items() if n not in new),
            "updated": sorted(
                [n, old[n], new[n]] for n in new if n in old and old[n] != new[n]
            ),
        },
        "scans": scans,
    }


def notes(rec):
    image, release = rec["image"], rec["release"]
    out = [f"## `{image}:{release}`", ""]
    out.append(f"Go {rec['go']} ({rec['flavor']}). Index digest `{rec['digest']}`.")
    out.append("Tags: " + ", ".join(f"`{t}`" for t in [release] + rec["floating"]) + ".")
    out += ["", "### What changed", ""]
    pk = rec["packages"]
    if rec["first_release"]:
        out.append("First release of this image.")
    elif not (pk["added"] or pk["removed"] or pk["updated"]):
        out.append("No package changed; the image metadata did.")
    else:
        out += ["| Package | From | To |", "| :--- | :--- | :--- |"]
        out += [f"| `{n}` | {a} | {b} |" for n, a, b in pk["updated"]]
        out += [f"| `{p.split()[0]}` | (new) | {p.split()[1]} |" for p in pk["added"]]
        out += [f"| `{p.split()[0]}` | {p.split()[1]} | (removed) |" for p in pk["removed"]]
    out += ["", "### SBOM and size", "",
            "| Architecture | Packages (SBOM) | Compressed | Installed |",
            "| :--- | :--- | :--- | :--- |"]
    for arch in ARCHES:
        scan = rec["scans"][arch]
        out.append(f"| {arch} | {scan['sbom']['packages']} | {mb(scan['size']['compressed'])} | {mb(scan['size']['installed'])} |")
    out += ["", "Main components: " + ", ".join(f"`{p}`" for p in rec["key_packages"]) + "."]
    out += ["", "### Hardening and security", "",
            "| Architecture | DISA GPOS SRG profile | Vulnerabilities (Grype) |",
            "| :--- | :--- | :--- |"]
    for arch in ARCHES:
        scan = rec["scans"][arch]
        st = scan["stig"]
        vu = scan["vulnerabilities"]
        out.append(f"| {arch} | {st['counts'].get('pass', 0)} of {st['applicable']} rules pass ({st['score']}%) | "
                   f"{vu['total']} total (Critical {vu['counts'].get('Critical', 0)}, High {vu['counts'].get('High', 0)}, "
                   f"Medium {vu['counts'].get('Medium', 0)}, Low {vu['counts'].get('Low', 0)}) |")
    out += ["", "The signed release and the evidence files are attached to this release.", ""]
    return "\n".join(out)


def mb(b):
    return f"{b / 1048576:.1f} MB"


def badge(label, message, color):
    return {"schemaVersion": 1, "label": label, "message": str(message), "color": color}


PAGE_STYLE = """
body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
       max-width: 900px; margin: 40px auto; padding: 0 20px; line-height: 1.5; color: #24292f; }
h1, h2, h3 { line-height: 1.25; margin-top: 24px; margin-bottom: 16px; font-weight: 600; }
h1 { font-size: 2em; border-bottom: 1px solid #d0d7de; padding-bottom: .3em; }
h2 { font-size: 1.4em; border-bottom: 1px solid #d0d7de; padding-bottom: .3em; }
table { border-collapse: collapse; width: 100%; margin-top: 10px; margin-bottom: 20px; }
th, td { padding: 8px 12px; border: 1px solid #d0d7de; text-align: left; font-size: 14px; }
th { background-color: #f6f8fa; font-weight: 600; }
tr:nth-child(even) { background-color: #fcfcfc; }
code { background-color: #afb8c133; padding: .2em .4em; border-radius: 4px; font-size: 85%; }
.badge { display: inline-block; padding: 2px 6px; border-radius: 4px; font-size: 12px; font-weight: bold; color: white; }
.sev-Critical { background-color: #cf222e; }
.sev-High { background-color: #d4a72c; color: black; }
.sev-Medium { background-color: #fb8f44; }
.sev-Low { background-color: #57606a; }
.sev-Negligible, .sev-Unknown { background-color: #8c959f; }
.muted { color: #57606a; font-size: 13px; }
"""


def page(rec, record_dir, site):
    e = html.escape
    family = rec["family"]
    rows = [f"<h1><code>{e(rec['image'])}:{e(family)}</code></h1>"]
    rows.append(f"<p>Go {e(rec['go'])} ({e(rec['flavor'])}). Tags: "
                + ", ".join(f"<code>{e(t)}</code>" for t in [rec['release']] + rec['floating']) + ".</p>")
    rows.append(f"<p class=\"muted\">Index digest: <code>{e(rec['digest'])}</code></p>")

    rows.append('<h2 id="vulnerabilities">Vulnerabilities (Grype)</h2>')
    rows.append('<table><tr><th>Architecture</th><th>Total</th><th>Critical</th><th>High</th>'
                '<th>Medium</th><th>Low</th></tr>')
    for arch in ARCHES:
        v = rec["scans"][arch]["vulnerabilities"]["counts"]
        rows.append(f"<tr><td>{arch}</td><td>{rec['scans'][arch]['vulnerabilities']['total']}</td>"
                    f"<td><span class=\"badge sev-Critical\">{v.get('Critical', 0)}</span></td>"
                    f"<td><span class=\"badge sev-High\">{v.get('High', 0)}</span></td>"
                    f"<td><span class=\"badge sev-Medium\">{v.get('Medium', 0)}</span></td>"
                    f"<td><span class=\"badge sev-Low\">{v.get('Low', 0)}</span></td></tr>")
    rows.append("</table>")

    rows.append('<h2 id="sbom">Software Bill of Materials (SBOM)</h2>')
    rows.append('<table><tr><th>Architecture</th><th>Packages</th><th>SPDX file</th><th>Size (compressed)</th>'
                '<th>Size (installed)</th></tr>')
    for arch in ARCHES:
        sc = rec["scans"][arch]
        rows.append(f"<tr><td>{arch}</td><td>{sc['sbom']['packages']}</td>"
                    f'<td><a href="../sbom/{e(family)}/sbom-{arch}.spdx.json">SPDX JSON</a></td>'
                    f"<td>{mb(sc['size']['compressed'])}</td><td>{mb(sc['size']['installed'])}</td></tr>")
    rows.append("</table>")

    rows.append('<h2 id="stig">Security Hardening (DISA GPOS SRG)</h2>')
    rows.append('<p class="muted">Derived from the DISA General Purpose Operating System SRG; not an official '
                'DISA STIG for containers.</p><table><tr><th>Architecture</th><th>Passed / applicable</th>'
                '<th>Not applicable</th><th>Report</th></tr>')
    for arch in ARCHES:
        st = rec["scans"][arch]["stig"]
        rows.append(f"<tr><td>{arch}</td><td>{st['counts'].get('pass', 0)} / {st['applicable']} ({st['score']}%)</td>"
                    f"<td>{st['counts'].get('notapplicable', 0)}</td>"
                    f'<td><a href="../reports/{e(family)}/stig-{arch}.html">OpenSCAP report</a></td></tr>')
    rows.append("</table>")
    title = f"go:{family}"
    return (f"<!doctype html><html lang=\"en\"><head><meta charset=\"utf-8\">"
            f"<meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">"
            f"<title>{e(title)}</title><style>{PAGE_STYLE}</style></head><body>"
            + "\n".join(rows) + "</body></html>\n")


def pages(record_dir, site, archive_release=True):
    record_dir, site = pathlib.Path(record_dir), pathlib.Path(site)
    rec = json.loads((record_dir / "record.json").read_text())
    family = rec["family"]
    for d in ("status", "badges", "images", f"sbom/{family}", f"reports/{family}"):
        (site / d).mkdir(parents=True, exist_ok=True)
    for arch in ARCHES:
        shutil.copy(record_dir / f"sbom-{arch}.spdx.json", site / "sbom" / family / f"sbom-{arch}.spdx.json")
        shutil.copy(record_dir / f"stig-{arch}.html", site / "reports" / family / f"stig-{arch}.html")
    (site / "images" / f"{family}.html").write_text(page(rec, record_dir, site))
    if not archive_release:
        return write_status(rec, site)
    archive = site / "archive" / family / rec["release"]
    archive.mkdir(parents=True, exist_ok=True)
    for f in ["record.json", "notes.md"] + [f"sbom-{a}.spdx.json" for a in ARCHES] + [f"stig-{a}.html" for a in ARCHES]:
        if (record_dir / f).exists():
            shutil.copy(record_dir / f, archive / f)
    (archive / "index.html").write_text(page(rec, record_dir, site).replace(f"../sbom/{family}/", "").replace(
        f"../reports/{family}/", ""))
    write_status(rec, site)


def write_status(rec, site):
    family = rec["family"]
    stig = rec["scans"]["x86_64"]["stig"]
    vulns = {
        s: max(rec["scans"][a]["vulnerabilities"]["counts"].get(s, 0) for a in ARCHES)
        for s in SEVERITIES
    }
    status = {
        "family": family,
        "release": rec["release"],
        "go": rec["go"],
        "digest": rec["digest"],
        "stig": {a: {k: rec["scans"][a]["stig"][k] for k in ("counts", "applicable", "score")} for a in ARCHES},
        "vulnerabilities": {a: rec["scans"][a]["vulnerabilities"]["counts"] for a in ARCHES},
        "sbom": {a: rec["scans"][a]["sbom"] for a in ARCHES},
        "size": {a: rec["scans"][a]["size"] for a in ARCHES},
        "key_packages": rec["key_packages"],
    }
    (site / "status" / f"{family}.json").write_text(json.dumps(status, indent=2) + "\n")
    score = stig["score"]
    color = "brightgreen" if score >= 90 else "yellow" if score >= 75 else "red"
    (site / "badges" / f"{family}-stig.json").write_text(json.dumps(badge(
        "GPOS SRG", f"{stig['counts'].get('pass', 0)}/{stig['applicable']} ({score}%)", color)))
    serious = vulns["Critical"] + vulns["High"]
    color = "brightgreen" if serious == 0 and vulns["Medium"] == 0 else "yellow" if serious == 0 else "red"
    (site / "badges" / f"{family}-vulns.json").write_text(json.dumps(badge(
        "CVEs", f"C{vulns['Critical']} H{vulns['High']} M{vulns['Medium']} L{vulns['Low']}", color)))
    sbom = " / ".join(str(rec["scans"][a]["sbom"]["packages"]) for a in ARCHES)
    (site / "badges" / f"{family}-sbom.json").write_text(json.dumps(badge(
        "SBOM", f"{sbom} packages (amd64 / arm64)", "blue")))
    x86 = rec["scans"]["x86_64"]
    (site / "badges" / f"{family}-size.json").write_text(json.dumps(badge(
        "size", mb(x86["size"]["compressed"]), "blue")))
    (site / "badges" / f"{family}-release.json").write_text(json.dumps(badge(
        "release", rec["release"], "blue")))


if __name__ == "__main__":
    command = sys.argv[1]
    if command == "record":
        print(json.dumps(record(*sys.argv[2:5]), indent=2))
    elif command == "notes":
        print(notes(json.loads(pathlib.Path(sys.argv[2]).read_text())), end="")
    elif command == "pages":
        pages(sys.argv[2], sys.argv[3], archive_release="--no-archive" not in sys.argv[4:])
    else:
        sys.exit(f"unknown command {command}")
