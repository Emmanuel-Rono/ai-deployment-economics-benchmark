# Aq_Econ

An executable analytical benchmark for AI deployment investment decisions. An analyst evaluates three Q4 deployment plans using demand records, commercial terms, replay evidence and infrastructure quotations, then writes an investment-committee recommendation.

## Current version

- 500,000 workload version rows, 550,000 attempt events and 5,000 customer accounts.
- Ten generated input files totalling about 147 MiB.
- One requested deliverable: `recommendation.md`.
- A 35-criterion, 100-point rubric for substantive answer quality.
- Harbor 0.18.0: nop diagnostic reward **0.0**, oracle **1.0**, with no exceptions.

The five programmatic checks validate the memo and its headings. Substantive grading uses the rubric. Platform rubric scores and model difficulty have not been measured. See [run evidence](HARBOR_RUN_RESULTS.md).

## Repository layout

| Path | Purpose |
|---|---|
| `instruction.md` | Exact analyst prompt |
| `environment/` | Container definition and input data |
| `solution/` | Private reference computation and example memo |
| `tests/` | Output diagnostics and numerical reference targets |
| `rubrics.json` | Answer-quality criteria |
| `tools/` | Repository tooling; excluded from client ZIPs |

See [GitHub and submission guide](GIT_TRACKING.md) for initial push commands, Git LFS, local setup, packaging and exact-archive checks. Keep tested ZIPs and raw job logs under `.local-checks/`; Git ignores that directory.

Generated scenario material is fictional. Its declared licence is recorded in [LICENSE](LICENSE).
