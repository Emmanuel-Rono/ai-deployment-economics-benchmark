"""Memo contract diagnostics; substantive answer quality is rubric-judged."""
import os
import unittest
from pathlib import Path

OUTPUT = Path(os.environ.get('OUTPUT_DIR', '/workspace/output'))


def memo():
    return (OUTPUT / 'recommendation.md').read_text(encoding='utf-8')


class OutputChecks(unittest.TestCase):
    def test_memo_delivered(self):
        self.assertTrue(memo().strip(), 'recommendation.md is empty')


def heading_check(heading):
    def check(self):
        pattern = rf'(?im)(?:^#{{1,6}}[ \t]+{heading}[ \t]*#*[ \t]*$|^{heading}[ \t]*\r?\n[=-]+[ \t]*$)'
        self.assertRegex(memo(), pattern)
    return check


for heading in ['Recommendation', 'Evidence', 'Alternatives', 'Risks']:
    setattr(OutputChecks, 'test_heading_' + heading.lower(), heading_check(heading))
