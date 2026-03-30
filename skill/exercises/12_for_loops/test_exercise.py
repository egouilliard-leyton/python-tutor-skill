"""Tests for Lesson 12: For Loops — FizzBuzz"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from exercise import fizzbuzz

def test_fizzbuzz_5():
    """fizzbuzz(5) basic test"""
    assert fizzbuzz(5) == [1, 2, "Fizz", 4, "Buzz"]

def test_fizz_at_3():
    """3 should be 'Fizz'"""
    result = fizzbuzz(3)
    assert result[2] == "Fizz", f"Position 3 should be 'Fizz', got: {result[2]}"

def test_buzz_at_5():
    """5 should be 'Buzz'"""
    result = fizzbuzz(5)
    assert result[4] == "Buzz", f"Position 5 should be 'Buzz', got: {result[4]}"

def test_fizzbuzz_at_15():
    """15 should be 'FizzBuzz'"""
    result = fizzbuzz(15)
    assert result[14] == "FizzBuzz", f"Position 15 should be 'FizzBuzz', got: {result[14]}"

def test_regular_numbers():
    """Non-multiples should be numbers, not strings"""
    result = fizzbuzz(5)
    assert result[0] == 1, f"1 should stay as number 1, got: {result[0]}"
    assert result[3] == 4, f"4 should stay as number 4, got: {result[3]}"

def test_correct_length():
    """fizzbuzz(n) should have exactly n items"""
    assert len(fizzbuzz(15)) == 15
    assert len(fizzbuzz(1)) == 1

def test_returns_list():
    """Should return a list"""
    assert isinstance(fizzbuzz(5), list)
