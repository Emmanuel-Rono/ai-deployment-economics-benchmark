# Exact agreed prompt: current Harbor results

instruction.md contains the user's exact memo-only prompt. Its sole deliverable is recommendation.md; CSV, table, fixed decimal precision, diagnostic counts and October contribution are not required. All rubric file targets refer only to recommendation.md. The 35-criterion rubric totals 100 positive points (recommend 35; instruction following 10).

## Harbor 0.18.0

| Job | Diagnostic reward | Checks passed | Exceptions |
|---|---:|---:|---:|
| aq-econ-memo-nop-20261015-155001 | 0.0 | 0/5 | 0 |
| aq-econ-memo-oracle-20261015-155001 | 1.0 | 5/5 | 0 |

Both commands exited successfully. The five checks validate delivery of the memo and its four headings; the substantive financial evidence, correct decision, citations, discrepancies, constraints and risks are judged by the rubric. Diagnostic reward 1.0 is not a platform rubric score.

## Current tested ZIP

`.local-checks/Aq_Econ-memo.zip`

SHA-256: `23f9b176a073ae5a9e79f6b6d16b1653db92a96a0f2e93299afe172056bfb2c5`

The 30 packaged files match the current working files byte for byte. The prompt in the ZIP matches instruction.md exactly. Tests ran against `.local-checks/harbor-task-memo`, a clean extraction; the archive was not rebuilt afterwards. Previous CSV-contract ZIPs are historical and do not contain the current prompt.

## Inspect and repeat

The viewer at http://127.0.0.1:8080 shows both `aq-econ-memo-*` jobs. Logs are under `.local-checks/harbor-jobs/`. Run `./RUN_HARBOR.ps1` to repeat the same memo-only extraction. If source files change, first prepare a new ZIP and clean extraction.

The expanded data and financial calculations are unchanged: 500,000 workload rows, 550,000 attempts, 5,000 accounts; P3 Q4 contribution USD 2,921,547.55. The memo may include a table and extra diagnostics as supporting evidence, but those forms are optional. No platform rubric judging or model difficulty sweep has been performed.
