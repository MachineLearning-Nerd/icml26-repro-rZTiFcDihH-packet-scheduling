"""Text-only verifier for the 2026-07-23 claim summaries."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2] / "evidence" / "2026-07-23"
EXPECTED = {
    1: "BLOCKED",
    2: "FALSIFIED",
    3: "FALSIFIED",
    4: "BLOCKED",
    5: "BLOCKED",
    6: "VERIFIED",
}


def main() -> None:
    rows = {
        claim: json.loads((ROOT / f"claim-{claim}.json").read_text())
        for claim in EXPECTED
    }
    assert {claim: row["verdict"] for claim, row in rows.items()} == EXPECTED
    assert rows[2]["ratio"] > rows[2]["theta_3"]
    assert rows[3]["tail_regret_per_round"] > 0.03
    assert rows[3]["last_loglog_slope"] > 0.9
    assert rows[6]["quantified_bijection_status"] == "unsat"
    assert all(row["negative_control_detected"] for row in rows.values())
    assert rows[1]["valid_counterexamples"] == 0
    assert rows[4]["valid_counterexamples"] == 0
    assert rows[5]["valid_counterexamples"] == 0
    print("CAMPAIGN_20260723_VERDICT=PASS")


if __name__ == "__main__":
    main()
