import heapq
import random
import unittest
from typing import Sequence

from algo.chapters.core.supports_less_than import SupportsLT


def merge_sorted_lists[T: SupportsLT](a: Sequence[T], b: Sequence[T]) -> list[T]:
    """Merge two sorted lists."""
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
    def merge_sort_impl(src: list[T]) -> list[T]:
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
    def test_merge_sorted_lists(self):
        self.assertEqual(merge_sorted_lists([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(merge_sorted_lists([1, 2, 3], []), [1, 2, 3])
        self.assertEqual(merge_sorted_lists([], [4, 5, 6]), [4, 5, 6])
        self.assertEqual(merge_sorted_lists([1, 3], [2]), [1, 2, 3])

    def test_merge_sort(self):
        random.seed(0)
        sample = random.sample(range(100), 10)
        self.assertEqual(
            merge_sort(sample),
            sorted(sample),
        )
        self.assertEqual(merge_sort([]), [])


if __name__ == "__main__":
    unittest.main()
