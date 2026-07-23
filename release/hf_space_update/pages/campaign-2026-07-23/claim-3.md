# Claim 3 — ALG^theta,U regret

**Verdict: FALSIFIED · Confidence: HIGH**

This route targets the upper bound directly; it does not rely on the paper's
Gaussian lower-bound proof.

- K=3 distinct deterministic reward distributions with means `(0.9,0.6,0.3)`
- rewards always lie in `[0,1]`
- fixed oblivious two-bounded arrival sequence
- literal monotone UCB rule with `delta=1/T`
- separate exact offline DP

| T | theta_3-regret | regret/T |
| ---: | ---: | ---: |
| 1,024 | -23.70 | -0.023145 |
| 4,096 | 62.25 | 0.015198 |
| 16,384 | 438.45 | 0.026761 |
| 65,536 | 2,163.30 | 0.033009 |

The last-doubling log-log slope is `1.15137`, and the tail regret rate is
strictly positive. This is linear rather than soft-O(sqrt(KT)). An independent
per-block lower bound passes, and a zero-regret mutation is rejected.
