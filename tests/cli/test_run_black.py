import os

import pytest


def test_run_black():
    os.system("python src/pythoncritic/cli/cli.py black tests/sample/duplicate_code_sample.py")