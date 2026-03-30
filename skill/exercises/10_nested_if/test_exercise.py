"""Tests for Lesson 10: Nested Conditions — Movie Ticket Pricer"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from exercise import ticket_price

def test_child_normal():
    """Child on normal day = 6"""
    assert ticket_price(10, False, "monday") == 6

def test_adult_student():
    """Adult student on normal day = 10"""
    assert ticket_price(25, True, "monday") == 10

def test_adult_tuesday():
    """Adult on Tuesday = 10"""
    assert ticket_price(25, False, "tuesday") == 10

def test_student_tuesday():
    """Student on Tuesday = 8 (both discounts)"""
    assert ticket_price(25, True, "tuesday") == 8

def test_senior_tuesday():
    """Senior on Tuesday = 6"""
    assert ticket_price(70, False, "tuesday") == 6

def test_child_tuesday_minimum():
    """Child on Tuesday = 4 (minimum price)"""
    assert ticket_price(8, False, "tuesday") == 4

def test_adult_normal():
    """Adult on normal day = 12"""
    assert ticket_price(30, False, "friday") == 12

def test_senior_normal():
    """Senior on normal day = 8"""
    assert ticket_price(65, False, "saturday") == 8

def test_child_not_student():
    """Child can't be student — student discount shouldn't apply to children"""
    assert ticket_price(10, True, "monday") == 6
