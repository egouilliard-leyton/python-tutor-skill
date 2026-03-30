"""Tests for Lesson 24: Scope — Predict the Output"""
import subprocess, sys, os

def run_exercise():
    result = subprocess.run(
        [sys.executable, "exercise.py"],
        capture_output=True, text=True, timeout=5,
        cwd=os.path.dirname(__file__)
    )
    return result.stdout, result.stderr

def read_source():
    with open(os.path.join(os.path.dirname(__file__), "exercise.py")) as f:
        return f.read()

def test_runs_without_error():
    """Program should run without errors"""
    _, stderr = run_exercise()
    assert "Error" not in stderr, f"Error: {stderr.strip()}"

def test_has_predictions():
    """You should write your predictions as comments"""
    src = read_source()
    # Count meaningful predictions (not the blank ___)
    blanks = src.count("prediction: ___")
    filled = src.count("prediction:") - blanks
    assert filled >= 7, \
        f"Write your predictions next to 'My prediction:' (found {filled}, need at least 7)"

def test_added_own_examples():
    """Write 2 scope examples of your own in the YOUR TURN section"""
    src = read_source()
    your_turn_section = src.split("YOUR TURN")[1] if "YOUR TURN" in src else ""
    has_def = "def " in your_turn_section
    has_print = "print(" in your_turn_section
    assert has_def and has_print, \
        "Add at least one function with a print in the YOUR TURN section"

def test_output_has_all_seven():
    """All 7 original examples should run"""
    stdout, _ = run_exercise()
    for i in range(1, 8):
        found = f"{i}:" in stdout or f"{i}a:" in stdout
        assert found, f"Example {i} is missing from output"
