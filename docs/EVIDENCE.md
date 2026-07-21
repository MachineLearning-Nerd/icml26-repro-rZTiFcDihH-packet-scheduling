# Evidence map

| Claim | Outcome | Executed evidence | Independent check / control |
|---|---|---|---|
| C1 EDF-Phi | finite source-equivalent check | 793 ordered 2-bounded packet cells, max OPT/EDF ratio 1.2857 | offline dynamic-programming scheduler, not the online rule |
| C2 ALG^theta | **falsified** | Source theta system closes for K=2..8; a valid K=3 cell has OPT=8 and ALG=5 | independent DP oracle; 1.6 > theta_3=1.5 |
| C3 theta learning lower bound | **falsified** | source static audit pins `X_p in [0,1]` and proof `X_0 ~ N(1,sigma)` | direct domain incompatibility, no numerical approximation |
| C4 ALG^R2 | source-rule check | 100 admissible UCB/LCB cells, all p-hat values in [1/5,1] | all branch boundaries enumerated |
| C5 ALG^Rs | source-rule check | 8,704 UCB/LCB/quantile cells | selected packet always meets Eq. (f_t_selection) threshold |
| C6 sleeping-bandit reduction | verified finite reduction | all 120 nonempty availability sets through K=6 | direct set-to-buffer and action-set bijection |

The finite sweeps validate literal executable components and deliberately do
not claim to prove general asymptotic theorems. The two falsifications are
reported because they invalidate their corresponding literal source claims.
