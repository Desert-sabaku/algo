"""Tests for heapsort (migrated from source)."""

import random

from algo.chapters.chapter_06_sorting.nlogn.heapsort import heap_sort, sift_down


def test_sift_down_root_sinks_one_level() -> None:
    """Root smaller than children sinks one level."""
    src = [1, 10, 5, 2, 3]
    sift_down(src, 0, 4)
    assert src[0] == 10
    assert 1 in src


def test_sift_down_root_sinks_multiple_levels() -> None:
    """Root smallest sinks through multiple levels."""
    src = [1, 10, 9, 5, 3, 8, 7]
    sift_down(src, 0, 6)
    assert src[0] == 10
    assert 1 in src


def test_sift_down_already_valid() -> None:
    """Root already >= children; no change."""
    src = [10, 5, 8, 2, 3, 6, 4]
    original = src.copy()
    sift_down(src, 0, 6)
    assert src == original


def test_sift_down_only_left_child() -> None:
    """Root with only left child swaps if smaller."""
    src = [1, 10]
    sift_down(src, 0, 1)
    assert src[0] == 10
    assert src[1] == 1


def test_sift_down_root_larger_than_left_child() -> None:
    """No change needed when root >= left child."""
    src = [10, 5]
    original = src.copy()
    sift_down(src, 0, 1)
    assert src == original


def test_sift_down_partial_range() -> None:
    """sift_down only operates on the specified sub-range."""
    src = [1, 10, 5, 2, 3, 100, 200]
    sift_down(src, 0, 4)
    assert src[5] == 100
    assert src[6] == 200
    assert src[0] == 10


def test_sift_down_single_element() -> None:
    """Single element list is unchanged."""
    src = [42]
    original = src.copy()
    sift_down(src, 0, 0)
    assert src == original


def test_sift_down_equal_children() -> None:
    """Equal children: left child should be preferred."""
    src = [1, 5, 5, 2, 3]
    sift_down(src, 0, 4)
    assert src[0] == 5


def test_heap_sort_random() -> None:
    """heap_sort produces a correctly sorted result."""
    src = [random.randint(0, 100) for _ in range(100)]
    assert heap_sort(src) == sorted(src)


def test_heap_sort_empty() -> None:
    """heap_sort handles empty list."""
    assert heap_sort([]) == []


def test_heap_sort_single() -> None:
    """heap_sort handles single element."""
    assert heap_sort([42]) == [42]


def test_heap_sort_duplicates() -> None:
    """heap_sort correctly handles duplicate values."""
    assert heap_sort([3, 1, 3, 2, 1]) == [1, 1, 2, 3, 3]
