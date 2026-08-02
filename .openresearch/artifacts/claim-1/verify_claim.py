#!/usr/bin/env python3
"""Independent parser/checker for the Claim-1 evidence files."""
from __future__ import annotations

import csv
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def valid_rows(rows):
    try:
        for row in rows:
            n = int(row["n"])
            m = int(row["m"])
            k = int(row["epsilon_denominator"])
            binding = int(row["binding_agents"])
            verification = binding * (n - binding + 1) + (n - binding)
            hyperplane = binding * (m + (m - 1) * (2 * k * k).bit_length())
            envelope = n * (n + 1) // 2 + binding * (
                m + (m - 1) * (2 * math.ceil(math.log2(k)) + 2)
            )
            if int(row["verification_queries"]) != verification:
                return False
            if int(row["hyperplane_queries"]) != hyperplane:
                return False
            if int(row["total_queries"]) != verification + hyperplane:
                return False
            if int(row["universal_total_envelope"]) != envelope:
                return False
            if verification + hyperplane > envelope:
                return False
        return True
    except (KeyError, TypeError, ValueError):
        return False


rows = list(csv.DictReader((ROOT / "raw_scaling.csv").open()))
assert len(rows) == 37
assert {row["regime"] for row in rows} == {
    "quadratic_verification", "independent_n", "independent_m", "independent_precision"
}
assert valid_rows(rows)

corrupted = [dict(row) for row in rows]
corrupted[0]["total_queries"] = str(int(corrupted[0]["total_queries"]) + 1)
assert not valid_rows(corrupted)

checker = json.loads((ROOT / "checker_output.json").read_text())
controls = json.loads((ROOT / "negative_control_output.json").read_text())
proof = json.loads((ROOT / "proof_certificate.json").read_text())
assert checker["passed"] and checker["max_n"] >= 65536 and checker["max_m"] >= 256
assert checker["max_epsilon_denominator"] >= 65536
quadratic = [row for row in rows if row["regime"] == "quadratic_verification"]
assert all(int(row["n"]) ** 2 / 4 <= int(row["verification_queries"]) <= int(row["n"]) ** 2 / 3 for row in quadratic)
assert checker["quadratic_direct_envelope"] == "n^2/4 <= verification_queries <= n^2/3"
assert controls["passed"] and all(value is True for key, value in controls.items() if key != "passed")
assert proof["status"] == "VERIFIED" and all(proof["obligations"].values())

print(json.dumps({
    "claim": 1,
    "independent_checker": "PASS",
    "rows_checked": len(rows),
    "corruption_self_test_detected": True,
}, sort_keys=True))
