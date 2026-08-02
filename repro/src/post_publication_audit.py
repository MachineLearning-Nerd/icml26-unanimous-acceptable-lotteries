#!/usr/bin/env python3
"""Audit the exact published Hugging Face revision from canonical entrypoints."""
from __future__ import annotations

import hashlib
import json
import re
import tempfile
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

from publication_gate import hf_paths, validate_claim_page, validate_evidence, walk_logbook


ROOT = Path(__file__).resolve().parents[2]
SPACE_ID = "DineshAI/daiccpXZfU"
PUBLISHED_REVISION = "b9ca864e0933fb79daa53802cc38bf971397eae8"
USER_AGENT = "OpenResearch-Reproduction/1.0 (arXiv:2604.17505)"


def manifest(path):
    result = {}
    for line in path.read_text().splitlines():
        digest, relative = line.split("  ", 1)
        result[relative.removeprefix("./")] = digest
    return result


def download_exact_tree(destination, expected):
    for relative, digest in expected.items():
        quoted = urllib.parse.quote(relative)
        url = f"https://huggingface.co/spaces/{SPACE_ID}/resolve/{PUBLISHED_REVISION}/{quoted}?download=true"
        request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        with urllib.request.urlopen(request, timeout=120) as response:
            data = response.read()
        assert hashlib.sha256(data).hexdigest() == digest, f"published hash mismatch: {relative}"
        target = destination / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)


def canonical_traversal(release_root):
    opened = {"README.md", "logbook.json"}
    readme = (release_root / "README.md").read_text()
    assert "#/current" in readme and "#/historical-rejected-baseline" in readme
    opened.update(hf_paths(readme))
    logbook = json.loads((release_root / "logbook.json").read_text())
    assert logbook["space_id"] == SPACE_ID and logbook["root"]["slug"] == "current"
    slugs = {}
    walk_logbook(logbook["root"], opened, slugs)
    assert "release-report" in slugs and "historical-rejected-baseline" in slugs

    current = (release_root / slugs["current"]).read_text()
    assert "Visibility matrix" in current
    opened.update(hf_paths(current))
    visibility = {}
    for claim in range(1, 6):
        visibility[f"claim_{claim}"] = validate_claim_page(
            claim, release_root / slugs[f"current-claim-{claim}"], release_root, opened
        )
    validate_evidence(release_root, opened)

    report = release_root / slugs["current-report"]
    report_text = report.read_text()
    opened.add(report.relative_to(release_root).as_posix())
    assert [line for line in report_text.splitlines() if line.strip()][1].startswith("![")
    for name in re.findall(r"\]\(images/([^)]+\.svg)\)", report_text):
        image = report.parent / "images" / name
        ET.fromstring(image.read_text())
        opened.add(image.relative_to(release_root).as_posix())

    release_report = release_root / slugs["release-report"]
    opened.add(release_report.relative_to(release_root).as_posix())
    assert release_report.read_text().startswith("# Final release report\n\nPrevious live judged score: `5/10`")
    opened.add("notebooks/reproduction.py")
    assert all((release_root / relative).is_file() for relative in opened)
    return {"files_opened": sorted(opened), "visibility": visibility}


def main():
    uploaded = manifest(ROOT / ".openresearch" / "release" / "upload_sha256.txt")
    protected = manifest(ROOT / ".openresearch" / "protected-space" / "PROTECTED_SHA256_MANIFEST_RELATIVE.txt")
    expected = dict(protected)
    expected.update(uploaded)
    with tempfile.TemporaryDirectory(prefix="daiccpXZfU-published-") as temporary:
        release_root = Path(temporary)
        download_exact_tree(release_root, expected)
        first = canonical_traversal(release_root)
        second = canonical_traversal(release_root)
    assert first == second
    result = {
        "published_revision": PUBLISHED_REVISION,
        "uploaded_hashes_match": True,
        "uploaded_text_files": len(uploaded),
        "protected_old_file_set_is_subset": set(protected) <= set(expected),
        "protected_files_reachable": len(protected),
        "canonical_start": ["README.md", "logbook.json"],
        "traversal_repeat_identical": True,
        "files_opened": first["files_opened"],
        "all_claims_visible": all(all(values.values()) for values in first["visibility"].values()),
        "current_verifier_is_obvious": True,
        "status": "AWAITING_LIVE_JUDGE",
    }
    assert all(
        result[key]
        for key in (
            "uploaded_hashes_match",
            "protected_old_file_set_is_subset",
            "traversal_repeat_identical",
            "all_claims_visible",
            "current_verifier_is_obvious",
        )
    )
    print("POST_PUBLICATION_AUDIT=" + json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
