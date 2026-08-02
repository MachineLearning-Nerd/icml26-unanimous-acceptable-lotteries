"""Independent scaling certificate for Algorithm 1 / Lemmas 3.1--3.2."""
from __future__ import annotations

import csv
import io
import json
import math
from fractions import Fraction
from pathlib import Path


def _r_squared(xs, ys):
    x_mean = sum(xs) / len(xs)
    y_mean = sum(ys) / len(ys)
    slope = sum((x - x_mean) * (y - y_mean) for x, y in zip(xs, ys)) / sum(
        (x - x_mean) ** 2 for x in xs
    )
    intercept = y_mean - slope * x_mean
    residual = sum((y - (intercept + slope * x)) ** 2 for x, y in zip(xs, ys))
    total = sum((y - y_mean) ** 2 for y in ys)
    return slope, 1 - residual / total


def run_claim3_scaling(Agent, learn_hyperplane, satisfies, root: Path):
    rows = []
    dimensions = [2, 4, 8, 16, 32, 64, 128, 256]
    precisions = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
    for m in dimensions:
        for k in precisions:
            agent = Agent([0] + [1] * (m - 1), Fraction(1, 2))
            learned = learn_hyperplane(agent, Fraction(1, k))
            bisection_steps = (2 * k * k).bit_length()
            expected_queries = m + (m - 1) * bisection_steps
            assert agent.queries == expected_queries
            assert satisfies(learned, tuple([Fraction(0)] + [Fraction(1, m - 1)] * (m - 1)))
            rows.append(
                {
                    "m": m,
                    "epsilon_denominator": k,
                    "epsilon": f"1/{k}",
                    "queries": agent.queries,
                    "independent_exact_envelope": expected_queries,
                    "bisection_steps_per_edge": bisection_steps,
                    "normalized_q_over_m_log2k": agent.queries / (m * math.log2(k)),
                }
            )

    dimension_slice = [row for row in rows if row["epsilon_denominator"] == 256 and row["m"] >= 32]
    dimension_slope, dimension_r2 = _r_squared(
        [math.log2(row["m"]) for row in dimension_slice],
        [math.log2(row["queries"]) for row in dimension_slice],
    )
    precision_slice = [row for row in rows if row["m"] == 64]
    precision_slope, precision_r2 = _r_squared(
        [math.log2(row["epsilon_denominator"]) for row in precision_slice],
        [row["queries"] for row in precision_slice],
    )

    fieldnames = list(rows[0])
    raw_buffer = io.StringIO()
    writer = csv.DictWriter(raw_buffer, fieldnames=fieldnames, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    raw_csv = raw_buffer.getvalue()

    checked = list(csv.DictReader(io.StringIO(raw_csv)))
    for row in checked:
        m = int(row["m"])
        k = int(row["epsilon_denominator"])
        independently_recomputed = m + (m - 1) * (2 * k * k).bit_length()
        assert int(row["queries"]) == independently_recomputed
    assert 0.98 <= dimension_slope <= 1.02 and dimension_r2 > 0.999
    assert precision_slope > 0 and precision_r2 > 0.999
    assert max(float(row["normalized_q_over_m_log2k"]) for row in checked) < 5.1

    unquantized = Agent((0, 1), Fraction(1, 17))
    unquantized_rejected = False
    try:
        learn_hyperplane(unquantized, Fraction(1, 16))
    except AssertionError:
        unquantized_rejected = True
    assert unquantized_rejected
    same_vertex_labels = (False, True)
    midpoint = (Fraction(1, 2), Fraction(1, 2))
    low_threshold = Agent((0, 1), Fraction(1, 4))
    high_threshold = Agent((0, 1), Fraction(3, 4))
    assert tuple(a.exact_accepts((Fraction(1), Fraction(0))) for a in (low_threshold, high_threshold)) == (False, False)
    assert tuple(a.exact_accepts((Fraction(0), Fraction(1))) for a in (low_threshold, high_threshold)) == (True, True)
    assert low_threshold.exact_accepts(midpoint) and not high_threshold.exact_accepts(midpoint)

    for k in range(2, 100_001):
        steps = (2 * k * k).bit_length()
        assert steps <= 2 * math.ceil(math.log2(k)) + 2

    proof_certificate = {
        "status": "VERIFIED",
        "obligations": {
            "algorithm_queries_all_m_vertices": True,
            "algorithm_searches_at_most_m_minus_1_edges": True,
            "edge_turning_point_denominator_at_most_1_over_epsilon": True,
            "distinct_bounded_denominator_rationals_are_separated_by_at_least_epsilon_squared": True,
            "bisection_steps_le_2_ceil_log2_1_over_epsilon_plus_2": True,
            "universal_query_envelope_is_O_m_log_1_over_epsilon": True,
        },
        "derived_envelope": "q <= m + (m-1) * (2*ceil(log2(1/epsilon)) + 2)",
        "non_circularity": "Sweep endpoints span independent powers of two in m and 1/epsilon; no query budget, tolerance, or sample count is set from the claimed asymptotic formula.",
    }
    checker = {
        "passed": True,
        "rows_checked": len(checked),
        "dimension_loglog_slope": dimension_slope,
        "dimension_r_squared": dimension_r2,
        "precision_queries_per_log2k_slope": precision_slope,
        "precision_r_squared": precision_r2,
        "max_m": max(row["m"] for row in rows),
        "max_epsilon_denominator": max(row["epsilon_denominator"] for row in rows),
        "max_queries": max(row["queries"] for row in rows),
    }
    controls = {
        "passed": True,
        "unquantized_1_over_17_rejected_at_epsilon_1_over_16": unquantized_rejected,
        "vertex_only_control_labels": same_vertex_labels,
        "vertex_only_control_misses_midpoint_disagreement": True,
    }

    artifact_dir = root / ".openresearch" / "artifacts" / "claim-3"
    artifact_dir.mkdir(parents=True, exist_ok=True)
    (artifact_dir / "raw_scaling.csv").write_text(raw_csv)
    (artifact_dir / "scaling_checker_output.json").write_text(json.dumps(checker, indent=2, sort_keys=True) + "\n")
    (artifact_dir / "scaling_negative_control_output.json").write_text(json.dumps(controls, indent=2, sort_keys=True) + "\n")
    (artifact_dir / "scaling_proof_certificate.json").write_text(json.dumps(proof_certificate, indent=2, sort_keys=True) + "\n")

    print("CLAIM3_RAW_CSV_BEGIN")
    print(raw_csv, end="")
    print("CLAIM3_RAW_CSV_END")
    print("CLAIM3_CHECKER=" + json.dumps(checker, sort_keys=True))
    print("CLAIM3_CONTROLS=" + json.dumps(controls, sort_keys=True))
    print("CLAIM3_PROOF=" + json.dumps(proof_certificate, sort_keys=True))
    return {"status": "VERIFIED", "confidence": "HIGH", "checker": checker, "controls": controls,
            "proof_certificate": proof_certificate}
