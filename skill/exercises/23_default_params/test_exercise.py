"""Tests for Lesson 23: Default Parameters"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from exercise import format_message, create_tag, repeat_char

def test_format_defaults():
    assert format_message("hello") == "hello"

def test_format_uppercase():
    assert format_message("hello", uppercase=True) == "HELLO"

def test_format_prefix():
    assert format_message("hello", prefix=">>") == ">> hello"

def test_format_both():
    assert format_message("hi", True, "!!") == "!! HI"

def test_format_uppercase_false():
    assert format_message("Hello", uppercase=False) == "Hello"

def test_tag_defaults():
    assert create_tag("python") == "medium blue tag: python"

def test_tag_custom_color():
    assert create_tag("urgent", "red") == "medium red tag: urgent"

def test_tag_all_custom():
    assert create_tag("urgent", "red", "large") == "large red tag: urgent"

def test_tag_custom_size():
    assert create_tag("info", "blue", "small") == "small blue tag: info"

def test_repeat_default():
    assert repeat_char("*") == "*****"

def test_repeat_custom():
    assert repeat_char("#", 3) == "###"

def test_repeat_one():
    assert repeat_char("x", 1) == "x"
