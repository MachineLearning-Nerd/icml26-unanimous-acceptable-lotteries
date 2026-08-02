#!/usr/bin/env python3
"""Standalone fail-closed checker for both Claim 3 evidence routes."""
import csv
import json
from pathlib import Path


artifact_dir = Path(__file__).resolve().parent
scaling = list(csv.DictReader((artifact_dir / "raw_scaling.csv").open()))
assert len(scaling) == 80
for row in scaling:
    m = int(row["m"])
    k = int(row["epsilon_denominator"])
    assert int(row["queries"]) == m + (m - 1) * (2 * k * k).bit_length()
assert max(int(row["m"]) for row in scaling) == 256
assert max(int(row["epsilon_denominator"]) for row in scaling) == 1024

exhaustive = json.loads((artifact_dir / "raw_exhaustive.json").read_text())
assert len(exhaustive) == 18
for row in exhaustive:
    m = int(row["m"])
    k = int(row["epsilon_denominator"])
    assert int(row["instances"]) == k * (k + 1) ** m
    assert int(row["lottery_cells_checked"]) > int(row["instances"])
assert max(int(row["m"]) for row in exhaustive) == 4
assert max(int(row["epsilon_denominator"]) for row in exhaustive) == 12

result = {"passed": True, "scaling_rows_checked": len(scaling),
          "exhaustive_settings_checked": len(exhaustive),
          "instances_recomputed": sum(int(row["instances"]) for row in exhaustive)}
(artifact_dir / "standalone_checker_output.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
print("CLAIM3_STANDALONE_CHECKER=" + json.dumps(result, sort_keys=True))
