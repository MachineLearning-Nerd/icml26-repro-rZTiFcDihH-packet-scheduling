# Status — Online Packet Scheduling with Deadlines and Learning

## State

`awaiting_judge` — the claim campaign is complete, the approved additive
Hugging Face revision is published, and the presentation artifacts are mirrored
to the default branch. No score increase is claimed before the live judge runs.

## Source and compute

- Paper: arXiv `2606.00835v1`
- Source SHA-256:
  `cfecbd50bdaa81a774e044f8ce568ddd25880f39debeb3d81d796f7d05f5534f`
- Validated baseline: `208fb9372e541152a1062f292163a2c017eaebd4`
- Fixed command: `uv run --frozen python -m repro.run_all`
- Environment: Python 3.12.11, `uv`, one repository `.venv`, committed lock
- Compute: local Apple arm64 CPU only; no HF cpu-upgrade and no GPU
- Protected Space revision:
  `DineshAI/rZTiFcDihH@8f84eab5754de43ee08dfc1bb9a792cde93cc6ab`
- Published candidate revision:
  `DineshAI/rZTiFcDihH@3591f28e98d375687f4ac00fb48686edd1ef714f`

## Claim status

| Claim | Verdict | Confidence | Basis |
| --- | --- | --- | --- |
| 1 | BLOCKED | LOW | three aligned verification routes and no counterexample; universal charging proof incomplete |
| 2 | FALSIFIED | HIGH | OPT/ALG=1.6 > theta_3=1.5 |
| 3 | FALSIFIED | HIGH | bounded-reward family has linear theta-regret |
| 4 | BLOCKED | LOW | exact 1.25-tight core; full learning coupling incomplete |
| 5 | BLOCKED | LOW | accounting repaired; literal zero-LCB initialization undefined |
| 6 | VERIFIED | HIGH | parameterized bijection and reward coupling |

Every LOW-confidence claim completed analytical, long-horizon, exact-model,
and dedicated falsification routes. A missing counterexample was not converted
to verification.

## Publication verification

The published update is text-only and additive. The judged 26-file set is a
subset of the 42-file published revision; unchanged old hashes match, the old
index is a prefix of the new index, and all old navigation nodes are preserved.
All 18 uploaded files independently match the approved SHA-256 manifest under
`release/`.

Current live judged score: **6/12**. No score increase is claimed before a new
live judge verdict.
