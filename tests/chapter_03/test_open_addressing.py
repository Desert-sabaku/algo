"""Tests for OpenHash in open_addressing.py."""

import pytest

from algo.chapters.chapter_03_search_hash.open_addressing import OpenHash


def test_add_and_search() -> None:
    """add then search returns the value."""
    h: OpenHash[str, int] = OpenHash(10)
    assert h.add("a", 1) is True
    assert h.search("a") == 1


def test_search_missing() -> None:
    """Searching a missing key returns None."""
    h: OpenHash[str, int] = OpenHash(10)
    assert h.search("missing") is None


def test_add_duplicate_returns_false() -> None:
    """Adding a duplicate key returns False."""
    h: OpenHash[str, int] = OpenHash(10)
    h.add("x", 10)
    assert h.add("x", 20) is False
    assert h.search("x") == 10


def test_remove() -> None:
    """remove returns True and key is no longer findable."""
    h: OpenHash[str, int] = OpenHash(10)
    h.add("k", 99)
    assert h.remove("k") is True
    assert h.search("k") is None


def test_remove_missing() -> None:
    """Removing a missing key returns False."""
    h: OpenHash[str, int] = OpenHash(10)
    assert h.remove("nope") is False


def test_zero_capacity_raises() -> None:
    """Capacity 0 raises ValueError."""
    with pytest.raises(ValueError):
        OpenHash[str, int](0)


def test_add_after_remove_reuses_slot() -> None:
    """A new key can be inserted into a previously deleted slot."""
    h: OpenHash[str, int] = OpenHash(3)
    h.add("a", 1)
    h.add("b", 2)
    h.remove("a")
    # Adding a new key "c" should succeed (reuses deleted slot)
    assert h.add("c", 3) is True
    assert h.search("c") == 3


def test_table_full() -> None:
    """Adding beyond capacity returns False."""
    h: OpenHash[str, int] = OpenHash(1)
    assert h.add("first", 1) is True
    assert h.add("second", 2) is False
