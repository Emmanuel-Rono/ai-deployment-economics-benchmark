# Current correction: exact memo-only prompt

instruction.md now contains the user's exact agreed text. There is no CSV deliverable, mandatory table, specified monetary precision or diagnostic checklist. The reference solver, gold deliverable, 35-item rubric, five file/heading checks and coverage map have been aligned. Use the memo-only archive and its own run evidence in HARBOR_RUN_RESULTS.md. The expanded input data and economic ground truth are unchanged.

The previous merge notes below are historical and describe the superseded CSV contract.

# Merged Aq_Econ review - 15 October 2026

## Current state

The working folder now combines AQ_Econ2's expanded inputs, solver, expected values and 66-criterion rubric with the less-leading prompt developed in this conversation. All ten data files match the source exactly. The source AQ_Econ2 directory was left unchanged. The previous working package and operator notes are preserved in `.local-checks/pre-merge-20261015-152152.zip`.

The current data has 500,000 versioned workload rows, 450,000 logical requests, 442,622 completed latest requests, 550,000 attempts and 5,000 accounts. It occupies 147.37 MiB. The current dictionary is a PDF; the obsolete Markdown dictionary was removed after backup.

## What was reconciled

- Retained the prompt's open analytical direction and precise file/schema contract.
- Removed AQ_Econ2's revived diagnostic checklist, October contribution requirement and headline-price hint from compulsory scoring.
- Preserved numerical ground truth for the expanded dataset: P3 contribution USD 2,921,547.55, ahead of P1 by USD 17,377.14 and P2 by USD 1,911.30.
- Used 66 rubric criteria totalling 100 positive points: 35 recommend, 10 instruction following; no penalties.
- Retained 40 output-only programmatic checks with expanded-data targets. Equivalent heading/recommendation wording is accepted.
- Updated the coverage map, build report, task card, submission guide, reference memo and component READMEs. Generated-data permission is recorded.
- Operator scripts now default to the merged clean extraction; previous archives and jobs remain historical evidence only.

## Verification

The request-by-request solver and an independent aggregate-first SQL calculation agree on financial totals, monthly invoices/GPU costs, capacity and feasibility. Recomputed diagnostics and monthly values agree with supplied expected targets. Direct reference verification passes 40/40; empty output passes 0/40. The exact merged ZIP and official Harbor results are recorded in HARBOR_RUN_RESULTS.md.

## Remaining review questions

Generated fictional data is explicitly allowed, but volume and difficulty acceptance remain unverified. There are only six replay cells; the attempt log mainly supplies a population distinction; the policy still contains detailed calculation recipes. Extra administrative paragraphs in PDFs do not establish deeper analytical difficulty. See DATA_COMPLEXITY_PLAN.md for the proposed next-stage design.

The handbook's statement that unweighted programmatic reward must be zero conflicts with its local oracle-1.0 instructions. The working verifier retains its diagnostic passed/total reward and empty test weights, consistent with the successful local Harbor protocol; platform rubric judging is a separate score. Resolve any platform-specific reward-policy finding through the actual project configuration rather than changing rewards to create difficulty.

No platform rubric judging, model difficulty sweep, external submission or task-quality approval has been performed.
