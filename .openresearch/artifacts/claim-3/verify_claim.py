#!/usr/bin/env python3
"""Standalone fail-closed checker for Claim 3 exhaustive summaries."""
import json
from pathlib import Path


artifact_dir = Path(__file__).resolve().parent
rows = json.loads((artifact_dir / "raw_exhaustive.json").read_text())
assert len(rows) == 18
for row in rows:
    m = int(row["m"])
    k = int(row["epsilon_denominator"])
    assert int(row["instances"]) == k * (k + 1) ** m
    assert int(row["lottery_cells_checked"]) > int(row["instances"])
assert max(int(row["m"]) for row in rows) == 4
assert max(int(row["epsilon_denominator"]) for row in rows) == 12
result = {"passed": True, "settings_checked": len(rows),
          "instances_recomputed": sum(int(row["instances"]) for row in rows)}
(artifact_dir / "standalone_checker_output.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
print("CLAIM3_STANDALONE_CHECKER=" + json.dumps(result, sort_keys=True))
