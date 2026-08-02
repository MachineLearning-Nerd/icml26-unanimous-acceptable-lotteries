#!/usr/bin/env python3
"""Independent parser/checker for Claim-5 record-quality evidence."""
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
            levels = int(row["constraint_agents"])
            quality_r = int(row["quality_R"])
            verification = n + (n - levels) * quality_r
            elicitation = quality_r * (m + (m - 1) * (2 * k * k).bit_length())
            envelope = n * (quality_r + 1) + quality_r * (
                m + (m - 1) * (2 * math.ceil(math.log2(k)) + 2)
            )
            if int(row["verification_queries"]) != verification:
                return False
            if int(row["elicitation_queries"]) != elicitation:
                return False
            if int(row["total_queries"]) != verification + elicitation:
                return False
            if int(row["universal_R_plus_1_envelope"]) != envelope:
                return False
            if verification + elicitation > envelope:
                return False
        return True
    except (KeyError, TypeError, ValueError):
        return False


rows = list(csv.DictReader((ROOT / "raw_scaling.csv").open()))
assert len(rows) == 40 and valid_rows(rows)
quality = [row for row in rows if row["regime"] == "quality_R"]
assert [int(row["quality_R"]) for row in quality] == [1, 2, 4, 8, 16, 32, 64, 128, 256]
zero = [row for row in rows if row["regime"] == "zero_record_footnote"]
assert len(zero) == 1 and int(zero[0]["total_queries"]) == int(zero[0]["n"])

corrupted = [dict(row) for row in rows]
corrupted[-1]["verification_queries"] = "0"
assert not valid_rows(corrupted)

checker = json.loads((ROOT / "checker_output.json").read_text())
controls = json.loads((ROOT / "negative_control_output.json").read_text())
proof = json.loads((ROOT / "proof_certificate.json").read_text())
assert checker["passed"] and checker["max_n"] >= 65536
assert checker["max_m"] >= 256 and checker["max_epsilon_denominator"] >= 65536
assert controls["passed"] and all(value is True for key, value in controls.items() if key != "passed")
assert proof["status"] == "VERIFIED" and all(proof["obligations"].values())

print(json.dumps({"claim": 5, "independent_checker": "PASS", "rows_checked": len(rows),
                  "corruption_self_test_detected": True}, sort_keys=True))

