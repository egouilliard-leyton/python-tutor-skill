"""Tests for Bonus: List Statistics"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from lists_stats import median, mode, range_of

def test_median_odd():
    assert median([3, 1, 2]) == 2

def test_median_even():
    assert median([1, 2, 3, 4]) == 2.5

def test_median_single():
    assert median([5]) == 5

def test_median_already_sorted():
    assert median([1, 2, 3, 4, 5]) == 3

def test_median_unsorted():
    assert median([9, 1, 5, 3, 7]) == 5

def test_mode_basic():
    assert mode([1, 2, 2, 3]) == 2

def test_mode_clear_winner():
    assert mode([1, 2, 2, 3, 3, 3]) == 3

def test_mode_single():
    assert mode([7]) == 7

def test_mode_all_same():
    assert mode([4, 4, 4]) == 4

def test_range_basic():
    assert range_of([10, 3, 7]) == 7

def test_range_negative():
    assert range_of([-5, 5]) == 10

def test_range_single():
    assert range_of([3]) == 0

def test_range_all_same():
    assert range_of([2, 2, 2]) == 0
