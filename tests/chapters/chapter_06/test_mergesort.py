"""Tests for merge sort (migrated from source)."""

import random

from algo.chapters.chapter_06_sorting.nlogn.mergesort import merge_sort, merge_sorted_lists


def test_merge_sorted_lists_basic() -> None:
    """Merging two sorted lists produces a sorted result."""
    assert merge_sorted_lists([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]


def test_merge_sorted_lists_empty_right() -> None:
    """Merging with an empty right list returns the left list."""
    assert merge_sorted_lists([1, 2, 3], []) == [1, 2, 3]


def test_merge_sorted_lists_empty_left() -> None:
    """Merging with an empty left list returns the right list."""
    assert merge_sorted_lists([], [4, 5, 6]) == [4, 5, 6]


def test_merge_sorted_lists_unequal_lengths() -> None:
    """Merging lists of different lengths works correctly."""
    assert merge_sorted_lists([1, 3], [2]) == [1, 2, 3]


def test_merge_sort_random() -> None:
    """merge_sort produces a correctly sorted result for random input."""
    random.seed(0)
    sample = random.sample(range(100), 10)
    assert merge_sort(sample) == sorted(sample)


def test_merge_sort_empty() -> None:
    """merge_sort handles empty list."""
    assert merge_sort([]) == []


def test_merge_sort_single() -> None:
    """merge_sort handles single element."""
    assert merge_sort([7]) == [7]


def test_merge_sort_already_sorted() -> None:
    """merge_sort handles already-sorted input."""
    src = [1, 2, 3, 4, 5]
    assert merge_sort(src) == src


def test_merge_sort_reverse_sorted() -> None:
    """merge_sort handles reverse-sorted input."""
    src = [5, 4, 3, 2, 1]
    assert merge_sort(src) == [1, 2, 3, 4, 5]


def test_merge_sort_duplicates() -> None:
    """merge_sort handles all-duplicate values."""
    assert merge_sort([2, 2, 2, 2]) == [2, 2, 2, 2]
