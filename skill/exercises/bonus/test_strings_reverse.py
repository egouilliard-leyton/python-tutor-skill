"""Tests for Bonus: String Reversal & Palindromes"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from strings_reverse import reverse_string, is_palindrome

def test_reverse_basic():
    assert reverse_string("hello") == "olleh"

def test_reverse_single():
    assert reverse_string("a") == "a"

def test_reverse_empty():
    assert reverse_string("") == ""

def test_reverse_with_spaces():
    assert reverse_string("hi there") == "ereht ih"

def test_palindrome_true():
    assert is_palindrome("racecar") == True

def test_palindrome_false():
    assert is_palindrome("hello") == False

def test_palindrome_case_insensitive():
    assert is_palindrome("Racecar") == True

def test_palindrome_single():
    assert is_palindrome("a") == True

def test_palindrome_madam():
    assert is_palindrome("Madam") == True
