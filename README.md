# claude-code-learning

A small command-line greeting app used to practice writing and testing Python
scripts with pytest.

## What this project does

`manual_test.py` asks for a name and an age, then prints a greeting. If the
age isn't a valid positive whole number, it prints an error message instead.

## Running manual_test.py

```
python manual_test.py
```

You'll be prompted to enter a name and an age interactively.

## Running the tests

```
python -m pytest
```

This runs `test_manual_test.py`, which drives `manual_test.py` as a
subprocess with various name/age inputs and checks the output.
