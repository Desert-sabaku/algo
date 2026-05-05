"""Tests for all sort functions in sort.py using parametrize."""

from collections.abc import Callable, Sequence
from typing import Any

import pytest

from algo.chapters.chapter_06_sorting.sort import (
    binary_insertion_sort,
    binary_insertion_sort2,
    bubble_sort,
    bubble_sort2,
    bubble_sort3,
    selection_sort,
    shaker_sort,
    shell_sort,
    shell_sort2,
    shuttle_sort,
)

SortFn = Callable[[Sequence[int]], list[int]]

SORT_FUNCTIONS: list[tuple[str, SortFn]] = [
    ("bubble_sort", bubble_sort),
    ("bubble_sort2", bubble_sort2),
    ("bubble_sort3", bubble_sort3),
    ("shaker_sort", shaker_sort),
    ("selection_sort", selection_sort),
    ("binary_insertion_sort", binary_insertion_sort),
    ("binary_insertion_sort2", binary_insertion_sort2),
    ("shell_sort", shell_sort),
    ("shell_sort2", shell_sort2),
]


@pytest.mark.parametrize("name,fn", SORT_FUNCTIONS, ids=[n for n, _ in SORT_FUNCTIONS])
def test_sort_random(name: str, fn: SortFn) -> None:
    """Sort function produces a correctly sorted result."""
    src = [5, 3, 8, 1, 9, 2, 7, 4, 6]
    assert fn(src) == sorted(src)


@pytest.mark.parametrize("name,fn", SORT_FUNCTIONS, ids=[n for n, _ in SORT_FUNCTIONS])
def test_sort_empty(name: str, fn: SortFn) -> None:
    """Sort function handles empty list."""
    assert fn([]) == []


@pytest.mark.parametrize("name,fn", SORT_FUNCTIONS, ids=[n for n, _ in SORT_FUNCTIONS])
def test_sort_single(name: str, fn: SortFn) -> None:
    """Sort function handles single-element list."""
    assert fn([42]) == [42]


@pytest.mark.parametrize("name,fn", SORT_FUNCTIONS, ids=[n for n, _ in SORT_FUNCTIONS])
def test_sort_already_sorted(name: str, fn: SortFn) -> None:
    """Sort function handles already-sorted input."""
    src = [1, 2, 3, 4, 5]
    assert fn(src) == src


@pytest.mark.parametrize("name,fn", SORT_FUNCTIONS, ids=[n for n, _ in SORT_FUNCTIONS])
def test_sort_reverse_sorted(name: str, fn: SortFn) -> None:
    """Sort function handles reverse-sorted input."""
    src = [5, 4, 3, 2, 1]
    assert fn(src) == sorted(src)


@pytest.mark.parametrize("name,fn", SORT_FUNCTIONS, ids=[n for n, _ in SORT_FUNCTIONS])
def test_sort_does_not_mutate_input(name: str, fn: SortFn) -> None:
    """Sort function does not mutate the input sequence."""
    src = [3, 1, 4, 1, 5, 9]
    original = src.copy()
    fn(src)
    assert src == original


def test_shuttle_sort_inplace() -> None:
    """shuttle_sort with is_inplace=True sorts the list in-place."""
    src = [3, 1, 4, 1, 5]
    shuttle_sort(src, is_inplace=True)
    assert src == sorted([3, 1, 4, 1, 5])
