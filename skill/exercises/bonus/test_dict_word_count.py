"""Tests for Bonus: Word Counter"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from dict_word_count import word_count, most_common

def test_word_count_basic():
    result = word_count("hi hi hello")
    assert result == {"hi": 2, "hello": 1}

def test_word_count_single():
    result = word_count("word")
    assert result == {"word": 1}

def test_word_count_case_insensitive():
    result = word_count("Hi hi HI")
    assert result == {"hi": 3}

def test_word_count_returns_dict():
    result = word_count("a b c")
    assert isinstance(result, dict)

def test_word_count_all_different():
    result = word_count("one two three")
    assert result == {"one": 1, "two": 1, "three": 1}

def test_most_common_basic():
    assert most_common("the cat and the dog") == "the"

def test_most_common_clear_winner():
    assert most_common("a a a b b c") == "a"

def test_most_common_single():
    assert most_common("only") == "only"

def test_most_common_case_insensitive():
    assert most_common("Go go GO stay") == "go"
