# Submission guide

## Task settings

- Title: Q4 AI Deployment Investment Decision.
- Domain: Technology / AI infrastructure economics.
- Primary objective: Opportunity Sizing & Decision Support.
- Additional objectives: Comparative Analysis & Explanation; Data Quality, Monitoring & Alerting.
- Reasoning phases: Explore / Discover, Hypothesize, Analyze & Validate, Synthesize, Recommend.
- Rubric: 35 criteria, 100 positive points.
- Distractor: `environment/data/product_research.pdf`.
- Licence: CC-BY-4.0 for the task material covered by LICENSE.

## Upload

1. Use the tested ZIP identified in HARBOR_RUN_RESULTS.md.
2. Verify its SHA-256 against the run report.
3. Upload the ZIP with `task.toml` at archive root. All input data is included.
4. Mark the distractor and import `rubrics.json` if required by the editor.
5. Enter actual preparation time and confirm the recorded nop/oracle runs.

## Release workflow

```powershell
python tools/build_package.py --name Aq_Econ-submit
./RUN_HARBOR.ps1 -TaskDirectory '.local-checks/harbor-task-submit' -JobPrefix 'aq-econ-submit'
```

Use a new version name for each subsequent release. Required results: nop 0.0, oracle 1.0, zero trial exceptions. Record the archive hash and run evidence, then upload those exact bytes.

The builder excludes Git metadata, local environments, logs, repository tooling and personal documentation.
