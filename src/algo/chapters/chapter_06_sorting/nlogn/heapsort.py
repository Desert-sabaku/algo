"""Heap sort implementation and tests."""

import heapq
import random
import unittest
from typing import Sequence

from algo.chapters.core.supports_less_than import SupportsLT


def sift_down(src: list[int], lo: int, hi: int) -> None:
    """A function that corrects a heap with incorrect root values by repositioning it to the correct locations

    Args:
        src (list[int]): A pseudo-heap that is correct except for the root value
        lo (int): Inclusive lower limit
        hi (int): Inclusive upper limit
    """
    # 沈めたい値
    candidate = src[lo]

    parent = lo
    # `parent`に少なくとも左子が存在するなら
    while parent < (hi + lo + 1) // 2:
        # 左右の子を比較し大きい方を取得
        lc = 2 * parent - lo + 1
        rc = lc + 1
        ## 右が存在し左より大きければ右を、さもなくば左を
        flag = rc <= hi and src[rc] > src[lc]
        child = rc if flag else lc

        # ヒープ条件の確認
        if candidate >= src[child]:
            break
        else:
            src[parent] = src[child]
            parent = child
    src[parent] = candidate


def heap_sort[T: SupportsLT](src: Sequence[T]) -> list[T]:
    """Return a new list sorted in ascending order using heap sort."""
    heap = list(src)
    heapq.heapify(heap)

    rslt: list[T] = []
    while heap:
        rslt.append(heapq.heappop(heap))

    return rslt


class TestSiftDown(unittest.TestCase):
    """Test sift_down function that corrects a max-heap with incorrect root."""

    def test_root_needs_to_sink_one_level(self):
        """Root is smaller than children and should sink one level."""
        src = [1, 10, 5, 2, 3]
        sift_down(src, 0, 4)
        # After sift_down, 1 should sink to position 1
        # Children of root are 10 (idx 1) and 5 (idx 2)
        # 10 is larger, so 10 moves to root, 1 goes to idx 1
        self.assertEqual(src[0], 10)
        self.assertIn(1, src)

    def test_root_needs_to_sink_multiple_levels(self):
        """Root is smallest and should sink through multiple levels."""
        src = [1, 10, 9, 5, 3, 8, 7]
        sift_down(src, 0, 6)
        # 1 should sink down until it reaches appropriate position
        # Root should be 10 (the larger child)
        self.assertEqual(src[0], 10)
        # 1 should be somewhere in the heap
        self.assertIn(1, src)

    def test_root_already_satisfies_heap_condition(self):
        """Root is already >= both children, no change needed."""
        src = [10, 5, 8, 2, 3, 6, 4]
        original = src.copy()
        sift_down(src, 0, 6)
        # Heap is already valid, should remain unchanged
        self.assertEqual(src, original)

    def test_root_with_only_left_child(self):
        """Root has only left child."""
        src = [1, 10]
        sift_down(src, 0, 1)
        # 1 should swap with 10
        self.assertEqual(src[0], 10)
        self.assertEqual(src[1], 1)

    def test_root_larger_than_only_left_child(self):
        """Root >= left child (only child exists)."""
        src = [10, 5]
        original = src.copy()
        sift_down(src, 0, 1)
        # No change needed
        self.assertEqual(src, original)

    def test_partial_heap_range(self):
        """Apply sift_down to a partial range within a larger list."""
        src = [1, 10, 5, 2, 3, 100, 200]
        sift_down(src, 0, 4)
        # Only operate on indices 0-4
        # Must not affect indices 5-6
        self.assertEqual(src[5], 100)
        self.assertEqual(src[6], 200)
        # Heap property should hold for 0-4
        self.assertEqual(src[0], 10)

    def test_single_element(self):
        """Single element (no children)."""
        src = [42]
        original = src.copy()
        sift_down(src, 0, 0)
        # No children to process
        self.assertEqual(src, original)

    def test_equal_children(self):
        """When both children are equal, should choose left."""
        src = [1, 5, 5, 2, 3]
        sift_down(src, 0, 4)
        # Should move 5 (from left child) to root
        self.assertEqual(src[0], 5)


class TestHeapSort(unittest.TestCase):
    """Tests for the heap_sort function."""

    def test_base_case(self) -> None:
        """Verify heap_sort produces a correctly sorted result for a random list."""
        src = [random.randint(0, 100) for _ in range(100)]
        self.assertEqual(heap_sort(src), sorted(src))

    def test_empty_list(self) -> None:
        """Verify heap_sort handles an empty list."""
        self.assertEqual(heap_sort([]), [])

    def test_single_element(self) -> None:
        """Verify heap_sort handles a single-element list."""
        self.assertEqual(heap_sort([42]), [42])

    def test_duplicates(self) -> None:
        """Verify heap_sort correctly handles duplicate values."""
        self.assertEqual(heap_sort([3, 1, 3, 2, 1]), [1, 1, 2, 3, 3])


if __name__ == "__main__":
    unittest.main()
