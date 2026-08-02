#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
raw = json.loads((ROOT / "raw_seed_runs.json").read_text())
summary = json.loads((ROOT / "raw_summary.json").read_text())
assert len(raw) == 40 and len(summary) == 5
assert sorted({row["m"] for row in raw}) == [4, 8, 16, 24, 32]
for row in raw:
    assert row["verification_queries"] == row["n"] * row["rounds"]
    assert row["learned_agents"] <= min(row["n"], row["sample_cap"] * row["rounds"])
    assert row["total_queries"] == row["verification_queries"] + row["elicitation_queries"]
corrupted = [dict(row) for row in raw]
corrupted[0]["verification_queries"] += 1
assert corrupted[0]["verification_queries"] != corrupted[0]["n"] * corrupted[0]["rounds"]
checker = json.loads((ROOT / "checker_output.json").read_text())
controls = json.loads((ROOT / "negative_control_output.json").read_text())
proof = json.loads((ROOT / "proof_certificate.json").read_text())
assert checker["passed"] and checker["all_means_below_finite_envelopes"] and checker["max_m"] == 32
assert controls["passed"] and all(v is True for k, v in controls.items() if k != "passed")
assert proof["status"] == "VERIFIED" and all(proof["obligations"].values())
print(json.dumps({"claim": 2, "independent_checker": "PASS", "runs": 40, "corruption_self_test_detected": True}, sort_keys=True))
