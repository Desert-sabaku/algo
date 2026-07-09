"""Tests for FixedQueue in queue.py."""

import pytest

from algo.chapters.chapter_04_stacks_queues.queue import FixedQueue


def test_enqueue_dequeue_fifo() -> None:
    """Elements dequeue in FIFO order."""
    q: FixedQueue[int] = FixedQueue(5)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert q.dequeue() == 1
    assert q.dequeue() == 2
    assert q.dequeue() == 3


def test_peek() -> None:
    """peek returns front element without removing it."""
    q: FixedQueue[int] = FixedQueue(5)
    q.enqueue(42)
    assert q.peek() == 42
    assert len(q) == 1


def test_dequeue_empty_raises() -> None:
    """dequeue on empty queue raises EmptyError."""
    q: FixedQueue[int] = FixedQueue(5)
    with pytest.raises(FixedQueue.EmptyError):
        q.dequeue()


def test_peek_empty_raises() -> None:
    """peek on empty queue raises EmptyError."""
    q: FixedQueue[int] = FixedQueue(5)
    with pytest.raises(FixedQueue.EmptyError):
        q.peek()


def test_enqueue_full_raises() -> None:
    """enqueue on full queue raises FullError."""
    q: FixedQueue[int] = FixedQueue(2)
    q.enqueue(1)
    q.enqueue(2)
    with pytest.raises(FixedQueue.FullError):
        q.enqueue(3)


def test_zero_capacity_raises() -> None:
    """Capacity 0 raises ValueError."""
    with pytest.raises(ValueError):
        FixedQueue[int](0)


def test_ring_buffer_wraparound() -> None:
    """Ring buffer wraps around correctly after dequeue + enqueue."""
    q: FixedQueue[int] = FixedQueue(3)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert q.dequeue() == 1
    assert q.dequeue() == 2
    q.enqueue(4)
    q.enqueue(5)
    assert q.dequeue() == 3
    assert q.dequeue() == 4
    assert q.dequeue() == 5


def test_len() -> None:
    """__len__ reflects current size."""
    q: FixedQueue[int] = FixedQueue(5)
    assert len(q) == 0
    q.enqueue(1)
    assert len(q) == 1
    q.dequeue()
    assert len(q) == 0


def test_is_empty_and_full() -> None:
    """is_empty and is_full behave correctly."""
    q: FixedQueue[int] = FixedQueue(2)
    assert q.is_empty() is True
    q.enqueue(1)
    q.enqueue(2)
    assert q.is_full() is True


def test_find() -> None:
    """find returns physical index of value or None."""
    q: FixedQueue[int] = FixedQueue(5)
    q.enqueue(10)
    q.enqueue(20)
    assert q.find(10) is not None
    assert q.find(99) is None


def test_count() -> None:
    """count returns occurrence count."""
    q: FixedQueue[int] = FixedQueue(5)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(1)
    assert q.count(1) == 2
    assert q.count(3) == 0


def test_contains() -> None:
    """__contains__ works correctly."""
    q: FixedQueue[int] = FixedQueue(5)
    q.enqueue(7)
    assert 7 in q
    assert 8 not in q


def test_elements() -> None:
    """elements property returns list in FIFO order."""
    q: FixedQueue[int] = FixedQueue(5)
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    assert q.elements == [10, 20, 30]


def test_clear() -> None:
    """clear empties the queue."""
    q: FixedQueue[int] = FixedQueue(5)
    q.enqueue(1)
    q.enqueue(2)
    q.clear()
    assert q.is_empty() is True
    assert len(q) == 0
