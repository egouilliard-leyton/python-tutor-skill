"""Tests for Project 2: Text Adventure Game"""
import os

def read_source():
    with open(os.path.join(os.path.dirname(__file__), "game.py")) as f:
        return f.read()

def get_active_lines():
    return [l for l in read_source().split("\n")
            if l.strip() and not l.strip().startswith("#")]

def test_has_story_text():
    """Should print story/scene descriptions"""
    src = read_source()
    prints = [l for l in src.split("\n")
              if "print(" in l and not l.strip().startswith("#")]
    assert len(prints) >= 5, f"A story needs more text! Found {len(prints)} print statements."

def test_has_choices():
    """Should ask the player to make at least 2 choices"""
    src = read_source()
    inputs = [l for l in src.split("\n")
              if "input(" in l and not l.strip().startswith("#")]
    assert len(inputs) >= 2, f"Need at least 2 player choices. Found {len(inputs)}."

def test_has_branching():
    """Should use if/elif/else for branching paths"""
    src = read_source()
    active = [l for l in src.split("\n") if not l.strip().startswith("#")]
    active_src = "\n".join(active)
    ifs = active_src.count("if ")
    assert ifs >= 2, "Need at least 2 if statements for branching paths"

def test_has_multiple_endings():
    """Should have at least 2 different ending messages"""
    src = read_source()
    active_prints = [l.strip() for l in src.split("\n")
                     if "print(" in l and not l.strip().startswith("#")]
    ending_keywords = ["game over", "win", "end", "congratulations", "died",
                       "escaped", "lost", "victory", "score", "the end"]
    endings = sum(1 for p in active_prints
                  if any(k in p.lower() for k in ending_keywords))
    assert endings >= 2 or len(active_prints) >= 10, \
        "Add at least 2 different endings to your story"

def test_enough_code():
    """Should be a substantial program"""
    lines = get_active_lines()
    assert len(lines) >= 20, f"A text adventure needs more code! Found {len(lines)} lines."
