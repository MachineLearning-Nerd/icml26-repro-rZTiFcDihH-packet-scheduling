# Formal command ledger

This ledger records commands that produced, validated, or inspected campaign
evidence. Routine file reads (`sed`, `find`, `git status`) are not evidence
producers and are omitted.

## Startup and source

```text
orx skill
orx skill orx-experiment-tree
orx skill orx-evidence
orx skill orx-git
orx skill orx-compute
orx skill orx-lit
orx skill orx-reports
orx skill report
orx projects --json
orx runs a21843f7-988b-48f5-a6b3-9d30c7be4365
orx paper 2606.00835 --full
```

The paper e-print was fetched from
`https://export.arxiv.org/e-print/2606.00835` with an explicit browser
User-Agent. Its SHA-256 is
`cfecbd50bdaa81a774e044f8ce568ddd25880f39debeb3d81d796f7d05f5534f`.
The live verdict dataset was selected by exact
`space_id == "DineshAI/rZTiFcDihH"`. The judged Space was downloaded at exact
revision `8f84eab5754de43ee08dfc1bb9a792cde93cc6ab`.

## Fixed experiment command

Every node reports this identical command:

```text
uv run --frozen python -m repro.run_all
```

## Formal launches

```text
orx exp run 898b753e-f5e7-4783-b89f-a76f37a09f80 --backend local
orx exp run 3f0f31f8-880b-4b2e-85d0-0714f4ea3f25 --backend local
orx exp run 9c6e12d5-4923-4b77-afde-e86bd37f0d81 --backend local
orx exp run a6be341d-5a33-4273-a45b-9e6731493058 --backend local
orx exp run 024366a1-df74-47fb-bdfc-7262af94a042 --backend local
orx exp run e27b3b10-3c3d-48eb-9755-ec9f4fc92a58 --backend local
```

Each launch was followed by:

```text
orx exp wait <experiment-id> --timeout 480
orx logs <run-id> --bytes <bounded-byte-count>
```

The accepted run IDs are `79676866-910c-4895-b2d9-4603c3fa547a`,
`cb396f27-7f46-43a9-afad-d98731824cd1`,
`581f9bda-04a5-4356-a9ef-db0f8aa9ce57`,
`74b96f65-3615-413d-9933-56ac9dbfb2be`,
`1520ef60-bfa5-45fa-b9ed-008c1d68e0ed`, and
`487674a8-55ed-4f57-85ce-87c41696983f`.

Three early verifier-control runs failed and remain visible:
`11447c22-d73b-4cda-b69e-5df96ef42ad4`,
`5bb7e233-4547-47f0-824c-bb97e1f03760`, and
`bd5fc137-c790-4174-91c7-fed5cadba621`.

## Presentation and release validation

```text
uv run --frozen python repro/generate_report_figures.py
uvx --from marimo marimo check --fix notebooks/packet_scheduling_reproduction.py
uvx --from marimo marimo check --strict notebooks/packet_scheduling_reproduction.py
uv run --frozen python release/hf_space_update/repro/src/verify_campaign_20260723.py
uv run --frozen python repro/verify_space_subset.py --judged <protected-tree> --candidate <candidate-tree> --out <subset-check.json>
```

The `uvx` lint did not modify the locked experiment environment. No Hugging
Face upload command has been executed.
