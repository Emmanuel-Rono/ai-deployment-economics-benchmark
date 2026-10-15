# Submission settings

Working title: Q4 AI Deployment Investment Decision

Domain: select the closest available Technology / AI infrastructure or Business / Finance domain. Do not select Biomedical & Clinical Research.

Primary objective: Opportunity Sizing & Decision Support.
Additional objectives: Comparative Analysis & Explanation; Data Quality, Monitoring & Alerting.
Reasoning phases: all five (Explore / Discover, Hypothesize, Analyze & Validate, Synthesize, Recommend).

Upload this task's ZIP with task.toml at the archive root. No separate task-data upload is needed. Import rubrics.json if the platform does not seed its editor automatically. Positive points total 100, of which recommend is 35 and instruction_following is 10. The rubric has 35 criteria. test_weights.json is empty because programmatic checks are determinism gates rather than weighted platform reward.

Mark environment/data/product_research.pdf as the only distractor. There are ten packaged data files, so the distractor fraction is 10%. Do not mark the commercial or planning PDFs as distractors.

Licence declaration: CC-BY-4.0 for newly authored task material, subject to submitter authority and the provenance note in LICENSE. Do not declare MIT for these data merely because it appears in a form default. Do not represent generated scenario records as real operational records. The user confirmed on 15 October 2026 that generated fictional data is explicitly permitted for this project.

Preparation time: enter the actual author's wall-clock time, including subsequent verification, rather than a fabricated estimate.

## Local checks and exact upload archive

Use the merged archive and run evidence named in HARBOR_RUN_RESULTS.md. Older archives under .local-checks contain smaller datasets and should not be substituted. The two local checks must show nop 0.0 and oracle 1.0 against a clean extraction of the upload ZIP. Platform rubric judging and model sweeps are separate.

To repeat checks after preparing a clean merged extraction:

```powershell
./RUN_HARBOR.ps1 -TaskDirectory '.local-checks\harbor-task-memo' -JobPrefix 'aq-econ-memo'
```

Inspect http://127.0.0.1:8080 while Harbor Viewer is running, or use `harbor view .local-checks/harbor-jobs`. If package files change, create a new ZIP, rerun validations and record its SHA-256. Do not include .local-checks, virtual environments, caches, job logs or operator scripts in the submission ZIP.

## Reviewer files

solution/gold contains the example deliverables, solution/solve.py reconstructs them from inputs, and tests/expected.json stores output-only numerical targets. These are intentionally outside environment, so the agent cannot read them. See BUILD_REPORT.md for performed checks and material limitations.

The current exact prompt requires only recommendation.md. Use the memo-only archive and its own Harbor evidence from HARBOR_RUN_RESULTS.md; the earlier merged ZIP has the superseded CSV contract.
