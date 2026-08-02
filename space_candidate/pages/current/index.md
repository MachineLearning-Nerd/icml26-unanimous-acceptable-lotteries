# Current verification

This page is the canonical evaluator entrypoint. Current code supersedes the toy verifier at judged revision `88488bc18db7974567008ee55dbea85871de82e4`; the historical pages remain reachable and unchanged.

Start with the [illustrated cumulative report](#/current-report), then inspect the [final release report and score forecast](#/release-report). The exact fixed command is `uv sync --frozen && uv run --frozen python repro/src/verify.py && uv run --frozen python repro/src/publication_gate.py`; inspect the [current cumulative verifier](https://huggingface.co/spaces/DineshAI/daiccpXZfU/blob/main/code/current_verify.py), [fail-closed release gate](https://huggingface.co/spaces/DineshAI/daiccpXZfU/blob/main/code/publication_gate.py), [pyproject.toml](https://huggingface.co/spaces/DineshAI/daiccpXZfU/blob/main/code/pyproject.toml), and [uv.lock](https://huggingface.co/spaces/DineshAI/daiccpXZfU/blob/main/code/uv.lock). All research compute ran on Hugging Face `cpu-upgrade`, with no GPU.

## Visibility matrix

| Claim | Canonical page | Code visible | Data inline | Raw link | Checker | Control | Exact claim tested | Reviewer verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | [Current Claim 1](#/current-claim-1) | Yes | Yes | Yes | Yes | Yes | Yes | VERIFIED |
| 2 | [Current Claim 2](#/current-claim-2) | Yes | Yes | Yes | Yes | Yes | Yes | VERIFIED |
| 3 | [Current Claim 3](#/current-claim-3) | Yes | Yes | Yes | Yes | Yes | Yes | VERIFIED |
| 4 | [Current Claim 4](#/current-claim-4) | Yes | Yes | Yes | Yes | Yes | Yes | VERIFIED |
| 5 | [Current Claim 5](#/current-claim-5) | Yes | Yes | Yes | Yes | Yes | Yes | VERIFIED |

No score increase is claimed. The previous live judged score remains **5/10** until the live judge evaluates a published revision.
