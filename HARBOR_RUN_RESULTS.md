# Harbor run results

Harbor version: 0.18.0. Date: 15 October 2026.

| Job | Diagnostic reward | Checks passed | Exceptions |
|---|---:|---:|---:|
| aq-econ-submit-nop-20261015-220608 | 0.0 | 0/5 | 0 |
| aq-econ-submit-oracle-20261015-220608 | 1.0 | 5/5 | 0 |

Both commands exited successfully. Five verifier checks cover memo delivery and the four headings. The 35-item rubric evaluates substantive answer quality.

## Submission archive

Upload `Aq_Econ-release.zip` from the project root. It is identical to the tested `.local-checks/Aq_Econ-submit.zip`.

SHA-256:

```text
eca88dfab97704b4e93eff171654ea51d543688aaff7405127480ea55d52c60f
```

The archive contains 23 files: task.toml, instruction.md, rubrics.json, task_card.md, LICENSE, environment/Dockerfile, ten input files, three solution runtime files and four verifier files.

Repository guides, reports, READMEs, gold examples, unused expected-value files, Git metadata and local artifacts are excluded. The rubric and task card support grading; LICENSE records provenance and terms.

## Inspect and repeat

Viewer: http://127.0.0.1:8080. Select the `aq-econ-submit-*` jobs above.

```powershell
./RUN_HARBOR.ps1
```

The clean extraction is `.local-checks/harbor-task-submit`. Job logs are in `.local-checks/harbor-jobs/`; the manifest is `.local-checks/Aq_Econ-submit.manifest.json`.
