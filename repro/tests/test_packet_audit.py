from repro.src.packet_audit import PHI, audit, theta_system


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
