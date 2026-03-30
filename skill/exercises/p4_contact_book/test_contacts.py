"""Tests for Project 4: Contact Book"""
import os

def read_source():
    with open(os.path.join(os.path.dirname(__file__), "contacts.py")) as f:
        return f.read()

def get_active_lines():
    return [l for l in read_source().split("\n")
            if l.strip() and not l.strip().startswith("#")]

def test_uses_dictionary():
    """Should use a dictionary to store contacts"""
    src = read_source()
    active = "\n".join(l for l in src.split("\n") if not l.strip().startswith("#"))
    assert "{}" in active or "dict(" in active, \
        "Create a dictionary to store contacts (e.g., contacts = {})"

def test_uses_input():
    """Should get user input"""
    src = read_source()
    active = [l for l in src.split("\n")
              if "input(" in l and not l.strip().startswith("#")]
    assert len(active) >= 1, "Use input() to get the user's menu choice and contact info"

def test_has_add_function():
    """Should have a function to add contacts"""
    src = read_source()
    active = "\n".join(l for l in src.split("\n") if not l.strip().startswith("#"))
    assert "def " in active and "add" in active.lower(), \
        "Write a function to add contacts (e.g., def add_contact)"

def test_has_search_function():
    """Should have a function to search contacts"""
    src = read_source()
    active = "\n".join(l for l in src.split("\n") if not l.strip().startswith("#"))
    assert "def " in active and "search" in active.lower(), \
        "Write a function to search contacts (e.g., def search_contact)"

def test_has_list_function():
    """Should have a function to list contacts"""
    src = read_source()
    active = "\n".join(l for l in src.split("\n") if not l.strip().startswith("#"))
    assert "def " in active and "list" in active.lower(), \
        "Write a function to list all contacts (e.g., def list_contacts)"

def test_has_while_loop():
    """Should use a while loop for the menu"""
    src = read_source()
    active = [l for l in src.split("\n") if not l.strip().startswith("#")]
    has_while = any("while" in l for l in active)
    assert has_while, "Use a while loop to keep showing the menu"

def test_enough_code():
    """Should be a substantial program"""
    lines = get_active_lines()
    assert len(lines) >= 20, f"Your contact book needs more code! Found {len(lines)} lines."
