# Method

The implementation samples integer positions from the labeled weighted multiset without replacement and maps them through exact cumulative weights. It runs exact Algorithm 3 on epsilon-grid coordinate-basis families with 32,768 agents, `m=4..32`, and eight deterministic seeds per dimension. It reports means and 95% confidence intervals, verification and elicitation queries separately, and finite expectation envelopes reconstructed from the proof constants.

An independent proof certificate carries the universal expectation quantifier. Controls distinguish without-replacement sampling, reweighting, and cached elicitation.
