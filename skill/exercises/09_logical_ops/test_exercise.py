"""Tests for Lesson 9: Logical Operators — Bug Fix"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from exercise import can_ride

def test_both_pass():
    """130cm and age 10 should be allowed"""
    assert can_ride(130, 10) == True

def test_too_short():
    """110cm should be rejected even if old enough"""
    assert can_ride(110, 10) == False

def test_too_young():
    """Age 6 should be rejected even if tall enough"""
    assert can_ride(130, 6) == False

def test_both_fail():
    """Both too short and too young"""
    assert can_ride(100, 5) == False

def test_exact_boundary():
    """Exactly 120cm and age 8 should pass"""
    assert can_ride(120, 8) == True

def test_exact_height_young():
    """Exactly 120cm but too young"""
    assert can_ride(120, 7) == False

def test_tall_exact_age():
    """Tall but exactly age 8"""
    assert can_ride(150, 8) == True
