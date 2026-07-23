# Claim 6 — sleeping-bandit reduction

**Verdict: VERIFIED · Confidence: HIGH**

The reduction is parameterized, not inferred from a small sweep:

- map sleeping action `i` available at round `t` to one type-`i` packet with
  release and deadline both `t`;
- map every one-bounded packet buffer back to the set of represented types;
- duplicate same-type packets do not change the action set;
- the selected action and packet have the same reward sample under coupling.

A quantified SMT query for an action-set mismatch is unsatisfiable. A separate
K=257, T=1000 round-trip preserves all availability sets and cumulative reward.
The negative control changes a deadline away from its release and is detected.
