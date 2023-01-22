import os

import pytest


def test_run_flake8():
    os.system("python src/pythoncritic/cli/cli.py flake8 test/sample/duplicate_code_sample.py")

    assert os.path.exists("tmp/flake8_output.txt") == True
