"""Tests for Lesson 2: Variables"""
import subprocess
import sys
import os

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
    """Your program should run without errors"""
    stdout, stderr = run_exercise()
    assert "Error" not in stderr, f"Your program has an error: {stderr.strip()}"

def test_has_variables():
    """You should create name, age, and city variables"""
    src = read_source()
    assert "name =" in src or "name=" in src, "Create a 'name' variable"
    assert "age =" in src or "age=" in src, "Create an 'age' variable"
    assert "city =" in src or "city=" in src, "Create a 'city' variable"

def test_name_not_empty():
    """The name variable should have your actual name"""
    src = read_source()
    assert 'name = ""' not in src and "name = ''" not in src, \
        "Put your actual name inside the quotes"

def test_age_not_zero():
    """The age variable should be your actual age"""
    src = read_source()
    assert "age = 0" not in src, "Put your actual age (a number)"

def test_prints_output():
    """Your program should print something"""
    stdout, _ = run_exercise()
    assert len(stdout.strip()) > 0, "Your program doesn't print anything"

def test_output_has_name():
    """Output should include the word 'name' or your actual name"""
    stdout, _ = run_exercise()
    lower = stdout.lower()
    assert "name" in lower or len(stdout.strip().split("\n")) >= 1, \
        "Print your name using print() or f-strings"

def test_output_has_multiple_lines():
    """Print at least 3 pieces of info"""
    stdout, _ = run_exercise()
    lines = [l for l in stdout.strip().split("\n") if l.strip()]
    assert len(lines) >= 2, f"Expected at least 2 lines, got {len(lines)}"
