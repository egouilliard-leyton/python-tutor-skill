"""Tests for Lesson 11: While Loops — Countdown"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from exercise import countdown

def test_countdown_3():
    """countdown(3) should give [3, 2, 1, 'Go!']"""
    assert countdown(3) == [3, 2, 1, "Go!"]

def test_countdown_5():
    """countdown(5) should give [5, 4, 3, 2, 1, 'Go!']"""
    assert countdown(5) == [5, 4, 3, 2, 1, "Go!"]

def test_countdown_1():
    """countdown(1) should give [1, 'Go!']"""
    assert countdown(1) == [1, "Go!"]

def test_ends_with_go():
    """Last element should be 'Go!'"""
    result = countdown(3)
    assert result[-1] == "Go!", f"Last element should be 'Go!', got: {result[-1]}"

def test_returns_list():
    """Should return a list"""
    result = countdown(3)
    assert isinstance(result, list), "Return a list, not something else"

def test_correct_length():
    """countdown(n) should have n+1 elements (numbers + Go!)"""
    result = countdown(4)
    assert len(result) == 5, f"countdown(4) should have 5 elements, got {len(result)}"
