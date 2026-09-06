---
paths:
  - "**/test_*.py"
---

# Python Testing Rules

- Use pytest for automated tests.
- Prefer pytest.mark.parametrize when testing the same behavior with multiple inputs.
- Use sys.executable when tests launch Python subprocesses.
- Verify subprocess return codes as well as expected output.
- Do not weaken an existing test just to make it pass.
