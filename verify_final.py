#!/usr/bin/env python3
"""Check the published documentation and repository identity surfaces."""

import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parent
EXPECTED_STATUS = (
    "ALL_FIVE_CLAIMS_VERIFIED_SCOPED_FINITE_AUDIT_HISTORICAL_SCORE_5_OF_10_NO_CURRENT_SCORE"
)
EXPECTED_BRANCHES = 17
EXPECTED_COMMITS = 42
CANONICAL_IDENTITY = "MachineLearning-Nerd <MachineLearning-Nerd@users.noreply.github.com>"


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def load(name: str) -> dict:
    return json.loads((ROOT / name).read_text())


def branch_names() -> set[str]:
    refs = git(
        "for-each-ref",
        "--format=%(refname)",
        "refs/heads",
        "refs/remotes/origin",
    ).splitlines()
    names = set()
    for ref in refs:
        if ref.endswith("/HEAD"):
            continue
        names.add(ref.removeprefix("refs/heads/").removeprefix("refs/remotes/origin/"))
    return names


def main() -> None:
    required = load("EVIDENCE_MANIFEST.json")["required_evidence"]
    missing = [path for path in required if not (ROOT / path).exists()]
    if missing:
        raise SystemExit(f"missing evidence: {', '.join(missing)}")

    claims = load("claims.json")
    verdicts = load("reproduction_verdicts.json")
    if claims["overall_status"] != EXPECTED_STATUS:
        raise SystemExit("claims.json overall status is inconsistent")
    if verdicts["overall_status"] != EXPECTED_STATUS:
        raise SystemExit("reproduction_verdicts.json overall status is inconsistent")
    if set(verdicts["claims"]) != {"C1", "C2", "C3", "C4", "C5"}:
        raise SystemExit("claim set is incomplete")
    if any(status != "VERIFIED_SCOPED_HIGH_CONFIDENCE" for status in verdicts["claims"].values()):
        raise SystemExit("a claim is not marked verified scoped with high confidence")
    if verdicts["historical_live_score"]["points"] != 5 or verdicts["historical_live_score"]["total"] != 10:
        raise SystemExit("historical score record is inconsistent")
    if verdicts["candidate"]["revision"] != "b9ca864e0933fb79daa53802cc38bf971397eae8":
        raise SystemExit("candidate revision is inconsistent")
    if verdicts["candidate"]["publication_gate_passed"] is not True:
        raise SystemExit("publication gate is not recorded as passed")
    if verdicts["publication_allowed"] is not False or verdicts["official_author_endorsement"] is not False:
        raise SystemExit("publication or endorsement boundary is inconsistent")

    names = branch_names()
    if len(names) != EXPECTED_BRANCHES or "main" not in names or any(name.startswith("orx/") for name in names):
        raise SystemExit(f"unexpected branches: {sorted(names)}")

    commits = int(git("rev-list", "--all", "--count"))
    if commits != EXPECTED_COMMITS:
        raise SystemExit(f"expected {EXPECTED_COMMITS} reachable commits, found {commits}")

    identities = set(git("log", "--all", "--format=%an <%ae> | %cn <%ce>").splitlines())
    expected = f"{CANONICAL_IDENTITY} | {CANONICAL_IDENTITY}"
    if identities != {expected}:
        raise SystemExit(f"non-canonical commit identities: {sorted(identities)}")

    print(
        "FINAL_AUDIT=VERIFIED"
        f" branches={len(names)}"
        f" commits={commits}"
        " claims=C1:C5_verified_scoped"
        " historical_score=5/10"
        " current_score_claim=false"
        " publication_allowed=false"
    )


if __name__ == "__main__":
    main()
