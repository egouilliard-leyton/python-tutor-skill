"""Tests for Lesson 19: Dictionaries — Phone Book"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from exercise import create_contact, get_phone, add_contact, list_names

def test_create():
    result = create_contact("Alice", "555-1234")
    assert result == {"name": "Alice", "phone": "555-1234"}

def test_create_returns_dict():
    assert isinstance(create_contact("A", "1"), dict)

def test_get_exists():
    assert get_phone({"Alice": "555-1234"}, "Alice") == "555-1234"

def test_get_not_found():
    result = get_phone({"Alice": "555-1234"}, "Bob")
    assert result == "Not found", f"Should return 'Not found' for missing name, got: {result}"

def test_add():
    book = {"Alice": "555-1234"}
    result = add_contact(book, "Bob", "555-5678")
    assert "Bob" in result and result["Bob"] == "555-5678"

def test_add_keeps_existing():
    book = {"Alice": "555-1234"}
    result = add_contact(book, "Bob", "555-5678")
    assert "Alice" in result

def test_list_names_sorted():
    book = {"Charlie": "3", "Alice": "1", "Bob": "2"}
    assert list_names(book) == ["Alice", "Bob", "Charlie"]

def test_list_names_empty():
    assert list_names({}) == []
