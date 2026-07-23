import marimo

__generated_with = "0.23.14"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import matplotlib.pyplot as plt

    return mo, plt


@app.cell
def _(mo):
    mo.md(r"""
    # A bounded-reward stress test for online packet scheduling

    **Central result.** A source-faithful implementation of
    $\mathrm{ALG}^{\theta,U}$ on a fixed, oblivious, two-bounded packet
    family accumulates positive regret at an approximately linear rate.
    The evidence below is embedded from the completed CPU experiment; this
    notebook does not rerun the expensive campaign.
    """)
    return


@app.cell
def _():
    horizons = [1024, 4096, 16384, 65536]
    theta_regret = [
        -23.700000000003115,
        62.25000000005775,
        438.44999999914035,
        2163.300000013951,
    ]
    regret_rate = [
        -0.023144531250003042,
        0.0151977539062641,
        0.02676086425776003,
        0.033009338379119124,
    ]
    return horizons, regret_rate, theta_regret


@app.cell
def _(horizons, plt, theta_regret):
    positive_horizons = [h for h, r in zip(horizons, theta_regret) if r > 0]
    positive_regret = [r for r in theta_regret if r > 0]
    reference = [
        positive_regret[-1] * (h / positive_horizons[-1]) ** 0.5
        for h in positive_horizons
    ]
    figure, axis = plt.subplots(figsize=(8.2, 4.5))
    axis.loglog(
        positive_horizons,
        positive_regret,
        "o-",
        linewidth=2.6,
        color="#e76f51",
        label="observed positive theta-regret",
    )
    axis.loglog(
        positive_horizons,
        reference,
        "--",
        linewidth=2.0,
        color="#6b7280",
        label="sqrt(T) reference",
    )
    axis.set(
        title="Claim 3 counterexample grows faster than square-root regret",
        xlabel="horizon T",
        ylabel="positive theta_3-regret",
    )
    axis.grid(alpha=0.2, which="both")
    axis.legend(frameon=False)
    figure
    return


@app.cell
def _(horizons, mo):
    horizon_picker = mo.ui.slider(
        start=0,
        stop=len(horizons) - 1,
        step=1,
        value=len(horizons) - 1,
        label="Inspect a measured horizon",
        show_value=False,
    )
    horizon_picker
    return (horizon_picker,)


@app.cell
def _(horizon_picker, horizons, mo, regret_rate, theta_regret):
    selected = horizon_picker.value
    mo.callout(
        mo.md(
            f"""
            At **T={horizons[selected]:,}**, measured theta-regret is
            **{theta_regret[selected]:,.2f}**, or
            **{regret_rate[selected]:.5f} per round**.
            """
        ),
        kind="info",
    )
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Why this contradicts the upper-bound component

    The paper's contract is universal: for every valid instance,
    $\mathbb{E}[G_{\mathrm{OPT}}] \leq
    \theta_K\mathbb{E}[G_{\mathrm{ALG}}] +
    \widetilde O(\sqrt{KT})$.

    This instance uses:

    - three distinct deterministic reward distributions with means
      `(0.9, 0.6, 0.3)`;
    - rewards entirely in `[0,1]`;
    - a fixed oblivious two-bounded arrival sequence;
    - the paper's monotone UCB and epoch updates;
    - an independent subset-state dynamic program for OPT.

    The final regret rate is `0.0330093` and the last-doubling log-log
    slope is `1.15137`. A positive limiting rate is incompatible with a
    square-root upper bound. This route does **not** depend on the separate
    Gaussian inconsistency in the paper's lower-bound proof.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Claim-by-claim outcome

    | Claim | Verdict | Why |
    | --- | --- | --- |
    | 1 — EDF_Phi^L | BLOCKED | substantial aligned evidence, incomplete universal charging proof |
    | 2 — ALG^theta | FALSIFIED | OPT/ALG = 1.6 > theta_3 = 1.5 |
    | 3 — ALG^theta,U | FALSIFIED | bounded-reward linear theta-regret |
    | 4 — ALG^R2 | BLOCKED | exact tight core, incomplete full learning coupling |
    | 5 — ALG^Rs | BLOCKED | zero-LCB initialization undefined |
    | 6 — reduction | VERIFIED | parameterized bijection and reward coupling |

    The formal fixed command is
    `uv run --frozen python -m repro.run_all`. The detailed illustrated
    report is in `reports/packet-scheduling-claim-audit-2026-07-23/`.
    """)
    return


if __name__ == "__main__":
    app.run()
