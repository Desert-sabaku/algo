"""Tests for quicksort (migrated from source)."""

import random

from algo.chapters.chapter_06_sorting.nlogn.quicksort import quick_sort, quick_sort2


def test_quick_sort_basic() -> None:
    """quick_sort produces correct result."""
    src = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    assert quick_sort(src) == sorted(src)


def test_quick_sort2_basic() -> None:
    """quick_sort2 produces correct result."""
    random.seed(0)
    src = random.sample(range(100), 30)
    assert quick_sort2(src) == sorted(src)


def test_quick_sort_empty() -> None:
    """quick_sort handles empty list."""
    assert quick_sort([]) == []


def test_quick_sort2_empty() -> None:
    """quick_sort2 handles empty list."""
    assert quick_sort2([]) == []


def test_quick_sort_single() -> None:
    """quick_sort handles single element."""
    assert quick_sort([42]) == [42]


def test_quick_sort2_single() -> None:
    """quick_sort2 handles single element."""
    assert quick_sort2([99]) == [99]


def test_quick_sort_all_same() -> None:
    """quick_sort handles all-identical elements."""
    assert quick_sort([5, 5, 5, 5]) == [5, 5, 5, 5]


def test_quick_sort2_all_same() -> None:
    """quick_sort2 handles all-identical elements."""
    assert quick_sort2([5, 5, 5, 5]) == [5, 5, 5, 5]


def test_quick_sort_large_random() -> None:
    """quick_sort handles large random input."""
    random.seed(42)
    src = random.sample(range(1000), 200)
    assert quick_sort(src) == sorted(src)


def test_quick_sort2_large_random() -> None:
    """quick_sort2 handles large random input."""
    random.seed(42)
    src = random.sample(range(1000), 200)
    assert quick_sort2(src) == sorted(src)
