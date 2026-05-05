"""Tests for sentinel linear search in sentinel.py."""

from algo.chapters.chapter_03_search_hash.sentinel import index_of, index_of2


def test_found() -> None:
    """Found element returns correct index."""
    assert index_of([1, 3, 5, 7], 5) == 2
    assert index_of2([1, 3, 5, 7], 5) == 2


def test_not_found() -> None:
    """Missing element returns None."""
    assert index_of([1, 2, 3], 9) is None
    assert index_of2([1, 2, 3], 9) is None


def test_first_element() -> None:
    """First element returns index 0."""
    assert index_of([10, 20, 30], 10) == 0
    assert index_of2([10, 20, 30], 10) == 0


def test_last_element() -> None:
    """Last element returns last index."""
    seq = [10, 20, 30]
    assert index_of(seq, 30) == 2
    assert index_of2(seq, 30) == 2


def test_both_agree() -> None:
    """index_of and index_of2 return identical results."""
    seq = [5, 3, 8, 1, 9, 2]
    for key in [5, 3, 8, 1, 9, 2, 0, 100]:
        assert index_of(seq, key) == index_of2(seq, key)


def test_string_sequence() -> None:
    """Works with a string sequence."""
    assert index_of("Hello", "l") == 2
    assert index_of2("Hello", "z") is None


def test_empty() -> None:
    """Empty sequence returns None."""
    assert index_of([], 1) is None
    assert index_of2([], 1) is None
