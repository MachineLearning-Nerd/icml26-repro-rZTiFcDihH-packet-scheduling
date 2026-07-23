from repro.src.stress_campaign import _run_r2, _run_rs


def test_r2_and_rs_smoke():
    r2 = _run_r2(128, 44)
    rs = _run_rs(128, 55)
    assert r2[1] > 0
    assert rs[1] > 0
    assert all(value == value for value in (*r2, *rs))
