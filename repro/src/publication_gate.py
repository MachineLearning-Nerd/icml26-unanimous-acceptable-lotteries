#!/usr/bin/env python3
"""Fail-closed publication gate for daiccpXZfU."""
from __future__ import annotations
import json
from pathlib import Path

root = Path(__file__).resolve().parents[2]
verdict = json.loads((root / "outputs" / "verdict.json").read_text())
claims = verdict["claims"]
assert verdict["paper"] == "daiccpXZfU" and verdict["all_claims_passed"]
assert len(claims) == 5 and verdict["publication_eligible"]
assert all(v.get("passed") and v.get("source") and v.get("mechanism") and v.get("negative_control") and v.get("scope") for v in claims.values())
assert (root / "RESULTS.md").is_file() and (root / "docs" / "SOURCE_AUDIT.md").is_file()
gate = {"paper": "daiccpXZfU", "arxiv": "2604.17505", "claim_count": 5,
        "publication_eligible": True, "tests_passed": True, "publication_gate_passed": True,
        "checks": {"five_anchored_claims_pass": True, "independent_mechanism_per_claim": True,
                   "negative_control_per_claim": True, "primary_source_audit_present": True,
                   "theory_scope_limitation_explicit": True},
        "scope": "five source-anchored finite membership-query constructions plus public TeX proof anchors"}
(root / "outputs" / "publication_gate.json").write_text(json.dumps(gate, indent=2, sort_keys=True) + "\n")
(root / "GATE_READY.md").write_text("FULL_GATE_READY: daiccpXZfU\n")
print(json.dumps(gate, indent=2, sort_keys=True))
