from repro.src.packet_audit import PHI, audit, theta_system
from repro.src.claim_campaign import (
    run_theta_learning_counterexample,
    verify_claim_6,
)
from repro.src.proof_certificates import (
    verify_edf_phi_obligations,
    verify_r2_phat_obligations,
    verify_rs_proof_accounting,
)
from repro.src.model_check_campaign import (
    verify_claim_1_model,
    verify_claim_4_model,
    verify_claim_5_model,
)


def test_theta_known_values_and_system_residuals():
    assert abs(theta_system(2)[0] - 2**0.5) < 1e-10
    assert abs(theta_system(3)[0] - 1.5) < 1e-10
    for k in range(2, 9):
        theta, xs = theta_system(k)
        assert 2**0.5 - 1e-12 <= theta < PHI
        assert abs(xs[k - 1] - (theta + 1) * xs[k - 2]) < 1e-10


def test_full_claim_audit_controls():
    result = audit()
    assert result["C1_edf_phi"]["finite_certificate_pass"]
    assert result["C2_theta_competitive"]["theta_system_pass"]
    assert result["C2_theta_competitive"]["outcome"] == "falsified"
    assert result["C2_theta_competitive"]["violations"]
    assert result["C3_theta_learning_lower_bound"]["source_domain_mismatch"]
    assert result["C4_randomized_R2"]["probability_range_pass"]
    assert result["C5_randomized_Rs"]["threshold_pass"]
    assert result["C6_sleeping_bandit_reduction"]["bijection_pass"]


def test_theta_learning_counterexample_becomes_linear():
    small = run_theta_learning_counterexample(1024)
    large = run_theta_learning_counterexample(4096)
    assert small["theta_regret"] > 0
    assert large["theta_regret"] > 3.5 * small["theta_regret"]
    assert large["theta_regret"] / large["horizon"] > 0.02


def test_parameterized_sleeping_bandit_reduction():
    result = verify_claim_6()
    assert result["verdict"] == "VERIFIED"
    assert result["quantified_bijection_status"] == "unsat"
    assert result["negative_control_detected"]


def test_analytical_proof_obligations_and_gap():
    assert verify_edf_phi_obligations()["optimism_charge_smt_unsat"]
    assert verify_r2_phat_obligations()["all_16_smt_obligations_unsat"]
    rs = verify_rs_proof_accounting()
    assert not rs["source_inequality_holds"]
    assert rs["balanced_negative_control_holds"]


def test_exact_model_checks_and_controls():
    claim_1 = verify_claim_1_model()
    claim_4 = verify_claim_4_model()
    claim_5 = verify_claim_5_model()
    assert claim_1["competitive_core_pass"]
    assert claim_1["negative_control"]["detected"]
    assert claim_4["competitive_core_pass"]
    assert claim_4["negative_control"]["detected"]
    assert claim_5["competitive_core_pass"]
    assert claim_5["negative_control"]["detected"]
