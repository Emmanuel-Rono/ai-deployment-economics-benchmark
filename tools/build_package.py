"""Build a client task ZIP, excluding Git metadata and personal tracking files."""
import argparse
import hashlib
import json
import re
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

ROOT = Path(__file__).resolve().parent.parent
TOP_LEVEL = [
    'task.toml', 'instruction.md', 'rubrics.json', 'task_card.md', 'LICENSE',
    'BUILD_REPORT.md', 'SUBMISSION_GUIDE.md', 'INSTRUCTION_COVERAGE.md',
]
TREES = ['environment', 'solution', 'tests']
SKIP_DIRS = {'.git', '.local-checks', '.venv', '__pycache__',
             '.pytest_cache', '.mypy_cache', '.ruff_cache'}
SKIP_FILES = {'.gitignore', '.gitattributes', '.DS_Store', 'Thumbs.db'}
ALLOWED = {
    '.py', '.r', '.sh', '.sql', '.ipynb', '.toml', '.cfg', '.ini', '.md',
    '.txt', '.json', '.jsonl', '.yaml', '.yml', '.xml', '.lock', '.diff',
    '.patch', '.csv', '.tsv', '.xlsx', '.xls', '.db', '.sqlite', '.sqlite3',
    '.parquet', '.pdf', '.png', '.jpg', '.jpeg', '.zip', '.gz', '.tgz',
}
NAMED = {'Dockerfile', 'Makefile', 'LICENSE', 'LICENCE', 'COPYING', 'NOTICE'}
ENV_ONLY = {'.log', '.mod', '.config', '.html', '.tab', '.ids', '.list', ''}


def validate(files):
    rubric = json.loads((ROOT / 'rubrics.json').read_text(encoding='utf-8'))
    if not 25 <= len(rubric) <= 100:
        raise ValueError('Rubric must contain 25-100 criteria.')
    if sorted(item['item'] for item in rubric) != list(range(1, len(rubric) + 1)):
        raise ValueError('Rubric item identifiers must be unique and sequential.')
    positive = sum(item['weight'] for item in rubric if item['weight'] > 0)
    recommend = [item for item in rubric if item['category'] == 'recommend' and item['weight'] > 0]
    following = sum(item['weight'] for item in rubric if item['category'] == 'instruction_following' and item['weight'] > 0)
    if positive != 100 or len(recommend) < 3 or sum(item['weight'] for item in recommend) < 30:
        raise ValueError('Check positive points and decision criterion count/share.')
    if not 1 <= following <= 10:
        raise ValueError('Instruction-following positive points must be 1-10.')
    for item in rubric:
        if not isinstance(item['weight'], int) or item['weight'] == 0 or abs(item['weight']) > 100:
            raise ValueError('Invalid rubric weight.')
        if item['weight'] > 20 or len(item['criterion']) > 250 or not item.get('grades_output_files'):
            raise ValueError('Check criterion weight, length and output file declarations.')
    if json.loads((ROOT / 'tests/test_weights.json').read_text(encoding='utf-8')) != []:
        raise ValueError('This project expects empty programmatic test weights.')
    required = ['solution/solve.sh', 'tests/test.sh', 'environment/Dockerfile']
    if any(not (ROOT / name).is_file() for name in required):
        raise ValueError('A required executable entry point or Dockerfile is missing.')
    if len([path for path in (ROOT / 'environment/data').rglob('*') if path.is_file()]) < 5:
        raise ValueError('At least five task input files are required.')
    for path in files:
        relative = path.relative_to(ROOT)
        if path.is_symlink():
            raise ValueError('Package source must contain regular files: ' + str(relative))
        if not path.is_file():
            raise ValueError('Missing package file: ' + str(relative))
        environment_only = relative.parts[0] == 'environment' and path.suffix.lower() in ENV_ONLY
        if path.suffix.lower() not in ALLOWED and path.name not in NAMED and not environment_only:
            raise ValueError('Unsupported task file type: ' + str(relative))
        if path.stat().st_size >= 1024**3:
            raise ValueError('Single-file size limit reached: ' + str(relative))
        with path.open('rb') as stream:
            if stream.read(128).startswith(b'version https://git-lfs.github.com/spec/v1'):
                raise ValueError('Git LFS data is not downloaded; run git lfs pull: ' + str(relative))
    if sum(path.stat().st_size for path in files) >= 4 * 1024**3 or len(files) > 150000:
        raise ValueError('Unpacked package exceeds archive limits.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--name', required=True, help='New version name, e.g. Aq_Econ-v2')
    parser.add_argument('--check-only', action='store_true', help='Validate and list files without creating anything')
    args = parser.parse_args()
    if not re.fullmatch(r'[A-Za-z0-9_-]+', args.name):
        parser.error('Use only letters, digits, underscores and hyphens for the version name.')
    label = args.name[len('Aq_Econ-'):] if args.name.startswith('Aq_Econ-') else args.name
    archive = ROOT / '.local-checks' / (args.name + '.zip')
    stage = ROOT / '.local-checks' / ('harbor-task-' + label)
    files = [ROOT / name for name in TOP_LEVEL]
    files += [path for tree in TREES for path in (ROOT / tree).rglob('*')
              if path.is_file() and not any(part in SKIP_DIRS for part in path.relative_to(ROOT).parts)
              and path.name not in SKIP_FILES and path.suffix != '.pyc']
    validate(files)
    if args.check_only:
        print(json.dumps({'files': sorted(path.relative_to(ROOT).as_posix() for path in files),
                          'file_count': len(files), 'unpacked_bytes': sum(path.stat().st_size for path in files)}, indent=2))
        return
    if archive.exists() or stage.exists():
        raise FileExistsError('Preserve existing archives/extractions; choose a new --name.')
    archive.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(archive, 'x', ZIP_DEFLATED) as bundle:
        for path in sorted(files):
            bundle.write(path, path.relative_to(ROOT).as_posix())
    if archive.stat().st_size >= 1024**3:
        raise ValueError('Compressed package exceeds the 1 GiB limit; do not upload.')
    with ZipFile(archive) as bundle:
        if bundle.testzip() is not None:
            raise ValueError('Archive integrity check failed.')
        bundle.extractall(stage)
    for path in files:
        extracted = stage / path.relative_to(ROOT)
        if hashlib.sha256(path.read_bytes()).digest() != hashlib.sha256(extracted.read_bytes()).digest():
            raise ValueError('Extracted file differs: ' + str(path.relative_to(ROOT)))
    manifest = {'archive': str(archive), 'sha256': hashlib.sha256(archive.read_bytes()).hexdigest(),
                'zip_bytes': archive.stat().st_size, 'file_count': len(files),
                'unpacked_bytes': sum(path.stat().st_size for path in files), 'extracted_task': str(stage)}
    (archive.parent / (args.name + '.manifest.json')).write_text(json.dumps(manifest, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(manifest, indent=2))
    print('Run nop and oracle against the extracted_task before uploading this ZIP.')


if __name__ == '__main__':
    main()
