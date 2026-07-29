# STATUS — daiccpXZfU

**State: PUBLICATION QUEUED — five source-anchored claims pass locally.**

- Effective anchored contract: five claims / 10 possible points.
- Pinned primary TeX source: arXiv `2604.17505`, source SHA-256
  `73dd9aa76258e676da3cdec4454a84e5dc576b680424e1366a4fff719ed6b3ab`.
- The complete algorithms, finite precision model, proofs, lower-bound family,
  and learning-augmented order construction are present in `main.tex`; no data,
  model weights, proprietary API, or GPU is needed.
- `python3 repro/src/verify.py` writes the five-claim verdict.
- `python3 repro/src/publication_gate.py` fails closed unless every claim has
  source, mechanism, control, scope, results, and source audit evidence.
- Public GitHub: `MachineLearning-Nerd/icml26-repro-daiccpXZfU-unanimous-acceptable-lotteries`
  at commit `0f105a8`.
- Atomically enqueued through `enqueue_backlog.py`. The shared publisher owns
  Space creation and is currently quota-blocked; no direct publish is made.
