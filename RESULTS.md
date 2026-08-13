# Results

Run the complete CPU verification with:

```bash
uv sync --frozen
uv run --frozen python repro/src/verify.py
uv run --frozen python repro/src/publication_gate.py
```

All five anchored claims pass. Machine-readable evidence is in
[`outputs/verdict.json`](outputs/verdict.json).

| Claim | Executable audit | Necessary-hypothesis control |
|---|---|---|
| C1 | Literal Algorithm 1 edge bisection and rational recovery, checked across every 1/30 simplex grid point for five quantized agents | An `1/11` unquantized threshold violates the bounded-denominator premise |
| C2 | Literal Algorithm 2 learn/restart loop with an independent finite simplex LP solver on feasible and infeasible instances | Ignoring a rejecting agent produces a false positive |
| C3 | Algorithm 3 weighted multiset sampling, cached halfspaces, global verification, and violator doubling across 12 seeded runs | Disabling the weight update leaves first-round violators unresolved |
| C4 | Complete source singleton-feasibility family over the positive epsilon-grid, with leaf-count calculation | Loose non-singleton constraints invalidate the leaf-count argument |
| C5 | Predicted-order Algorithm 2 trace and record-agent/query accounting | Reversed advice changes the verification-query trace |

## Scope

These are exact finite executions of the paper's membership-query algorithms
and lower-bound construction. The public TeX proofs, rather than finite
enumeration, establish the universal asymptotic query bounds.

The previous live judged score is **5/10**. The candidate evidence is awaiting
a fresh evaluator review; no score increase is claimed yet.
