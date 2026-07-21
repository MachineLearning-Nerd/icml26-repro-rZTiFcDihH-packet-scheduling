# Online Packet Scheduling with Deadlines and Learning — reproduction audit

This is a CPU-only, clean-room audit of arXiv:2606.00835v1 (OpenReview
`rZTiFcDihH`). The paper does not release code; the pinned TeX source is in
`source/`, and all executable evidence is original and explicitly labelled as
such.

## Outcome

Four claims have direct executable source-equivalence checks. Two central
claims are falsified rather than force-fit:

- **C2:** Literal ALG^theta gets gain 5 while an independent offline dynamic
  program gets 8 on a valid ordered three-type, two-bounded input, so 1.6 is
  greater than theta_3=1.5.
- **C3:** The lower-bound proof samples Gaussian packet rewards despite the
  paper’s stated `[0,1]` reward model.

Run the audit locally:

```bash
PYTHONPATH=. .venv/bin/python -m pytest repro/tests -q
PYTHONPATH=. .venv/bin/python repro/src/packet_audit.py --out outputs/claim_audit.json
```

See `docs/EVIDENCE.md` and `outputs/claim_audit.json` for the full contract,
controls, and raw results.
