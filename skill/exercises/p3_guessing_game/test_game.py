"""Tests for Project 3: Number Guessing Game"""
import os

def read_source():
    with open(os.path.join(os.path.dirname(__file__), "game.py")) as f:
        return f.read()

def get_active_lines():
    return [l for l in read_source().split("\n")
            if l.strip() and not l.strip().startswith("#")]

def test_imports_random():
    """Should import the random module"""
    src = read_source()
    active = [l for l in src.split("\n") if not l.strip().startswith("#")]
    assert any("import random" in l for l in active), \
        "Add 'import random' at the top"

def test_generates_random_number():
    """Should generate a random number with randint"""
    src = read_source()
    active = "\n".join(l for l in src.split("\n") if not l.strip().startswith("#"))
    assert "randint" in active, "Use random.randint() to pick a number"

def test_gets_user_input():
    """Should ask the user for guesses"""
    src = read_source()
    active = [l for l in src.split("\n")
              if "input(" in l and not l.strip().startswith("#")]
    assert len(active) >= 1, "Use input() to get the player's guess"

def test_converts_to_int():
    """Should convert input to a number"""
    src = read_source()
    active = "\n".join(l for l in src.split("\n") if not l.strip().startswith("#"))
    assert "int(" in active, "Convert the guess to a number with int()"

def test_has_comparison():
    """Should compare guess to answer (higher/lower)"""
    src = read_source()
    active = "\n".join(l for l in src.split("\n") if not l.strip().startswith("#"))
    has_compare = (">" in active or "<" in active or
                   "high" in active.lower() or "low" in active.lower())
    assert has_compare, "Compare the guess: tell the player if it's too high or too low"

def test_has_while_loop():
    """Should use a while loop for repeated guessing"""
    src = read_source()
    active = [l for l in src.split("\n") if not l.strip().startswith("#")]
    has_while = any("while" in l for l in active)
    assert has_while, "Use a while loop to let the player keep guessing"

def test_has_guess_counter():
    """Should count how many guesses it took"""
    src = read_source()
    active = "\n".join(l for l in src.split("\n") if not l.strip().startswith("#"))
    has_counter = ("+= 1" in active or "+ 1" in active or
                   "count" in active.lower() or "guesses" in active.lower() or
                   "attempts" in active.lower())
    assert has_counter, "Add a counter to track how many guesses the player makes"

def test_no_debug_print():
    """Should not have the DEBUG print showing the answer"""
    src = read_source()
    active = [l for l in src.split("\n") if not l.strip().startswith("#")]
    for line in active:
        assert "debug" not in line.lower(), \
            "Remove the DEBUG print that shows the answer — no cheating!"

def test_enough_code():
    """Should be a substantial program"""
    lines = get_active_lines()
    assert len(lines) >= 15, f"Your game needs more code! Found {len(lines)} lines."
