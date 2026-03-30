"""Tests for Lesson 22: Parameters & Return"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from exercise import convert_f_to_c, convert_c_to_f, convert_temp

def test_freezing_f_to_c():
    assert convert_f_to_c(32) == 0.0

def test_boiling_f_to_c():
    assert convert_f_to_c(212) == 100.0

def test_body_temp_f_to_c():
    assert convert_f_to_c(98.6) == 37.0

def test_negative_f_to_c():
    assert convert_f_to_c(-40) == -40.0

def test_rounding_f_to_c():
    result = convert_f_to_c(100)
    assert result == 37.8, f"Expected 37.8, got {result} — did you round to 1 decimal?"

def test_freezing_c_to_f():
    assert convert_c_to_f(0) == 32.0

def test_boiling_c_to_f():
    assert convert_c_to_f(100) == 212.0

def test_body_temp_c_to_f():
    assert convert_c_to_f(37) == 98.6

def test_negative_c_to_f():
    assert convert_c_to_f(-40) == -40.0

def test_rounding_c_to_f():
    result = convert_c_to_f(23)
    assert result == 73.4, f"Expected 73.4, got {result} — did you round to 1 decimal?"

def test_convert_temp_from_f():
    assert convert_temp(32, "F") == 0.0

def test_convert_temp_from_c():
    assert convert_temp(100, "C") == 212.0

def test_convert_temp_boiling_f():
    assert convert_temp(212, "F") == 100.0
