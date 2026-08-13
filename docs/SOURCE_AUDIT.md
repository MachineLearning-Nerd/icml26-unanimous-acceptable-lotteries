# Primary-source and scope audit

Paper: **Learning Unanimously Acceptable Lotteries via Queries**, by Davin
Choo, Paul W. Goldberg, and Nicholas Teh. See the
[arXiv record](https://arxiv.org/abs/2604.17505) and
[HTML source](https://arxiv.org/html/2604.17505).

OpenReview identifier: `daiccpXZfU`.

Pinned public TeX archive SHA-256:
`73dd9aa76258e676da3cdec4454a84e5dc576b680424e1366a4fff719ed6b3ab`.
The archive contains `main.tex`, Algorithms 1–3, and the proof appendices.
This is a finite membership-query theory problem; no unreleased experiment,
data, model weight, proprietary API, or GPU is required.

| Claim | Source anchor | Full executable reproduction | Control and boundary |
|---|---|---|---|
| C1 — halfspace recovery | Algorithm 1; Lemmas 3.1–3.2 | Exact edge bisection and rational recovery, with independent simplex evaluation, scaling rows, and exhaustive quantized instances. | An unquantized threshold violates the bounded-denominator premise; universal scaling remains proof-anchored. |
| C2 — deterministic feasibility | Algorithm 2; Theorem 3.3 | Source learn/restart/Select loop on feasible and infeasible instances, with exact membership-query accounting and independent finite LP-grid checks. | Ignoring a rejecting agent creates a false positive; the source loop is tested on complete finite instances. |
| C3 — randomized feasibility | Algorithm 3; Theorem 3.4 | Weighted multiset sampling without replacement, cached hyperplanes, global verification, violator doubling, seeded runs, and expectation certificate. | Disabling reweighting leaves first-round violators unresolved; finite runs do not replace the expectation proof. |
| C4 — lower bounds | Theorems 4.1–4.2 | Positive epsilon-grid singleton-feasibility family, decision-tree leaf count, minimax recurrence, Kraft/Yao certificate. | A non-singleton hard family invalidates the leaf-count argument; the source family is checked at finite calibration parameters. |
| C5 — prediction augmentation | Theorems 5.1–5.2 | Predicted-order Algorithm 2 trace, record-agent count, verification/elicitations, and accuracy/reversal controls. | Reversed advice changes the trace; the finite family demonstrates the mechanism while the theorem supplies the universal bound. |

The repository’s fail-closed publication gate requires a source anchor,
mechanism, result, negative control, and explicit scope for every claim. The
previous live score is 5/10; the current candidate awaits evaluation.
