# Primary-source and scope audit

Paper: **Learning Unanimously Acceptable Lotteries via Queries**, OpenReview
`daiccpXZfU`, arXiv [`2604.17505`](https://arxiv.org/abs/2604.17505).

Pinned public source: arXiv TeX archive SHA-256
`73dd9aa76258e676da3cdec4454a84e5dc576b680424e1366a4fff719ed6b3ab`.
The archive contains a complete `main.tex` with Algorithms 1–3 and all proof
appendices.  This is a finite membership-query theory problem, with no
unreleased experiment in the five anchored claims.

| Claim | Source anchor | Full executable reproduction |
|---|---|---|
| C1 | Algorithm 1; Lemmas 3.1–3.2 | Recover each quantized acceptability halfspace by source edge-threshold queries and compare to an independent oracle evaluation. |
| C2 | Algorithm 2; Theorem 3.3 | Execute deterministic learn/restart/LP feasibility on exhaustive small halfspace instances and count all membership queries. |
| C3 | Algorithm 3; Theorem 3.4 | Run source weighted sampling/reweighting with deterministic RNG seeds, verify feasible/infeasible outcomes and expected-query trend. |
| C4 | Theorems 4.1–4.2 | Construct the source singleton-feasibility/adversarial precision family and independently count indistinguishable query cells. |
| C5 | Theorems 5.1–5.2 | Run predicted-order Algorithm 2 and compare accurate, partially corrupted, and reverse orderings by record-agent/query count. |

## Fidelity boundary

Finite enumeration checks the full algorithms in their stated finite
membership-query model; it does not replace the source proofs of asymptotic
upper or lower bounds.  Every claim will include a control that violates a
necessary condition (e.g., unquantized threshold, ignored rejecting agent,
disabled reweighting, non-singleton lower-bound family, or reversed advice).
