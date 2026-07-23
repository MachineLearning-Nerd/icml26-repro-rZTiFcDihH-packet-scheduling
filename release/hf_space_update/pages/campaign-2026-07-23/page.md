# Claim-by-claim reproduction campaign — 2026-07-23

The fixed command is:

```text
uv run --frozen python -m repro.run_all
```

All accepted runs used local Apple arm64 CPU, Python 3.12.11, the committed
`uv.lock`, and deterministic seeds. Hugging Face compute was not needed; CPU
cost was $0.

| Claim | Verdict | Confidence | Strongest direct evidence |
| --- | --- | --- | --- |
| 1 | BLOCKED | LOW | 6,817 exact finite states plus T=65,536 stress; universal charging proof unresolved |
| 2 | FALSIFIED | HIGH | OPT/ALG = 8/5 = 1.6 > theta_3 = 1.5 |
| 3 | FALSIFIED | HIGH | bounded deterministic rewards give tail regret/T = 0.0330093 and slope 1.151 |
| 4 | BLOCKED | LOW | exact 1.25-tight cell, 16 SMT obligations, 80-seed stress; full coupling unresolved |
| 5 | BLOCKED | LOW | exact expectation and accounting repair; literal zero-LCB initialization undefined |
| 6 | VERIFIED | HIGH | quantified bijection query is unsat; K=257,T=1000 coupling passes |

`BLOCKED` is deliberate: three materially different verification routes and a
fourth falsification route did not justify a universal verdict for Claims 1,
4, or 5. The evidence files and executable verifier are under
`evidence/2026-07-23/` and `repro/src/verify_campaign_20260723.py`.
