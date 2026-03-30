"""Tests for Lesson 6: Booleans — Predict the Output"""
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
    predictions = src.count("prediction: True") + src.count("prediction: False") + \
                  src.count("prediction: true") + src.count("prediction: false")
    assert predictions >= 5, \
        f"Write your predictions next to 'My prediction:' (found {predictions}, need at least 5)"

def test_added_own_comparisons():
    """Write 2 of your own comparisons in the YOUR TURN section"""
    src = read_source()
    your_turn_section = src.split("YOUR TURN")[1] if "YOUR TURN" in src else ""
    prints = your_turn_section.count("print(")
    assert prints >= 1, "Add at least one comparison of your own in the YOUR TURN section"

def test_output_has_all_eight():
    """All 8 original comparisons should run"""
    stdout, _ = run_exercise()
    for i in range(1, 9):
        assert f"{i}:" in stdout, f"Comparison {i} is missing from output"
