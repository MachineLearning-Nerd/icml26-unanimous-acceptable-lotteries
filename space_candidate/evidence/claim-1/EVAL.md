# Evaluation

Run the repository's fixed command. The Claim-1 verifier writes raw CSV and JSON evidence, then `.openresearch/artifacts/claim-1/verify_claim.py` independently parses it. Any failed scientific assertion or checker assertion exits nonzero.

The result may be called `VERIFIED` only if the literal implementation, independent checker, proof obligations, and all negative controls pass. Regression checks for the previously accepted Claim-3 certificate run in the same command.
