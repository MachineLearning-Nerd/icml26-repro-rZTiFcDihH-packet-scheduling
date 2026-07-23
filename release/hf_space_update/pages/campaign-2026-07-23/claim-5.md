# Claim 5 — ALG^Rs regret

**Verdict: BLOCKED · Confidence: LOW**

The source proof's displayed bound
`max_i 1/sqrt(N_i,t) <= sqrt(K/t)` is false for counts `(9999,1)`: the two
sides are `1` and `0.014142`. This is a proof gap, not a theorem counterexample.
The required accounting can instead be repaired pathwise by grouping realized
selections by type and applying Cauchy.

The exact uniform-log-threshold integrator checked 4,096 deadline states
(maximum ratio 1.26444), while a 12,000-state falsification route reached
1.31407; both are below `e/(e-1)=1.58198`. Eighty-seed learning stress runs
through T=32,768 also aligned.

However, the literal learning rule begins with every LCB equal to zero, making
`log(UCB/LCB)` and `exp(x)LCB` undefined. Every executable initialization is a
deviation not specified by the paper. The ambiguity is not counted as
falsification, but it blocks verification.
