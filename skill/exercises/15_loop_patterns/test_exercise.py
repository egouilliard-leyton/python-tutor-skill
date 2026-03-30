"""Tests for Lesson 15: Loop Patterns — Data Analyzer"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from exercise import find_total, find_max, count_above

# --- find_total tests ---
def test_total_basic():
    """Sum of [1,2,3,4,5] is 15"""
    assert find_total([1, 2, 3, 4, 5]) == 15

def test_total_single():
    """Sum of one number is that number"""
    assert find_total([42]) == 42

def test_total_negatives():
    """Works with negative numbers"""
    assert find_total([-1, 1, -2, 2]) == 0

# --- find_max tests ---
def test_max_basic():
    """Max of [3,7,2,9,1] is 9"""
    assert find_max([3, 7, 2, 9, 1]) == 9

def test_max_first():
    """Max is the first element"""
    assert find_max([10, 5, 3]) == 10

def test_max_last():
    """Max is the last element"""
    assert find_max([1, 2, 3]) == 3

def test_max_negative():
    """Works with all negative numbers"""
    assert find_max([-5, -1, -8]) == -1

# --- count_above tests ---
def test_count_basic():
    """2 numbers above 3 in [1,5,3,8,2]"""
    assert count_above([1, 5, 3, 8, 2], 3) == 2

def test_count_none():
    """Nothing above 100"""
    assert count_above([1, 2, 3], 100) == 0

def test_count_all():
    """Everything above 0"""
    assert count_above([5, 10, 15], 0) == 3

def test_count_exact():
    """Threshold value itself is NOT counted (strictly above)"""
    assert count_above([3, 3, 3], 3) == 0
