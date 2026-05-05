"""Tests for binary_search in binary_search.py."""

from algo.chapters.chapter_03_search_hash.binary_search import binary_search


def test_found_at_start() -> None:
    """Element at index 0 is found."""
    seq = [1, 2, 3, 4, 5]
    assert binary_search(seq, 1) == 0


def test_found_at_end() -> None:
    """Last element is found."""
    seq = [1, 2, 3, 4, 5]
    assert binary_search(seq, 5) == 4


def test_found_at_middle() -> None:
    """Middle element is found."""
    seq = [1, 2, 3, 4, 5]
    assert binary_search(seq, 3) == 2


def test_not_found() -> None:
    """Missing key returns None."""
    seq = [1, 2, 3, 4, 5]
    assert binary_search(seq, 6) is None


def test_single_element_found() -> None:
    """Single-element list returns 0 when key matches."""
    assert binary_search([42], 42) == 0


def test_single_element_not_found() -> None:
    """Single-element list returns None when key doesn't match."""
    assert binary_search([42], 99) is None


def test_strings() -> None:
    """Works with sorted string sequences."""
    seq = ["apple", "banana", "cherry"]
    assert binary_search(seq, "banana") == 1
    assert binary_search(seq, "grape") is None


def test_empty() -> None:
    """Empty sequence returns None."""
    assert binary_search([], 1) is None
