# Online Packet Scheduling with Deadlines and Learning — reproduction audit

[![Open in molab](https://marimo.io/molab-shield.svg)](https://molab.marimo.io/github/MachineLearning-Nerd/icml26-repro-rZTiFcDihH-packet-scheduling/blob/master/notebooks/packet_scheduling_reproduction.py)

This CPU-only clean-room campaign audits all six judged claims from
[arXiv:2606.00835](https://arxiv.org/abs/2606.00835). The strongest new result
is a direct bounded-reward falsification of the ALG^theta,U upper bound:
theta_3-regret reaches **2,163.3 at T=65,536**, with tail regret/T
**0.0330093** and last-doubling slope **1.151**, rather than the claimed
soft-O(sqrt(KT)) behavior. The earlier ALG^theta counterexample is preserved:
the paper number is theta_3=**1.5**, while the observed OPT/ALG ratio is
**8/5=1.6**.

The sleeping-bandit reduction is now parameterically verified for arbitrary K
and T. Claims 1, 4, and 5 remain honestly `BLOCKED`: exact models, long-horizon
stress, analytical certificates, and dedicated falsification searches do not
replace their universal quantifiers.

| Claim | Assessment | Paper result | Observed evidence |
| --- | --- | --- | --- |
| 1 — EDF_Phi^L | BLOCKED | soft-O(sqrt(KT)) Phi-regret | aligned through T=65,536; 6,817 exact cells; no universal proof |
| 2 — ALG^theta | FALSIFIED | ratio <= theta_3=1.5 | ratio 1.6 on a valid six-packet instance |
| 3 — ALG^theta,U | FALSIFIED | soft-O(sqrt(KT)) theta-regret | regret/T=0.0330093 at T=65,536 |
| 4 — ALG^R2 | BLOCKED | soft-O(sqrt(KT)) 5/4-regret | exact 1.25-tight cell; full coupling unresolved |
| 5 — ALG^Rs | BLOCKED | soft-O(sqrt(KT)) e/(e-1)-regret | exact/stress alignment; zero-LCB initialization undefined |
| 6 — reduction | VERIFIED | equivalence for arbitrary K,T | quantified query unsat; K=257,T=1000 coupling passes |

The counterexamples and parameterized reduction are not downscaled. Finite
model checks and stress tests for Claims 1, 4, and 5 are explicitly bounded and
do not receive full-scale labels. All formal compute used local Apple arm64
CPU; Hugging Face cpu-upgrade and GPUs were not used. Compute cost was $0.

Read the [illustrated claim-by-claim report](reports/packet-scheduling-claim-audit-2026-07-23/report.md)
or the [self-contained marimo tutorial](notebooks/packet_scheduling_reproduction.py).
The notebook embeds the accepted evidence, so opening it does not rerun the
18-minute falsification campaign.

## Experiment log

The run command below is copied verbatim from every experiment status.

| Branch / experiment | Purpose or change | Exact run command | Assessment / outcome | Compute |
| --- | --- | --- | --- | --- |
| `master` | Publication surface | Not run as an experiment (publication surface) | Awaiting approved mirror | — |
| [`orx/frozen-judged-baseline`](https://github.com/MachineLearning-Nerd/icml26-repro-rZTiFcDihH-packet-scheduling/tree/orx/frozen-judged-baseline) | Freeze and rerun judged evidence | `uv run --frozen python -m repro.run_all` | Baseline reproduced; C2 preserved | local CPU, 10s |
| [`orx/faithful-theorem-contracts`](https://github.com/MachineLearning-Nerd/icml26-repro-rZTiFcDihH-packet-scheduling/tree/orx/faithful-theorem-contracts) | Direct C3 and C6 contracts | `uv run --frozen python -m repro.run_all` | C3 FALSIFIED; C6 VERIFIED | local CPU, 10s |
| [`orx/analytical-proof-certificates`](https://github.com/MachineLearning-Nerd/icml26-repro-rZTiFcDihH-packet-scheduling/tree/orx/analytical-proof-certificates) | SMT and accounting audit | `uv run --frozen python -m repro.run_all` | core obligations pass; C5 proof gap found | local CPU, 10s |
| [`orx/faithful-adversarial-stress`](https://github.com/MachineLearning-Nerd/icml26-repro-rZTiFcDihH-packet-scheduling/tree/orx/faithful-adversarial-stress) | Literal long-horizon learning rules | `uv run --frozen python -m repro.run_all` | C1/C4/C5 aligned, not universal | local CPU, 55s |
| [`orx/integrated-exact-route-audit`](https://github.com/MachineLearning-Nerd/icml26-repro-rZTiFcDihH-packet-scheduling/tree/orx/integrated-exact-route-audit) | Exact expectation and finite-state DP | `uv run --frozen python -m repro.run_all` | tight cores pass; initialization unresolved | local CPU, 1m15s |
| [`orx/dedicated-falsification-search`](https://github.com/MachineLearning-Nerd/icml26-repro-rZTiFcDihH-packet-scheduling/tree/orx/dedicated-falsification-search) | Mandatory fourth routes | `uv run --frozen python -m repro.run_all` | no valid C1/C4/C5 counterexample; all BLOCKED | local CPU, 18m04s |

Three failed runs are retained in the internal experiment log because they
caught verifier-control defects before acceptance. No failed run contributes
scientific evidence.

## Reproduce

The repository uses Python 3.12.11, one repository-level `.venv`, and the
committed `uv.lock`.

```bash
uv sync --frozen
uv run --frozen python -m repro.run_all
```

The fixed command regenerates every claim contract and cumulative verifier
under `.openresearch/artifacts/` in an OpenResearch run. For the bounded
tutorial only:

```bash
uv run marimo edit notebooks/packet_scheduling_reproduction.py
uv run marimo run notebooks/packet_scheduling_reproduction.py
```

## Evidence provenance

- Paper source: `https://export.arxiv.org/e-print/2606.00835`
- Retrieved: 2026-07-23
- SHA-256: `cfecbd50bdaa81a774e044f8ce568ddd25880f39debeb3d81d796f7d05f5534f`
- Validated baseline: `208fb9372e541152a1062f292163a2c017eaebd4`
- Previous live judged score: 6/12
- Protected judged Space revision: `8f84eab5754de43ee08dfc1bb9a792cde93cc6ab`

The live score remains 6/12 until an approved Hugging Face revision is
published and the judge evaluates it.
