#!/usr/bin/env python3
"""Independent parser/checker for the Claim-4 minimax evidence."""
from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def valid_family(rows):
    try:
        for row in rows:
            n, m, k = int(row["n"]), int(row["m"]), int(row["epsilon_denominator"])
            p = min(n, m)
            family = math.comb(k - 1, p - 1)
            if row["family_size"] != str(family):
                return False
            if int(row["floor_log2_family_size"]) != family.bit_length() - 1:
                return False
            if m > math.isqrt(k) or row["delta"] != "1/2":
                return False
            dummy = n - m if n >= m else 0
            if int(row["certified_query_lower_bound"]) != dummy + family.bit_length() - 1:
                return False
        return True
    except (KeyError, TypeError, ValueError):
        return False


family = json.loads((ROOT / "raw_lower_bound.json").read_text())
exhaustive = json.loads((ROOT / "raw_exhaustive.json").read_text())
minimax = json.loads((ROOT / "raw_minimax.json").read_text())
assert len(family) == 6 and valid_family(family)
assert {row["case"] for row in family} == {"n_ge_m", "n_lt_m"}
assert len(exhaustive) == 3
for row in exhaustive:
    p, k = int(row["p"]), int(row["epsilon_denominator"])
    assert int(row["hard_instances"]) == math.comb(k - 1, p - 1)
    assert int(row["grid_lotteries"]) == math.comb(k + p - 1, p - 1)
    assert int(row["singleton_comparisons"]) == int(row["hard_instances"]) * int(row["grid_lotteries"])
assert len(minimax) == 64
assert all(int(row["alternatives"]) == int(row["exact_minimax_worst_case_queries"]) for row in minimax)

corrupted = [dict(row) for row in family]
corrupted[0]["family_size"] = "1"
assert not valid_family(corrupted)

checker = json.loads((ROOT / "checker_output.json").read_text())
controls = json.loads((ROOT / "negative_control_output.json").read_text())
proof = json.loads((ROOT / "proof_certificate.json").read_text())
assert checker["passed"] and checker["max_n"] >= 1_000_000
assert checker["single_agent_minimax_max_m"] == 64
assert controls["passed"] and all(value is True for key, value in controls.items() if key != "passed")
assert proof["status"] == "VERIFIED" and all(proof["obligations"].values())

print(json.dumps({"claim": 4, "independent_checker": "PASS", "family_rows": len(family),
                  "corruption_self_test_detected": True}, sort_keys=True))
