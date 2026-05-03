"""Counting sort implementation and tests."""

import unittest
from itertools import accumulate
from typing import Sequence


def counting_sort(src: Sequence[int]) -> list[int]:
    """Sort an array of non-negative integers using counting sort.

    Args:
        src (Sequence[int]): Sequence of non-negative integers to sort.

    Returns:
        list[int]: A new list with sorted elements.

    Raises:
        ValueError: If any element is negative.
    """

    if not src:
        return []
    if min(src) < 0:
        raise ValueError("counting sort requires non-negative integers.")

    table = [0] * (max(src) + 1)
    rslt = [0] * len(src)

    # step 1: 度数分布表
    for e in src:
        table[e] += 1
    # step 2: 累積度数分布表
    table = list(accumulate(table))
    # step 3: 解配列への配置
    for e in reversed(src):
        table[e] -= 1
        rslt[table[e]] = e

    return rslt


class TestCountingSort(unittest.TestCase):
    """Test for counting sort"""

    def test_counting_sort(self):
        """Verify counting_sort produces a correctly sorted result."""
        src = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
        self.assertEqual(counting_sort(src), sorted(src))


if __name__ == "__main__":
    unittest.main()
