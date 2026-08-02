#!/usr/bin/env python3
"""Standalone fail-closed checker for Claim 3 raw scaling evidence."""
import csv
import json
from pathlib import Path


artifact_dir = Path(__file__).resolve().parent
rows = list(csv.DictReader((artifact_dir / "raw_scaling.csv").open()))
assert len(rows) == 80
for row in rows:
    m = int(row["m"])
    k = int(row["epsilon_denominator"])
    expected = m + (m - 1) * (2 * k * k).bit_length()
    assert int(row["queries"]) == expected
assert max(int(row["m"]) for row in rows) == 256
assert max(int(row["epsilon_denominator"]) for row in rows) == 1024
result = {"passed": True, "rows_checked": len(rows), "independent_formula": "m + (m-1)*bit_length(2*K^2)"}
(artifact_dir / "standalone_checker_output.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
print("CLAIM3_STANDALONE_CHECKER=" + json.dumps(result, sort_keys=True))
