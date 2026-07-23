# Evidence map

| Claim | Verdict | Direct evidence | Independent check / negative control |
| --- | --- | --- | --- |
| C1 EDF-Phi^L | BLOCKED | 6,817 exact states; T=65,536 literal stress; 20,000-instance falsification search | separate offline DP; pathwise width certificate; mutated bound rejected |
| C2 ALG^theta | FALSIFIED | valid K=3 cell has OPT=8 and ALG=5 | independent DP and theta residual; gain mutation rejected |
| C3 ALG^theta,U | FALSIFIED | bounded deterministic rewards give regret/T=0.0330093 and slope 1.151 | separate per-block lower bound; zero-regret mutation rejected |
| C4 ALG^R2 | BLOCKED | exact 1.25-tight cell; 16 SMT obligations; 80-seed T=32,768 stress | exact recursion matches 20,000-seed checker; p=0 mutation rejected |
| C5 ALG^Rs | BLOCKED | 4,096 exact states; 80-seed stress; pathwise accounting repair | separate offline DP; always-heaviest mutation rejected; zero-LCB start unresolved |
| C6 reduction | VERIFIED | parameterized construction and K=257,T=1000 round-trip | quantified mismatch query unsat; deadline mutation rejected |

The fixed command is:

```text
uv run --frozen python -m repro.run_all
```

It generates final claim bundles under
`.openresearch/artifacts/final_claims/claim_<n>/`, each containing:

- `claim_contract.json`
- `source_audit.md`
- `method.md`
- `raw_results.json`
- `independent_checker_output.json`
- `negative_control_output.json`
- `exact_command_environment.json`
- `limitations.md`
- `EVAL.md`

The illustrated article is
`reports/packet-scheduling-claim-audit-2026-07-23/report.md`. The text-only
Hugging Face payload, exact allowlist, and manifest are under `release/`.
