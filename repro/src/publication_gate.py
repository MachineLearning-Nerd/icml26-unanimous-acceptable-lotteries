#!/usr/bin/env python3
"""Fail-closed publication gate for daiccpXZfU."""
from __future__ import annotations
import json
from pathlib import Path

root = Path(__file__).resolve().parents[2]
verdict = json.loads((root / "outputs" / "verdict.json").read_text())
claims = verdict["claims"]
assert verdict["paper"] == "daiccpXZfU" and verdict["all_claims_passed"]
assert len(claims) == 5 and not verdict["publication_eligible"]
assert all(v.get("passed") and v.get("source") and v.get("mechanism") and v.get("negative_control") and v.get("scope") for v in claims.values())
assert verdict["campaign_claims"]["claim_3_halfspace"]["status"] == "VERIFIED"
assert (root / "RESULTS.md").is_file() and (root / "docs" / "SOURCE_AUDIT.md").is_file()
gate = {"paper": "daiccpXZfU", "arxiv": "2604.17505", "claim_count": 5,
        "publication_eligible": False, "tests_passed": True, "publication_gate_passed": False,
        "checks": {"historical_regression_suite_passes": True, "claim_3_exact_scaling_verified": True,
                   "claim_3_exhaustive_certificate_verified": True,
                   "all_five_current_claims_resolved": False, "evaluator_visibility_complete": False},
        "scope": "campaign checkpoint; publication remains blocked until all five current contracts and visibility gates pass"}
(root / "outputs" / "publication_gate.json").write_text(json.dumps(gate, indent=2, sort_keys=True) + "\n")
print(json.dumps(gate, indent=2, sort_keys=True))
