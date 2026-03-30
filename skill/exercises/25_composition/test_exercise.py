"""Tests for Lesson 25: Function Composition"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from exercise import clean_text, extract_words, count_unique, process_text

def test_clean_strips_whitespace():
    assert clean_text("  hello  ") == "hello"

def test_clean_lowercases():
    assert clean_text("HELLO") == "hello"

def test_clean_both():
    assert clean_text("  Hello World  ") == "hello world"

def test_extract_basic():
    assert extract_words("hello world") == ["hello", "world"]

def test_extract_duplicates():
    assert extract_words("hi hi hi") == ["hi", "hi", "hi"]

def test_extract_single():
    assert extract_words("word") == ["word"]

def test_count_unique_all_different():
    assert count_unique(["a", "b", "c"]) == 3

def test_count_unique_with_dupes():
    assert count_unique(["a", "b", "a", "c"]) == 3

def test_count_unique_all_same():
    assert count_unique(["x", "x", "x"]) == 1

def test_pipeline_basic():
    assert process_text("  Hi hi Hello hello  ") == 2

def test_pipeline_all_unique():
    assert process_text("one two three") == 3

def test_pipeline_all_same():
    assert process_text("  SAME same Same  ") == 1

def test_pipeline_with_whitespace():
    assert process_text("  Apple banana APPLE Banana  ") == 2
