"""Tests for Lesson 17: List Methods — Playlist Manager"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from exercise import add_song, remove_song, get_top_3, sort_playlist

def test_add_song():
    assert add_song(["Hey", "Imagine"], "Yesterday") == ["Hey", "Imagine", "Yesterday"]

def test_add_to_empty():
    assert add_song([], "First") == ["First"]

def test_remove_song():
    assert remove_song(["Hey", "Imagine"], "Hey") == ["Imagine"]

def test_remove_nonexistent():
    """Removing a song that doesn't exist should return the list unchanged"""
    assert remove_song(["Hey", "Imagine"], "Nope") == ["Hey", "Imagine"]

def test_top_3():
    assert get_top_3(["A", "B", "C", "D", "E"]) == ["A", "B", "C"]

def test_top_3_short():
    """If fewer than 3 songs, return all of them"""
    assert get_top_3(["A", "B"]) == ["A", "B"]

def test_sort():
    assert sort_playlist(["Cherry", "Apple", "Banana"]) == ["Apple", "Banana", "Cherry"]

def test_sort_doesnt_modify_original():
    """sort_playlist should not change the original list"""
    original = ["Cherry", "Apple", "Banana"]
    sort_playlist(original)
    assert original == ["Cherry", "Apple", "Banana"], \
        "Don't modify the original! Use sorted() instead of .sort()"
