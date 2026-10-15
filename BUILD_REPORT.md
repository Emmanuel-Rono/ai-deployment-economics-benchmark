# Current prompt correction - memo only

The user supplied the exact agreed text. instruction.md now contains it verbatim. The only required output is recommendation.md; CSV, table, precision and diagnostic disclosures are no longer compulsory. The reference solver emits only the memo. The rubric is now 35 criteria and 100 points (recommend 35, instruction following 10), with displayed precision respected. Five file/heading checks replace the old CSV diagnostics. Updated archive/run evidence is recorded separately in HARBOR_RUN_RESULTS.md. Inputs and economic calculations remain unchanged.

The sections below record the preceding merge and its historical 66-item/40-check contract, which is superseded by this correction.

# Merged package build report - 15 October 2026

## Sources and scope

Merged the expanded inputs, numerical solution, expected values and 66-item rubric from the sibling `AQ_Econ2` package into this `Aq_Econ` workspace. Retained the less-leading prompt agreed in this chat, permissive diagnostic checks and local operator tools. Aligned the rubric to remove compulsory diagnostic counts and October contribution. The source directory was not modified. The previous workspace package and notes were backed up under `.local-checks/pre-merge-20261015-152152.zip`.

All ten data files match the source input SHA-256 manifest. The obsolete `environment/data/data_dictionary.md` was replaced by the source's `data_dictionary.pdf` so there is only one current dictionary.

## Verified input inventory

- 500,000 workload version rows for 450,000 logical requests.
- 50,000 older revisions; 7,378 cancelled latest requests; 442,622 completed latest requests.
- 550,000 observed attempt events.
- 5,000 customer accounts in 100 route groups.
- 5,000 replay batches across six model/use-case cells, each batch evaluating 100 observations.
- 500 routing rows resolving to 300 current rules.
- 360 offer quotations resolving to 36 current offers for 12 pools and three months; one eligible pool per month.
- 720 September hourly buckets.
- Ten data files, four formats (SQLite, JSONL, CSV, PDF), three categories (database, spreadsheet, text).
- Total input size: 154,524,774 bytes (147.37 MiB). Single distractor: product_research.pdf (10% of files).

## Recomputed decision

| Plan | Q4 contribution (USD) | GPUs Oct/Nov/Dec | Feasible |
|---|---:|---|---|
| P1 | 2,904,170.42 | 2/2/2 | Yes |
| P2 | 2,919,636.25 | 5/5/5 | Yes |
| P3 | 2,921,547.55 | 4/4/4 | Yes |

P3 wins by USD 17,377.14 over P1 and USD 1,911.30 over P2 using unrounded calculations. Its October contribution is USD 967,057.16; disclosure of that diagnostic is optional. The differences between rounded displayed totals may differ by a cent from differences computed before rounding.

## Checks performed before packaging

- SQLite integrity, workload populations, CSV counts and input identity checks.
- Reference recomputation: all plans, diagnostics and monthly amounts agree with the expanded package's expected values.
- Independent aggregate-first SQL reconstruction using a different latest-revision query: every plan's financial totals, monthly invoices/GPU costs, capacities and feasibility agree within USD 0.01.
- Output-only verifier: reference 40/40, empty output 0/40.
- A memo with optional diagnostic numbers omitted, alternative recommendation phrasing and different heading levels also passes 40/40.
- Rubric: 66 criteria, 100 positive points, recommend 35, instruction following 10, maximum weight 12, no penalties, file targets declared.

Official Harbor 0.18.0 checks must use the clean extraction of the merged ZIP. The external HARBOR_RUN_RESULTS.md records the completed run results and exact archive hash, without requiring the tested ZIP to be rewritten after execution. Historical runs for the smaller datasets do not certify this merge.

## Provenance and limits

Generated fictional inputs are explicitly allowed according to the user's confirmation on 15 October 2026. Retain that provenance; these are not real business records. See LICENSE.

The larger dataset adds mapping/offer histories, but volume is not proof of difficulty. Replay analysis still aggregates six cells; the policy gives detailed calculation conventions; administrative document text does not add analytical depth. Platform quality review, rubric judging and model sweeps remain unperformed. No platform approval or difficulty-band claim is made.
