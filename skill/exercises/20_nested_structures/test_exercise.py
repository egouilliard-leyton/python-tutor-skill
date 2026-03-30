"""Tests for Lesson 20: Nested Structures"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from exercise import get_names, best_student, filter_by_subject, average_grade

STUDENTS = [
    {"name": "Alice", "grade": 85, "subject": "math"},
    {"name": "Bob", "grade": 72, "subject": "science"},
    {"name": "Charlie", "grade": 91, "subject": "math"},
]

def test_get_names():
    assert get_names(STUDENTS) == ["Alice", "Bob", "Charlie"]

def test_get_names_single():
    assert get_names([{"name": "X", "grade": 50, "subject": "art"}]) == ["X"]

def test_best_student():
    assert best_student(STUDENTS) == "Charlie"

def test_best_student_first():
    data = [{"name": "Top", "grade": 100, "subject": "x"}, {"name": "Low", "grade": 10, "subject": "x"}]
    assert best_student(data) == "Top"

def test_filter_math():
    result = filter_by_subject(STUDENTS, "math")
    names = [s["name"] for s in result]
    assert names == ["Alice", "Charlie"]

def test_filter_none():
    assert filter_by_subject(STUDENTS, "art") == []

def test_average():
    assert average_grade(STUDENTS) == 82.7

def test_average_round():
    data = [{"name": "A", "grade": 33, "subject": "x"}, {"name": "B", "grade": 33, "subject": "x"}]
    assert average_grade(data) == 33.0
