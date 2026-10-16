# AI Deployment Economics Benchmark

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
| `instruction.md` | Task prompt |
| `environment/` | Docker environment and input data |
| `solution/` | Reference computation and memo |
| `tests/` | Verifier and expected values |
| `rubrics.json` | Scoring criteria |
| `tools/` | Package builder |

[Git and release workflow](GIT_TRACKING.md) ? [Submission guide](SUBMISSION_GUIDE.md)
