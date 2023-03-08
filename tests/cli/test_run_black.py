import os

import pytest


def test_run_black():
    file_path = "tests/sample/black_code_impossible_to_reformat_sample.py"
    os.system(f"python src/pythoncritic/cli/cli.py black {file_path}")
