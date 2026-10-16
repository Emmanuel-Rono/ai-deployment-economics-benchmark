# Verifier

`test.sh` executes five offline checks: a nonempty `recommendation.md` and the four required headings. ATX and Setext headings are supported.

Results are written to `/logs/verifier/ctrf.json` and `/logs/verifier/reward.json`. The diagnostic reward is passed checks divided by total checks. `test_weights.json` is an empty array.

The 35-item rubric evaluates decision correctness, financial evidence, citations, reconciliation, constraints, risks and presentation.
