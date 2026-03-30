"""Tests for Lesson 5: User Input — Greeting Program
Note: input()-based exercises are harder to test automatically.
We check the source code for key patterns instead.
"""
import os

def read_source():
    with open(os.path.join(os.path.dirname(__file__), "exercise.py")) as f:
        return f.read()

def get_code_lines():
    """Get non-comment, non-empty lines"""
    src = read_source()
    lines = []
    for line in src.split("\n"):
        stripped = line.strip()
        if stripped and not stripped.startswith("#"):
            lines.append(stripped)
    return lines

def test_uses_input():
    """Should use input() to ask questions"""
    src = read_source()
    count = src.count("input(")
    assert count >= 2, f"Use input() at least twice (for name and birth year). Found {count} times."

def test_uses_int_conversion():
    """Should convert birth year to a number with int()"""
    src = read_source()
    assert "int(" in src, "You need int() to convert the birth year from text to a number"

def test_calculates_age():
    """Should calculate age using 2026"""
    src = read_source()
    assert "2026" in src, "Use 2026 as the current year to calculate age"

def test_uses_print():
    """Should print a greeting"""
    code_lines = get_code_lines()
    prints = [l for l in code_lines if "print(" in l]
    assert len(prints) >= 1, "Use print() to display the greeting"

def test_greeting_uses_variables():
    """Greeting should include the name and age variables"""
    src = read_source()
    has_fstring = "f'" in src or 'f"' in src
    has_concat = "+" in src and "name" in src
    has_comma = "print(" in src and "name" in src
    assert has_fstring or has_concat or has_comma, \
        "Your print should include the name and age — try using an f-string"

def test_has_enough_code():
    """Should have at least 4 meaningful lines of code"""
    code_lines = get_code_lines()
    assert len(code_lines) >= 4, \
        f"You need more code — at least input, convert, calculate, and print. Found {len(code_lines)} lines."
