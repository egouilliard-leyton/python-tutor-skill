"""Tests for Lesson 3: Strings — Username Generator"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from exercise import make_username

def test_basic():
    """Works with normal names"""
    assert make_username("Charles", "Gouilliard") == "cgouilliard"

def test_another_name():
    """Works with different names"""
    assert make_username("Ada", "Lovelace") == "alovelace"

def test_uppercase_input():
    """Handles ALL CAPS input"""
    assert make_username("JEAN", "DUPONT") == "jdupont"

def test_mixed_case():
    """Handles MiXeD case input"""
    assert make_username("Marie", "Curie") == "mcurie"

def test_returns_string():
    """Should return a string, not print it"""
    result = make_username("Test", "User")
    assert isinstance(result, str), "Your function should use 'return', not 'print'"

def test_single_letter_first():
    """Works when first name is just one letter"""
    assert make_username("J", "Smith") == "jsmith"
