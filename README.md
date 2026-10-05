# Python Week 6 – Safe Tools

- `safe_tools.py` – three functions (`safe_divide`, `safe_number`, `get_field`) that use try/except so they never crash.
- `unbreakable.py` – a program that keeps asking for input until it gets a valid whole number, and handles divide-by-zero.

## Why can the `if` check not catch `abc` on its own?

An `if` check can only test conditions you thought of in advance, such as `b == 0`, and there is no simple condition that says "this text can be converted by `int()`". The only reliable way to find out is to try the conversion and catch the `ValueError` with `try`/`except`.
