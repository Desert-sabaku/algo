"""Merge sort implementation and tests."""

import heapq
import random
import unittest
from typing import Sequence

from algo.chapters.core.supports_less_than import SupportsLT


def merge_sorted_lists[T: SupportsLT](a: Sequence[T], b: Sequence[T]) -> list[T]:
    """Merge two already-sorted sequences into a single sorted list.

    Args:
        a: First sorted sequence.
        b: Second sorted sequence.

    Returns:
        A new sorted list containing all elements from ``a`` and ``b``.
    """
    rslt: list[T] = []
    a_idx, b_idx = 0, 0
    while a_idx < len(a) and b_idx < len(b):
        if a[a_idx] < b[b_idx]:
            rslt.append(a[a_idx])
            a_idx += 1
        else:
            rslt.append(b[b_idx])
            b_idx += 1
    rslt.extend(a[a_idx:])
    rslt.extend(b[b_idx:])
    return rslt


def merge_sort[T: SupportsLT](src: Sequence[T]) -> list[T]:
    """Return a new list sorted in ascending order using merge sort.

    Recursively divides the sequence in half, sorts each half, then merges
    the sorted halves using ``heapq.merge``.  Time complexity is O(n log n).

    Args:
        src: Input sequence to sort.

    Returns:
        A new sorted list containing all elements of ``src``.
    """

    def merge_sort_impl(src: list[T]) -> list[T]:
        """Recursively sort ``src`` in-place by splitting and merging."""
        if len(src) <= 1:
            return src

        mid = len(src) // 2
        left = merge_sort(src[:mid])
        right = merge_sort(src[mid:])

        # return merge_sorted_lists(left, right)
        return list(heapq.merge(left, right))

    rslt = list(src)
    return merge_sort_impl(rslt)


class TestMergeSortedLists(unittest.TestCase):
    """Tests for merge_sorted_lists and merge_sort."""

    def test_merge_sorted_lists(self) -> None:
        """Verify merging of various sorted list pairs."""
        self.assertEqual(merge_sorted_lists([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(merge_sorted_lists([1, 2, 3], []), [1, 2, 3])
        self.assertEqual(merge_sorted_lists([], [4, 5, 6]), [4, 5, 6])
        self.assertEqual(merge_sorted_lists([1, 3], [2]), [1, 2, 3])

    def test_merge_sort(self) -> None:
        """Verify that merge_sort produces a correctly sorted result."""
        random.seed(0)
        sample = random.sample(range(100), 10)
        self.assertEqual(
            merge_sort(sample),
            sorted(sample),
        )
        self.assertEqual(merge_sort([]), [])


if __name__ == "__main__":
    unittest.main()
