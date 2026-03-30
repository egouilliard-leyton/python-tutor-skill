"""Tests for Lesson 8: Elif — Grade Calculator"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from exercise import get_grade

def test_grade_a():
    """95 is an A"""
    assert get_grade(95) == "A"

def test_grade_b():
    """83 is a B"""
    assert get_grade(83) == "B"

def test_grade_c():
    """71 is a C"""
    assert get_grade(71) == "C"

def test_grade_d():
    """65 is a D"""
    assert get_grade(65) == "D"

def test_grade_f():
    """45 is an F"""
    assert get_grade(45) == "F"

def test_boundary_90():
    """Exactly 90 is an A"""
    assert get_grade(90) == "A"

def test_boundary_80():
    """Exactly 80 is a B"""
    assert get_grade(80) == "B"

def test_boundary_70():
    """Exactly 70 is a C"""
    assert get_grade(70) == "C"

def test_boundary_60():
    """Exactly 60 is a D"""
    assert get_grade(60) == "D"

def test_perfect_score():
    """100 is an A"""
    assert get_grade(100) == "A"

def test_zero():
    """0 is an F"""
    assert get_grade(0) == "F"
