"""Tests for Lesson 16: Lists Basics"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from exercise import create_shopping_list, get_first_item, get_last_item, how_many

def test_create_list():
    """Should create a list with 3 items"""
    result = create_shopping_list("milk", "bread", "eggs")
    assert result == ["milk", "bread", "eggs"]

def test_create_returns_list():
    """Should return a list type"""
    result = create_shopping_list("a", "b", "c")
    assert isinstance(result, list), "Return a list using square brackets []"

def test_first_item():
    """Should return the first item"""
    assert get_first_item(["milk", "bread", "eggs"]) == "milk"

def test_first_item_different():
    """Works with different lists"""
    assert get_first_item(["apple", "banana"]) == "apple"

def test_last_item():
    """Should return the last item"""
    assert get_last_item(["milk", "bread", "eggs"]) == "eggs"

def test_last_item_single():
    """Works with a single-item list"""
    assert get_last_item(["only"]) == "only"

def test_how_many():
    """Should count items correctly"""
    assert how_many(["milk", "bread", "eggs"]) == 3

def test_how_many_empty():
    """Empty list has 0 items"""
    assert how_many([]) == 0

def test_how_many_one():
    """Single item list"""
    assert how_many(["just one"]) == 1
