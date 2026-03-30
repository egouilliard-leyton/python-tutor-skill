"""Tests for Lesson 1: Hello World"""
import subprocess
import sys

def run_exercise():
    result = subprocess.run(
        [sys.executable, "exercise.py"],
        capture_output=True, text=True, timeout=5,
        cwd=__import__("os").path.dirname(__file__)
    )
    return result.stdout, result.stderr

def test_runs_without_error():
    """Your program should run without errors"""
    stdout, stderr = run_exercise()
    assert "Error" not in stderr, f"Your program has an error: {stderr.strip()}"

def test_hello_world():
    """First line should print 'Hello, World!'"""
    stdout, _ = run_exercise()
    lines = stdout.strip().split("\n")
    assert len(lines) >= 1, "Your program doesn't print anything yet"
    assert "hello" in lines[0].lower() and "world" in lines[0].lower(), \
        "First line should say 'Hello, World!'"

def test_has_name():
    """Second line should include your name"""
    stdout, _ = run_exercise()
    lines = stdout.strip().split("\n")
    assert len(lines) >= 2, "You need at least 2 print statements"
    assert "name" in lines[1].lower() or len(lines[1].strip()) > 5, \
        "Second line should introduce your name"

def test_learning_python():
    """Third line should mention learning Python"""
    stdout, _ = run_exercise()
    lines = stdout.strip().split("\n")
    assert len(lines) >= 3, "You need 3 print statements"
    assert "python" in lines[2].lower(), \
        "Third line should mention Python"

def test_three_lines():
    """Should have at least 3 lines of output"""
    stdout, _ = run_exercise()
    lines = [l for l in stdout.strip().split("\n") if l.strip()]
    assert len(lines) >= 3, f"Expected 3 lines, got {len(lines)}"
