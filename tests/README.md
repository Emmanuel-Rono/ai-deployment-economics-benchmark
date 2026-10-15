# Memo verifier

`test.sh` runs five output-only diagnostics: recommendation.md is present and nonempty, and the four requested headings exist. ATX and Setext Markdown headings are accepted. No CSV, table, compulsory diagnostic numbers, fixed recommendation wording or monetary precision is required.

The substantive recommendation, financial evidence, citations, reconciliation, constraints and risks are judged by the 35-item rubric, not inferred from passing these file checks. Empty output passes zero checks. The standard offline runner writes CTRF diagnostics and a passed/total reward; test_weights.json remains empty. See the build report for the boundary between local diagnostics and platform rubric scoring.
