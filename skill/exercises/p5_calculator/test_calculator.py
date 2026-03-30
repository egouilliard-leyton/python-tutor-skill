"""Tests for Project 5: Calculator"""
import os

def read_source():
    with open(os.path.join(os.path.dirname(__file__), "calculator.py")) as f:
        return f.read()

def get_active_lines():
    return [l for l in read_source().split("\n")
            if l.strip() and not l.strip().startswith("#")]

def test_has_math_functions():
    """Should define functions for math operations"""
    src = read_source()
    active = "\n".join(l for l in src.split("\n") if not l.strip().startswith("#"))
    defs = [l for l in active.split("\n") if l.strip().startswith("def ")]
    assert len(defs) >= 3, \
        f"Write at least 3 math functions (add, subtract, multiply, etc.) — found {len(defs)}"

def test_functions_have_return():
    """Math functions should return results, not just print"""
    src = read_source()
    active = "\n".join(l for l in src.split("\n") if not l.strip().startswith("#"))
    assert "return" in active, \
        "Your math functions should use 'return' to send back the result"

def test_uses_while_loop():
    """Should use a while loop for the menu"""
    src = read_source()
    active = [l for l in src.split("\n") if not l.strip().startswith("#")]
    has_while = any("while" in l for l in active)
    assert has_while, "Use a while loop to keep showing the menu"

def test_uses_input():
    """Should get user input for choices and numbers"""
    src = read_source()
    active = [l for l in src.split("\n")
              if "input(" in l and not l.strip().startswith("#")]
    assert len(active) >= 2, \
        "Use input() to get the menu choice AND the numbers"

def test_converts_to_number():
    """Should convert input to a number type"""
    src = read_source()
    active = "\n".join(l for l in src.split("\n") if not l.strip().startswith("#"))
    assert "float(" in active or "int(" in active, \
        "Convert user input to a number with float() or int()"

def test_handles_division_by_zero():
    """Should handle division by zero"""
    src = read_source()
    active = "\n".join(l for l in src.split("\n") if not l.strip().startswith("#"))
    has_check = ("== 0" in active or "!= 0" in active or
                 "zero" in active.lower() or "ZeroDivision" in active)
    assert has_check, "Handle what happens when someone tries to divide by zero"

def test_enough_code():
    """Should be a substantial program"""
    lines = get_active_lines()
    assert len(lines) >= 20, f"Your calculator needs more code! Found {len(lines)} lines."
