"""Tests for Lesson 4: Numbers — Tip Calculator"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from exercise import calculate_tip

def test_fifteen_percent():
    """15% tip on 50.00"""
    assert calculate_tip(50.00, 15) == 57.5

def test_twenty_percent():
    """20% tip on 100.00"""
    assert calculate_tip(100.00, 20) == 120.0

def test_rounding():
    """Should round to 2 decimal places"""
    assert calculate_tip(33.50, 18) == 39.53

def test_zero_tip():
    """0% tip should return the original bill"""
    assert calculate_tip(50.00, 0) == 50.0

def test_large_tip():
    """Should handle generous tips"""
    assert calculate_tip(80.00, 25) == 100.0

def test_returns_number():
    """Should return a number, not a string"""
    result = calculate_tip(50.00, 15)
    assert isinstance(result, (int, float)), "Return a number, not a string"
