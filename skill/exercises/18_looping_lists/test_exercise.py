"""Tests for Lesson 18: Looping Lists"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from exercise import print_roster, find_passing, pair_names_scores

def test_roster():
    assert print_roster(["Alice", "Bob"]) == "1. Alice\n2. Bob"

def test_roster_single():
    assert print_roster(["Solo"]) == "1. Solo"

def test_roster_three():
    result = print_roster(["A", "B", "C"])
    assert "1. A" in result and "3. C" in result

def test_passing_basic():
    assert find_passing(["A", "B", "C"], [80, 50, 70]) == ["A", "C"]

def test_passing_all():
    assert find_passing(["A", "B"], [90, 80]) == ["A", "B"]

def test_passing_none():
    assert find_passing(["A", "B"], [30, 40]) == []

def test_passing_boundary():
    """Exactly 60 should pass"""
    assert find_passing(["A"], [60]) == ["A"]

def test_pair():
    assert pair_names_scores(["A", "B"], [80, 50]) == ["A: 80", "B: 50"]

def test_pair_single():
    assert pair_names_scores(["X"], [99]) == ["X: 99"]
