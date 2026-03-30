"""Tests for Lesson 13: Loop Control — Password Checker"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from exercise import find_valid_passwords

def test_filters_short():
    """Should skip passwords shorter than 6 characters"""
    result = find_valid_passwords(["hi", "secret123", "ab", "longpass"])
    assert result == ["secret123", "longpass"]

def test_stops_at_quit():
    """Should stop when it sees 'quit'"""
    result = find_valid_passwords(["hello1", "quit", "never_seen"])
    assert result == ["hello1"], f"Should stop at 'quit', got: {result}"

def test_quit_not_included():
    """'quit' itself should not be in the result"""
    result = find_valid_passwords(["quit", "anything"])
    assert result == []

def test_no_quit():
    """Works when there's no 'quit' in the list"""
    result = find_valid_passwords(["short", "quitnow", "valid1"])
    assert "quitnow" in result and "valid1" in result

def test_empty_list():
    """Empty input returns empty list"""
    assert find_valid_passwords([]) == []

def test_all_short():
    """All short passwords returns empty list"""
    assert find_valid_passwords(["ab", "cd", "ef"]) == []
