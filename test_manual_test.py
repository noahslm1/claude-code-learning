import subprocess
import sys

import pytest


@pytest.mark.parametrize(
    "name, age, expected",
    [
        ("Jollo", "30", "Hello Jollo, you are 30 years old. Welcome to Claude Code!"),
        ("Jollo", "0", "Sorry Jollo, '0' is not a valid age."),
        ("Jollo", "-5", "Sorry Jollo, '-5' is not a valid age."),
        ("Jollo", "25.5", "Sorry Jollo, '25.5' is not a valid age."),
        ("Jollo", "abc", "Sorry Jollo, 'abc' is not a valid age."),
        ("Jollo", "", "Sorry Jollo, '' is not a valid age."),
    ],
)
def test_manual_test_output(name, age, expected):
    result = subprocess.run(
        [sys.executable, "manual_test.py"],
        input=f"{name}\n{age}\n",
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert expected in result.stdout
