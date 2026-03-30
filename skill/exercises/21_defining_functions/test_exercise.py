"""Tests for Lesson 21: Defining Functions"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from exercise import greet, double, is_even, repeat_string

def test_greet():
    assert greet("Charles") == "Hello, Charles!"

def test_greet_different():
    assert greet("World") == "Hello, World!"

def test_double():
    assert double(5) == 10

def test_double_zero():
    assert double(0) == 0

def test_double_negative():
    assert double(-3) == -6

def test_is_even_true():
    assert is_even(4) == True

def test_is_even_false():
    assert is_even(7) == False

def test_is_even_zero():
    assert is_even(0) == True

def test_repeat():
    assert repeat_string("ha", 3) == "hahaha"

def test_repeat_once():
    assert repeat_string("hello", 1) == "hello"

def test_repeat_empty():
    assert repeat_string("x", 0) == ""
