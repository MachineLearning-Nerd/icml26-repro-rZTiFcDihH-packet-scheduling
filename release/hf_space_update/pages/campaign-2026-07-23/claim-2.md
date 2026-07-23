# Claim 2 — ALG^theta competitive ratio

**Verdict: FALSIFIED · Confidence: HIGH**

For the valid three-type, two-bounded six-packet instance recorded in
`evidence/2026-07-23/claim-2.json`, the independent subset-state DP schedules
packets worth `1+2+2+3=8`. Literal ALG^theta schedules `1+1+3=5`.

Therefore:

```text
OPT / ALG^theta = 8 / 5 = 1.6 > theta_3 = 1.5
```

The theta system is independently solved with residual zero. Deterministic
rewards are supported on the paper's required bounded domain. This previously
full-credit evidence is preserved in the cumulative regression.
