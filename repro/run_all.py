"""Fixed OpenResearch entrypoint.

Children extend the committed verifier suite; the experiment command remains
unchanged across the tree.
"""

from __future__ import annotations

import json
import platform
import subprocess
import sys
import time
from pathlib import Path

from repro.src.packet_audit import audit
from repro.src.claim_campaign import run_direct_campaign
from repro.src.model_check_campaign import run_model_check_campaign
from repro.src.proof_certificates import run_proof_certificates
from repro.src.stress_campaign import run_stress_campaign


ARTIFACT_DIR = Path(".openresearch/artifacts/baseline")


def main() -> int:
    started = time.monotonic()
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)

    test = subprocess.run(
        [sys.executable, "-m", "pytest", "repro/tests", "-q"],
        check=False,
        text=True,
        capture_output=True,
    )
    print("=== CUMULATIVE REGRESSION ===")
    print(test.stdout, end="")
    if test.stderr:
        print(test.stderr, file=sys.stderr, end="")
    if test.returncode:
        return test.returncode

    payload = audit()
    audit_path = ARTIFACT_DIR / "claim_audit.json"
    audit_path.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    runtime = {
        "cpu": platform.processor() or platform.machine(),
        "machine": platform.machine(),
        "platform": platform.platform(),
        "python": sys.version,
        "runtime_seconds": time.monotonic() - started,
    }
    runtime_path = ARTIFACT_DIR / "runtime.json"
    runtime_path.write_text(
        json.dumps(runtime, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    print("=== BASELINE CLAIM AUDIT ===")
    print(json.dumps(payload, sort_keys=True))
    print("=== RUNTIME ===")
    print(json.dumps(runtime, sort_keys=True))
    run_direct_campaign()
    run_proof_certificates()
    run_stress_campaign()
    run_model_check_campaign()
    print("BASELINE_VERDICT=PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
