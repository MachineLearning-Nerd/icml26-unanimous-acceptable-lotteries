# Environment and reproduction boundary

## Locked software

- Python: `>=3.12,<3.13`
- Package manager: `uv`
- Lockfile: [`uv.lock`](uv.lock)
- Optional notebook dependency: `marimo==0.23.1`

Run the committed checks with:

```bash
uv sync --frozen
uv run --frozen python repro/src/verify.py
uv run --frozen python repro/src/publication_gate.py
```

The optional tutorial uses the same environment:

```bash
uv sync --frozen --extra notebook
uv run --frozen --extra notebook marimo edit notebooks/reproduction.py
```

## Source and compute

- Paper source: [arXiv:2604.17505](https://arxiv.org/abs/2604.17505)
- Pinned TeX archive SHA-256: `73dd9aa76258e676da3cdec4454a84e5dc576b680424e1366a4fff719ed6b3ab`
- Compute contract: Hugging Face `cpu-upgrade`, CPU-only
- GPU used: no
- Quantum or proprietary service required: no
- Data: constructed theorem-calibration families, not natural preference data

The audit is deterministic where seeds are listed in the claim artifacts. The
source-faithful finite checks are intended to be rerunnable; no claim here
means that the finite runs replace the paper’s universal proof obligations.
