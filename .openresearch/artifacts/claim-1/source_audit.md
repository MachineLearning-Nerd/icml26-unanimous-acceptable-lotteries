# Source audit: Claim 1

Source: arXiv 2604.17505 TeX retrieved 2026-08-02 from `https://export.arxiv.org/e-print/2604.17505` with SHA-256 `73dd9aa76258e676da3cdec4454a84e5dc576b680424e1366a4fff719ed6b3ab`.

Theorem 3.3 (`thm:ub_deterministic`) states that Algorithm 2 (`alg:cardinal_deterministic`) returns a unanimously acceptable lottery when one exists, returns `Null` otherwise, and uses `O(n^2 + nm log(1/epsilon))` queries.

The model quantifies over `n` agents and `m` alternatives. Utilities are in `[0,1]`, thresholds in `(0,1]`, `epsilon` is in `(0,1/2]`, `1/epsilon` is integral, and all utility and threshold values are integer multiples of `epsilon`. A membership query asks whether expected utility is at least the threshold. Equality is accepted.

Algorithm 2 repeatedly chooses the lexicographically maximum lottery satisfying learned halfspaces, scans unlearned agents in fixed order, learns the first violator's halfspace, and restarts. It may return `Null` only when `Select` is infeasible or LearnHyperplane returns `RejectAll`.
