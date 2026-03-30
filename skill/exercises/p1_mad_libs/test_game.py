"""Tests for Project 1: Mad Libs Generator"""
import os

def read_source():
    with open(os.path.join(os.path.dirname(__file__), "game.py")) as f:
        return f.read()

def test_uses_input():
    """Should ask the user for at least 3 words"""
    src = read_source()
    count = src.count("input(")
    # Don't count commented-out lines
    active = sum(1 for line in src.split("\n")
                 if "input(" in line and not line.strip().startswith("#"))
    assert active >= 3, f"Ask for at least 3 words using input(). Found {active} active input() calls."

def test_uses_variables():
    """Should store words in variables"""
    src = read_source()
    lines = [l.strip() for l in src.split("\n")
             if "=" in l and "input(" in l and not l.strip().startswith("#")]
    assert len(lines) >= 3, "Store each word in a variable: word = input('...')"

def test_prints_story():
    """Should print a story using the variables"""
    src = read_source()
    active_prints = [l for l in src.split("\n")
                     if "print(" in l and not l.strip().startswith("#")
                     and ("f'" in l or 'f"' in l or "{" in l or "+" in l)]
    assert len(active_prints) >= 1, "Print your story using f-strings with the variables"

def test_has_enough_code():
    """Should have meaningful code (not just the starter)"""
    src = read_source()
    active_lines = [l for l in src.split("\n")
                    if l.strip() and not l.strip().startswith("#")]
    assert len(active_lines) >= 8, f"Your program needs more code. Found {len(active_lines)} lines."

def test_asks_for_word_types():
    """Input prompts should tell the user what type of word to give"""
    src = read_source()
    prompts = [l for l in src.split("\n")
               if "input(" in l and not l.strip().startswith("#")]
    for prompt in prompts:
        lower = prompt.lower()
        has_word_type = any(w in lower for w in [
            "noun", "verb", "adjective", "adverb", "name",
            "place", "food", "animal", "color", "number"
        ])
        if not has_word_type:
            # Not a hard fail, just check they have descriptive prompts
            assert '"' in prompt or "'" in prompt, \
                "Each input() should have a descriptive prompt string"
