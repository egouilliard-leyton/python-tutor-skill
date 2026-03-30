"""Tests for Lesson 14: Nested Loops — Multiplication Table"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from exercise import times_table

def test_returns_list():
    """Should return a list"""
    assert isinstance(times_table(3), list)

def test_correct_row_count():
    """times_table(3) should have 3 rows"""
    assert len(times_table(3)) == 3

def test_first_row():
    """First row should contain 1x1, 1x2, 1x3"""
    result = times_table(3)
    row = result[0]
    assert "1 x 1 = 1" in row
    assert "1 x 3 = 3" in row

def test_last_row():
    """Last row of times_table(3) should contain 3x3=9"""
    result = times_table(3)
    assert "3 x 3 = 9" in result[2]

def test_multiplication_correct():
    """Check that actual math is correct"""
    result = times_table(4)
    assert "4 x 4 = 16" in result[3]
    assert "3 x 4 = 12" in result[2]

def test_single():
    """times_table(1) should have 1 row"""
    result = times_table(1)
    assert len(result) == 1
    assert "1 x 1 = 1" in result[0]
