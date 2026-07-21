# Status — Online Packet Scheduling with Deadlines and Learning

## State

`publication_queued` — full local gate passed and public GitHub handoff is
complete; the shared drain is the only Hugging Face publisher.

## Source and scope

- Pinned source target: arXiv `2606.00835v1`.
- All six anchored claims are literal definitions, algorithms, finite-
  competitive-ratio constructions, or regret/lower-bound statements in the
  source. They do not depend on a withheld benchmark, checkpoint, or GPU run.
- The authors do not provide executable code. The reproduction will therefore
  be explicitly clean-room and will retain the TeX source, implementations,
  exhaustive finite instances, independent oracle checks, and destructive
  controls. No result will be described as an author-code rerun.

## Planned claim gates

1. EDF-Φ UCB scheduling and its finite packet-instance regret behaviour.
2. Solve the source θ_K system, enumerate the 2-bounded competitive cases, and
   independently compute the offline optimum.
3. Verify ALG^θ,U and the stated √T lower-bound gadget on source-defined cells.
4. Verify the randomized 2-bounded ALG^R2 decision probabilities and 5/4
   finite potential inequality across all small packet states.
5. Verify the randomized s-bounded construction and e/(e−1) potential/rate
   certificate on its literal finite state space.
6. Exhaustively map 1-bounded K-OPSD arrivals to sleeping-bandit availability
   sets and compare gain/regret definitions.

## Completed gate

- Pinned source archive and SHA-256 are retained under `source/` and `outputs/`.
- The clean-room executable has 2/2 tests passing and retains raw claim output.
- C1, C4, C5, and C6 have source-rule checks; C2 and C3 are explicitly
  falsified with destructive controls rather than misreported as verified.
- Trackio has the required index, per-claim pages, Methods, Negative controls,
  and Conclusion; captured commands are relative.
- Public GitHub commit is `e6dca3f917fecff47bffe7f88d3056970ec89e00`.

FULL_GATE_READY: rZTiFcDihH

## Next action

The canonical enqueue handoff is next. Do not create or publish a Hugging Face
Space directly; wait for the shared drain and then verify its public readback.
