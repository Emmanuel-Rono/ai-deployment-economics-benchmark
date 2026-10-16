# Build report

## Package

The task contains ten input files across SQLite, JSONL, CSV and PDF. Input size is 154,524,774 bytes (147.37 MiB).

| Dataset | Count |
|---|---:|
| Workload versions | 500,000 |
| Logical requests | 450,000 |
| Completed latest requests | 442,622 |
| Older revisions | 50,000 |
| Cancelled latest requests | 7,378 |
| Inference attempts | 550,000 |
| Accounts / route groups | 5,000 / 100 |
| Replay batches / model-use-case cells | 5,000 / 6 |
| Routing records / current rules | 500 / 300 |
| Infrastructure quotations / current offers | 360 / 36 |
| September hourly buckets | 720 |

`product_research.pdf` is the single distractor: one of ten input files.

## Reference result

| Plan | Q4 contribution (USD) | GPUs Oct / Nov / Dec |
|---|---:|---|
| P1 | 2,904,170.42 | 2 / 2 / 2 |
| P2 | 2,919,636.25 | 5 / 5 / 5 |
| P3 | 2,921,547.55 | 4 / 4 / 4 |

All plans satisfy the operating requirements. P3 leads P1 by USD 17,377.14 and P2 by USD 1,911.30. Differences are calculated before rounding.

## Verification

- SQLite integrity and input record counts checked.
- Reference calculations reconciled with expected plan and monthly values.
- Independent aggregate-first SQL reconstruction agrees within USD 0.01.
- Rubric: 35 criteria; 100 positive points; 35 recommendation points; 10 instruction-following points.
- Verifier: five memo-delivery and heading checks.
- Harbor 0.18.0 runs, archive fingerprint and logs: HARBOR_RUN_RESULTS.md.

## Environment

Python 3.12, pypdf 6.1.1, four CPUs and 8 GiB RAM. The Docker base image is pinned by digest. Inputs are synthetic scenario records licensed as specified in LICENSE.
