# Git and release workflow

## Initial push

Create an empty GitHub repository, then run:

```powershell
git init -b main
git lfs install --local
git add .
git status --short
git lfs ls-files
git commit -m "Add deployment economics benchmark"
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
git push -u origin main
```

Replace the repository URL. For an existing local repository, use the update commands below. `.gitattributes` tracks the workload SQLite database and attempt-event JSONL through Git LFS. `.gitignore` excludes environments, caches, logs, backups and ZIPs.

## Updates

```powershell
git add .
git diff --cached --stat
git commit -m "Describe the update"
git push
```

## Restore and install

```powershell
git lfs install
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
git lfs pull
uv venv --python 3.13 .local-checks/venv
uv pip install --python .local-checks/venv/Scripts/python.exe "harbor==0.18.0" "pypdf==6.1.1"
```

Start Docker before running Harbor.

## Build and validate

```powershell
python tools/build_package.py --name Aq_Econ-submit
./RUN_HARBOR.ps1 -TaskDirectory '.local-checks/harbor-task-submit' -JobPrefix 'aq-econ-submit'
```

The builder creates the ZIP, clean extraction and SHA-256 manifest under `.local-checks/`. Use a new version name for each release. Required run results: nop 0.0, oracle 1.0, zero exceptions.

Inspect the jobs:

```powershell
& ./.local-checks/venv/Scripts/harbor.exe view ./.local-checks/harbor-jobs --jobs --host 127.0.0.1 --port 8080
```

Open http://127.0.0.1:8080. Record the archive hash and job results in HARBOR_RUN_RESULTS.md, then upload the tested ZIP. The task file list excludes Git metadata, README.md, this guide, tools/ and local run artifacts.

## Tag a release

```powershell
git tag -a submission-v1 -m "Validated task release"
git push origin submission-v1
```

Use a unique tag for each submitted version. Submission settings are in SUBMISSION_GUIDE.md.

The client ZIP contains only task.toml, instruction.md, rubrics.json, task_card.md, LICENSE, the Docker environment and data, the reference-solution runtime, and the verifier runtime. Repository guides, reports, READMEs, gold examples, expected-value audit files and local artifacts stay outside the ZIP.
