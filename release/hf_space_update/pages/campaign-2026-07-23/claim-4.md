# Claim 4 — ALG^R2 regret

**Verdict: BLOCKED · Confidence: LOW**

The tested cell is nonvacuous and exactly tight: an expiring packet of mean
0.4 and a one-slot-slack packet of mean 0.8 give `p_hat=0.4`,
`E[ALG]=0.96`, `OPT=1.2`, and ratio exactly `1.25`.

Evidence routes:

- Z3 proved all 16 core p_hat inequalities for arbitrary valid confidence
  endpoints.
- 80-seed literal learning runs through T=32,768 had nonpositive 5/4-regret.
- Exact integration of 10,000 ordered mean pairs reached the 1.25 boundary
  with zero violations.
- A broader 10,000-instance falsification search reached 1.18705, with its
  exact expectation independently matched by 20,000 Monte Carlo seeds.

The source pseudocode omits single-set buffer cases, and the entire multi-round
learning potential was not independently mechanized. These limitations prevent
a universal VERIFIED verdict.
