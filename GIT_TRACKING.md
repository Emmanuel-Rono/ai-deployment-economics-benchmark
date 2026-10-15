# Personal GitHub tracking and client submission

Git tracks the editable project, including your repository notes and operator scripts. The client receives the task ZIP. The packaging tool uses an explicit list of task files, so `.gitignore`, `.gitattributes`, `.git/`, this guide, README.md and tools/ are excluded from that ZIP.

## First push

There is currently no Git repository in this working folder. These files prepare the folder; no repository, commit, remote or push was created by this setup.

Create an empty repository on GitHub. Keep its README, licence and gitignore initialization options off because this folder already supplies those files. A private repository is a useful default for your working benchmark and reference solution; choose the visibility you want for your brand.

Run in PowerShell from this project folder:

```powershell
git init -b main
git lfs install --local
git add .
git status --short
git lfs ls-files
git commit -m "Track expanded Aq_Econ benchmark with agreed memo prompt"
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
git push -u origin main
```

Replace the example username and repository with yours. Git will use your configured author identity. Git LFS is installed on this machine; `.gitattributes` places the workload SQLite database and attempt-event JSONL under LFS. Install LFS before staging those files. The data remains versioned; Git stores pointers and LFS stores the actual large content.

Review the staged file list before committing. `.local-checks`, Python environments/caches, output folders, root ZIPs and local credentials should be absent. The input data, solution, gold memo, expected values and rubric should be present.

For later changes:

```powershell
git add .
git diff --cached --stat
git commit -m "Describe the change made to the task"
git push
```

Use a descriptive commit for each meaningful dataset, prompt, solver or scoring change. Optionally tag a tested submission:

```powershell
git tag -a submission-v1 -m "Tested memo-only task submission"
git push origin submission-v1
```

Use a new tag name for each release. The archive SHA-256 identifies the submitted bytes; the Git commit/tag identifies the editable source.

## Restore the project on another machine

```powershell
git lfs install
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
git lfs pull
uv venv --python 3.13 .local-checks/venv
uv pip install --python .local-checks/venv/Scripts/python.exe "harbor==0.18.0" "pypdf==6.1.1"
```

Python, uv, Git/Git LFS and a running Docker engine are prerequisites. `.local-checks` is intentionally not restored from Git. LFS inputs must be downloaded before building the Docker image or client ZIP; the packaging tool rejects LFS pointers in place of data.

## Submit the current tested version

The current upload file is **`.local-checks/Aq_Econ-memo.zip`**. It already passed official nop and oracle checks. Do not use an older `merged` or `revised` ZIP and do not ZIP the entire workspace.

Check its fingerprint:

```powershell
Get-FileHash -LiteralPath .local-checks/Aq_Econ-memo.zip -Algorithm SHA256
```

Expected SHA-256:

```text
23f9b176a073ae5a9e79f6b6d16b1653db92a96a0f2e93299afe172056bfb2c5
```

Upload that exact ZIP in the client's package-upload field. No separate data upload is needed. Mark `environment/data/product_research.pdf` as the only distractor. Import the packaged 35-item rubric if the editor does not populate automatically. Declare the actual CC-BY-4.0 provenance, enter real preparation time, and confirm the local runs for this exact archive. Full evidence is in HARBOR_RUN_RESULTS.md. Submission starts the client's own checks; local success is not platform approval.

## Build and test a future version

After changing task files, prepare a newly named archive rather than modifying a previously tested ZIP:

```powershell
python tools/build_package.py --name Aq_Econ-v2
./RUN_HARBOR.ps1 -TaskDirectory '.local-checks/harbor-task-v2' -JobPrefix 'aq-econ-v2'
```

The builder lists the output ZIP, extraction directory and SHA-256. It refuses to overwrite an existing archive or extraction. Inspect the job results: nop must have reward 0.0, oracle 1.0, and neither trial should contain an exception. The command exit alone is not the result. Record the new hash and run evidence in a tracked report, then commit/tag that source version and upload those same ZIP bytes.

The builder is deliberately independent of Git ignore rules. Ignoring a file in Git does not exclude it from arbitrary ZIP commands; using the explicit packaging tool is what excludes repository metadata and personal tracking files from client uploads.
