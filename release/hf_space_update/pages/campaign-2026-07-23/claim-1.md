# Claim 1 — EDF_Phi^L regret

**Verdict: BLOCKED · Confidence: LOW**

Contract: for every 2- or 3-bounded K-OPSD instance, expected Phi-regret is
soft-O(sqrt(KT)).

Four routes were completed:

1. Z3 proved the generic optimism charge; 100,000 harmonic and 10,000 Cauchy
   checks passed.
2. The literal learner was stressed through T=65,536 on a valid 3-bounded
   block; positive Phi-regret was zero.
3. A separate DP exhaustively checked 6,817 K=2/3 finite states; maximum
   known-mean ratio was 1.25 < Phi.
4. A 20,000-instance falsification search found no violation; the hardest
   ratio was 1.313846 and its repeated learner run remained nonpositive.

No route independently mechanized the complete universal 3-bounded charging
bijection. A finite search without a counterexample is not verification.
