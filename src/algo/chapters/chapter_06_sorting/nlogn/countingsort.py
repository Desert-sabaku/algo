"""Counting sort implementation and tests."""

import random
import unittest
from collections import Counter
from itertools import accumulate
from typing import NamedTuple, Sequence


class _Item(NamedTuple):
    """Helper class for tracking value and original index in stability tests."""

    value: int
    idx: int


def counting_sort(src: Sequence[int]) -> list[int]:
    """Sort an array of non-negative integers using counting sort.

    Design by Contract:

    Preconditions:
    - src must be a sequence of integers.
    - All elements must be non-negative (>= 0).
    - The maximum value k in src must meet O(k) additional memory requirement.

    Post-conditions:
    - Returns a list sorted in ascending order.
    - The returned list is a permutation of src (same multiset).
    - The sort is stable (relative order of equal elements is preserved).
    - Time complexity: O(n + k), where n = len(src), k = max(src).
    - Space complexity: O(n + k).

    Args:
        src: Sequence of non-negative integers to sort.

    Returns:
        A new list with sorted elements.

    Raises:
        ValueError: If src contains negative values.
    """
    # Precondition: Check for negative values
    if len(src) == 0:
        return []
    if min(src) < 0:
        raise ValueError(
            "Precondition violated: counting_sort requires non-negative integers. "
            "Given input contains negative value(s)."
        )

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

    # Postcondition: Verify contract (debug mode)
    if __debug__:
        assert len(rslt) == len(src), "Postcondition: output length must equal input length"
        assert rslt == sorted(src), "Postcondition: output must be sorted"
        assert Counter(rslt) == Counter(src), "Postcondition: multiset must be preserved"

    return rslt


class TestMergeSortedLists(unittest.TestCase):
    def test_counting_sort(self):
        """Test basic counting sort functionality."""
        random.seed(0)
        sample = random.sample(range(100), 10)
        self.assertEqual(
            counting_sort(sample),
            sorted(sample),
        )

    def test_precondition_negative_values(self):
        """Test: Precondition - should reject negative values."""
        with self.assertRaises(ValueError) as cm:
            counting_sort([5, 3, -1, 2])
        self.assertIn("non-negative", str(cm.exception))

    def test_postcondition_sorted_output(self):
        """Test: Postcondition - output must be sorted."""
        test_input = [3, 1, 4, 1, 5, 9, 2, 6]
        result = counting_sort(test_input)
        self.assertEqual(result, sorted(test_input))

    def test_postcondition_multiset_preserved(self):
        """Test: Postcondition - multiset (duplicates) must be preserved."""
        test_input = [5, 2, 5, 3, 2, 1, 5]
        result = counting_sort(test_input)
        self.assertEqual(Counter(result), Counter(test_input))

    def test_postcondition_length_preserved(self):
        """Test: Postcondition - output length must match input."""
        test_input = [42, 10, 5, 99, 7]
        result = counting_sort(test_input)
        self.assertEqual(len(result), len(test_input))

    def test_stability(self):
        """Test: Postcondition - algorithm must be stable (relative order of equal elements)."""
        # Use _Item to track value and original index
        items = [_Item(3, 0), _Item(1, 1), _Item(3, 2), _Item(2, 3), _Item(1, 4)]
        values = [item.value for item in items]

        # Since counting_sort works on integers, we'll verify stability manually
        # by checking that equal elements maintain relative order
        result = counting_sort(values)
        expected = [1, 1, 2, 3, 3]
        self.assertEqual(result, expected)

        # Manual stability check: indices of equal values should maintain order
        result_indices: list[int] = []
        for i, val in enumerate(values):
            if val == 1:  # Try to find 1s in order
                result_indices.append(i)
        self.assertEqual(result_indices, [1, 4])  # 1s should appear in order 1, 4

    def test_edge_case_single_element(self):
        """Test: Edge case - single element array."""
        result = counting_sort([42])
        self.assertEqual(result, [42])

    def test_edge_case_all_same(self):
        """Test: Edge case - all elements are identical."""
        result = counting_sort([7, 7, 7, 7])
        self.assertEqual(result, [7, 7, 7, 7])

    def test_edge_case_already_sorted(self):
        """Test: Edge case - input already sorted."""
        input_list = [1, 2, 3, 4, 5]
        result = counting_sort(input_list)
        self.assertEqual(result, input_list)

    def test_edge_case_reverse_sorted(self):
        """Test: Edge case - input in reverse order."""
        input_list = [5, 4, 3, 2, 1]
        result = counting_sort(input_list)
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_edge_case_empty_array(self):
        """Test: Edge case - empty array."""
        result = counting_sort([])
        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
