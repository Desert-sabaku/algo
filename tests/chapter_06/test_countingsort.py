"""Tests for counting sort (migrated from source)."""

import pytest

from algo.chapters.chapter_06_sorting.nlogn.countingsort import counting_sort


def test_counting_sort_basic() -> None:
    """counting_sort produces a correctly sorted result."""
    src = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    assert counting_sort(src) == sorted(src)


def test_counting_sort_empty() -> None:
    """counting_sort handles empty input."""
    assert counting_sort([]) == []


def test_counting_sort_single() -> None:
    """counting_sort handles single element."""
    assert counting_sort([7]) == [7]


def test_counting_sort_negative_raises() -> None:
    """counting_sort raises ValueError for negative elements."""
    with pytest.raises(ValueError):
        counting_sort([-1, 2, 3])


def test_counting_sort_all_same() -> None:
    """counting_sort handles all-identical values."""
    assert counting_sort([3, 3, 3]) == [3, 3, 3]


def test_counting_sort_zeros() -> None:
    """counting_sort handles zeros correctly."""
    assert counting_sort([0, 0, 1, 0]) == [0, 0, 0, 1]
