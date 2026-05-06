"""Tests for FixedStack (deque-backed) in fixed_stack_by_deque.py."""

import pytest

from algo.chapters.chapter_04_stacks_queues.fixed_stack_by_deque import FixedStack


def test_push_pop() -> None:
    """push and pop return elements in LIFO order."""
    s: FixedStack[int] = FixedStack(5)
    s.push(1)
    s.push(2)
    s.push(3)
    assert s.pop() == 3
    assert s.pop() == 2
    assert s.pop() == 1


def test_pop_empty_raises() -> None:
    """pop on empty deque-backed stack raises IndexError."""
    s: FixedStack[int] = FixedStack(5)
    with pytest.raises(IndexError):
        s.pop()


def test_push_full_raises() -> None:
    """push beyond capacity raises ValueError."""
    s: FixedStack[int] = FixedStack(2)
    s.push(1)
    s.push(2)
    with pytest.raises(ValueError):
        s.push(3)


def test_zero_capacity_raises() -> None:
    """Capacity 0 raises ValueError."""
    with pytest.raises(ValueError):
        FixedStack[int](0)


def test_len() -> None:
    """__len__ reflects current number of elements."""
    s: FixedStack[int] = FixedStack(5)
    assert len(s) == 0
    s.push(10)
    assert len(s) == 1


def test_contains() -> None:
    """__contains__ returns True iff element is in stack."""
    s: FixedStack[int] = FixedStack(5)
    s.push(7)
    assert 7 in s
    assert 8 not in s


def test_find() -> None:
    """find returns internal index or None."""
    s: FixedStack[int] = FixedStack(5)
    s.push(10)
    s.push(20)
    s.push(30)
    assert s.find(10) is not None
    assert s.find(99) is None


def test_is_empty_and_full() -> None:
    """is_empty and is_full behave correctly."""
    s: FixedStack[int] = FixedStack(2)
    assert s.is_empty() is True
    assert s.is_full() is False
    s.push(1)
    s.push(2)
    assert s.is_empty() is False
    assert s.is_full() is True
