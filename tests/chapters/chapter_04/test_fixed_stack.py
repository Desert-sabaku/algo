"""Tests for FixedStack in fixed_stack.py."""

import pytest

from algo.chapters.chapter_04_stacks_queues.fixed_stack import FixedStack


def test_push_pop() -> None:
    """push and pop return elements in LIFO order."""
    s: FixedStack[int] = FixedStack(5)
    s.push(1)
    s.push(2)
    s.push(3)
    assert s.pop() == 3
    assert s.pop() == 2
    assert s.pop() == 1


def test_peek() -> None:
    """peek returns top without removing it."""
    s: FixedStack[int] = FixedStack(5)
    s.push(42)
    assert s.peek() == 42
    assert len(s) == 1


def test_pop_empty_raises() -> None:
    """pop on empty stack raises FixedStack.Empty."""
    s: FixedStack[int] = FixedStack(5)
    with pytest.raises(FixedStack.Empty):
        s.pop()


def test_peek_empty_raises() -> None:
    """peek on empty stack raises FixedStack.Empty."""
    s: FixedStack[int] = FixedStack(5)
    with pytest.raises(FixedStack.Empty):
        s.peek()


def test_push_full_raises() -> None:
    """push beyond capacity raises FixedStack.Full."""
    s: FixedStack[int] = FixedStack(2)
    s.push(1)
    s.push(2)
    with pytest.raises(FixedStack.Full):
        s.push(3)


def test_zero_capacity_raises() -> None:
    """Capacity 0 raises ValueError."""
    with pytest.raises(ValueError):
        FixedStack[int](0)


def test_len() -> None:
    """__len__ reflects current number of elements."""
    s: FixedStack[int] = FixedStack(5)
    assert len(s) == 0
    s.push(1)
    assert len(s) == 1
    s.push(2)
    assert len(s) == 2
    s.pop()
    assert len(s) == 1


def test_is_empty_and_full() -> None:
    """is_empty and is_full behave correctly."""
    s: FixedStack[int] = FixedStack(2)
    assert s.is_empty() is True
    assert s.is_full() is False
    s.push(1)
    s.push(2)
    assert s.is_empty() is False
    assert s.is_full() is True


def test_find() -> None:
    """find returns the storage index or None."""
    s: FixedStack[int] = FixedStack(5)
    s.push(10)
    s.push(20)
    s.push(30)
    assert s.find(20) == 1
    assert s.find(99) is None


def test_count() -> None:
    """count returns number of occurrences."""
    s: FixedStack[int] = FixedStack(5)
    s.push(1)
    s.push(2)
    s.push(1)
    assert s.count(1) == 2
    assert s.count(2) == 1
    assert s.count(9) == 0


def test_contains() -> None:
    """__contains__ returns True iff element is in stack."""
    s: FixedStack[int] = FixedStack(5)
    s.push(7)
    assert 7 in s
    assert 8 not in s


def test_clear() -> None:
    """clear empties the stack."""
    s: FixedStack[int] = FixedStack(5)
    s.push(1)
    s.push(2)
    s.clear()
    assert s.is_empty() is True
    assert len(s) == 0
