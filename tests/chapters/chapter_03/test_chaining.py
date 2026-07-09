"""Tests for ChainedHash in chaining.py."""

import pytest

from algo.chapters.chapter_03_search_hash.chaining import ChainedHash


def test_add_and_search() -> None:
    """add then search returns the value."""
    h: ChainedHash[str, int] = ChainedHash(10)
    assert h.add("a", 1) is True
    assert h.search("a") == 1


def test_search_missing() -> None:
    """Searching a missing key returns None."""
    h: ChainedHash[str, int] = ChainedHash(10)
    assert h.search("missing") is None


def test_add_duplicate_returns_false() -> None:
    """Adding a duplicate key returns False."""
    h: ChainedHash[str, int] = ChainedHash(10)
    h.add("x", 10)
    assert h.add("x", 20) is False
    assert h.search("x") == 10


def test_remove() -> None:
    """remove returns True and key is no longer findable."""
    h: ChainedHash[str, int] = ChainedHash(10)
    h.add("k", 99)
    assert h.remove("k") is True
    assert h.search("k") is None


def test_remove_missing() -> None:
    """Removing a missing key returns False."""
    h: ChainedHash[str, int] = ChainedHash(10)
    assert h.remove("nope") is False


def test_zero_capacity_raises() -> None:
    """Capacity 0 raises ValueError."""
    with pytest.raises(ValueError):
        ChainedHash[str, int](0)


def test_collision_handling() -> None:
    """Keys that collide on the same bucket are all stored and retrievable."""
    # Use capacity 1 to force all keys into the same bucket
    h: ChainedHash[int, str] = ChainedHash(1)
    h.add(1, "one")
    h.add(2, "two")
    h.add(3, "three")
    assert h.search(1) == "one"
    assert h.search(2) == "two"
    assert h.search(3) == "three"


def test_multiple_keys() -> None:
    """Multiple distinct keys can be stored and retrieved."""
    h: ChainedHash[str, int] = ChainedHash(5)
    for i, k in enumerate(["a", "b", "c", "d", "e"]):
        h.add(k, i)
    for i, k in enumerate(["a", "b", "c", "d", "e"]):
        assert h.search(k) == i
