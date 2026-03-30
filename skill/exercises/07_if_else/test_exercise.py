"""Tests for Lesson 7: If/Else — Can You Vote?"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from exercise import can_vote

def test_adult():
    """20-year-old can vote"""
    result = can_vote(20)
    assert "can vote" in result.lower(), f"A 20-year-old should be able to vote, got: {result}"

def test_exactly_18():
    """18-year-old can vote (edge case)"""
    result = can_vote(18)
    assert "can vote" in result.lower(), f"An 18-year-old should be able to vote, got: {result}"

def test_under_18():
    """15-year-old cannot vote"""
    result = can_vote(15)
    assert "not yet" in result.lower() or "can't" in result.lower() or "cannot" in result.lower(), \
        f"A 15-year-old should NOT be able to vote, got: {result}"

def test_years_remaining():
    """Should show correct years remaining"""
    result = can_vote(15)
    assert "3" in result, f"A 15-year-old needs 3 more years, got: {result}"

def test_years_remaining_young():
    """Should calculate years for younger ages too"""
    result = can_vote(7)
    assert "11" in result, f"A 7-year-old needs 11 more years, got: {result}"

def test_exactly_17():
    """17-year-old needs 1 more year"""
    result = can_vote(17)
    assert "1" in result, f"A 17-year-old needs 1 more year, got: {result}"
    assert "not yet" in result.lower() or "can't" in result.lower(), \
        f"17 is still too young, got: {result}"

def test_returns_string():
    """Should return a string"""
    result = can_vote(20)
    assert isinstance(result, str), "Use 'return', not 'print'"
