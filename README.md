# AI Deployment Economics Benchmark

<<<<<<< HEAD
An executable benchmark for evaluating deployment investment decisions using operational, commercial and financial evidence.

The task compares three Q4 2026 deployment plans and requires an investment-committee recommendation supported by the supplied data.

## Dataset

| Component | Records |
|---|---:|
| Workload versions | 500,000 |
| Inference attempts | 550,000 |
| Customer accounts | 5,000 |
| Replay batches | 5,000 |
| Routing records | 500 |
| Infrastructure quotations | 360 |
=======
An analytical benchmark evaluating AI agents’ ability to recommend an enterprise AI deployment plan using operational, commercial and financial evidence. Includes a real dataset, an executable reference solution, a weighted scoring rubric and Harbor-based validation.
>>>>>>> 8ef100045c9a4170ffb3afb668b425419532f127

Ten input files span SQLite, JSONL, CSV and PDF, totalling 147.37 MiB. Dataset provenance and terms are recorded in [LICENSE](LICENSE).

## Evaluation

- Deliverable: `recommendation.md`.
- Rubric: 35 criteria, 100 points.
- Harbor version: 0.18.0.
- Local verification: nop 0.0; oracle 1.0; zero exceptions.

The verifier checks the memo and its four headings. The rubric scores the recommendation, financial evidence, citations, reconciliation, operating constraints and risks. [Run results](HARBOR_RUN_RESULTS.md).

## Project structure

| Path | Contents |
|---|---|
<<<<<<< HEAD
| `instruction.md` | Task prompt |
| `environment/` | Docker environment and input data |
| `solution/` | Reference computation and memo |
| `tests/` | Verifier and expected values |
| `rubrics.json` | Scoring criteria |
| `tools/` | Package builder |

[Git and release workflow](GIT_TRACKING.md) ? [Submission guide](SUBMISSION_GUIDE.md)
=======
| `instruction.md` | analyst prompt |
| `environment/` | Container definition and input data |
| `solution/` | Private reference computation and example memo |
| `tests/` | Output diagnostics and numerical reference targets |
| `rubrics.json` | Rubrics |
| `tools/` | Repository tooling; excluded from client ZIPs |


>>>>>>> 8ef100045c9a4170ffb3afb668b425419532f127
