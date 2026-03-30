"""Tests for Bonus: Pyramid Builder"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from loops_pyramid import build_pyramid

def test_pyramid_one():
    assert build_pyramid(1) == ["*"]

def test_pyramid_two():
    assert build_pyramid(2) == [" * ", "***"]

def test_pyramid_three():
    assert build_pyramid(3) == ["  *  ", " *** ", "*****"]

def test_pyramid_returns_list():
    result = build_pyramid(3)
    assert isinstance(result, list), "build_pyramid should return a list"

def test_pyramid_correct_row_count():
    assert len(build_pyramid(5)) == 5

def test_pyramid_all_same_width():
    result = build_pyramid(4)
    widths = [len(row) for row in result]
    assert len(set(widths)) == 1, f"All rows should be the same width, got {widths}"

def test_pyramid_last_row_all_stars():
    result = build_pyramid(4)
    assert result[-1] == "*******"
