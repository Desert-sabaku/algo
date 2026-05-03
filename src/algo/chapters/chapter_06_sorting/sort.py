"""Implementations of sorting using various algorithms."""

import bisect
import math
import random
from typing import MutableSequence, Sequence

from algo.chapters.core.supports_less_than import SupportsLT


def bubble_sort[T: SupportsLT](src: Sequence[T]) -> list[T]:
    """Sorting using the straight exchange sort"""
    rslt = list(src)
    for i in range(len(rslt)):
        for j in range(len(rslt) - i - 1):
            if rslt[j] > rslt[j + 1]:
                rslt[j], rslt[j + 1] = rslt[j + 1], rslt[j]
    return rslt


def bubble_sort2[T: SupportsLT](src: Sequence[T]) -> list[T]:
    """Sort using bubble sort with early-exit optimisation.

    Identical to :func:`bubble_sort` but terminates as soon as a full pass
    completes without any swaps, indicating the sequence is already sorted.
    Best-case time complexity is O(n).
    """
    rslt = list(src)
    for i in range(len(rslt)):
        swapped = False
        for j in range(len(rslt) - i - 1):
            if rslt[j] > rslt[j + 1]:
                rslt[j], rslt[j + 1] = rslt[j + 1], rslt[j]
                swapped = True
        if not swapped:
            return rslt
    return rslt


def bubble_sort3[T: SupportsLT](src: Sequence[T]) -> list[T]:
    """Sort using bubble sort that tracks the last-swap boundary.

    After each pass, the next pass ends at the index of the last swap rather
    than shrinking the boundary by exactly one.  This can skip large already-
    sorted suffixes and reduces the number of comparisons in practice.
    """
    rslt = list(src)
    end_index = len(rslt) - 1

    while end_index > 0:
        last_swap_index = 0
        for j in range(end_index):
            if rslt[j] > rslt[j + 1]:
                rslt[j], rslt[j + 1] = rslt[j + 1], rslt[j]
                last_swap_index = j
        end_index = last_swap_index

    return rslt


def shaker_sort[T: SupportsLT](src: Sequence[T]) -> list[T]:
    """Sorting using the bi-direction bubble sort."""
    rslt = list(src)
    left, right = 0, len(src) - 1

    last = right
    while left < right:
        for i in range(right, left, -1):
            if rslt[i - 1] > rslt[i]:
                rslt[i - 1], rslt[i] = rslt[i], rslt[i - 1]
                last = i
        left = last

        for i in range(left, right):
            if rslt[i] > rslt[i + 1]:
                rslt[i], rslt[i + 1] = rslt[i + 1], rslt[i]
                last = i
        right = last

    return rslt


def selection_sort[T: SupportsLT](src: Sequence[T]) -> list[T]:
    """Sorting using the straight selection sort."""
    rslt = list(src)
    for i in range(len(rslt) - 1):
        m = i
        # 最小の値を探す
        for j in range(i + 1, len(rslt)):
            if rslt[j] < rslt[m]:
                m = j
        rslt[i], rslt[m] = rslt[m], rslt[i]

    return rslt


def shuttle_sort[T: SupportsLT](
    src: MutableSequence[T],
    left: int = 0,
    right: int | None = None,
    is_inplace: bool = False,
) -> MutableSequence[T]:
    """Sorting using the straight insertion sort."""
    rslt = src if is_inplace else list(src)
    if right is None:
        right = len(rslt) - 1

    for i in range(left + 1, right + 1):
        insert_value = rslt[i]

        # right shift
        j = i
        while j > left and insert_value < rslt[j - 1]:
            rslt[j] = rslt[j - 1]
            j -= 1
        rslt[j] = insert_value

    return rslt


def binary_insertion_sort[T: SupportsLT](src: Sequence[T]) -> list[T]:
    """Sorting using the binary insertion sort."""
    rslt = list(src)
    for i in range(1, len(rslt)):
        key = rslt[i]
        left, right = 0, i

        # 目的列はソート済みなので二分探索が可能
        # 範囲は [left, right)
        while left < right:
            middle = (left + right) // 2
            if key < rslt[middle]:
                right = middle
            else:
                left = middle + 1

        insert_position = left

        # right shift
        for j in range(i, insert_position, -1):
            rslt[j] = rslt[j - 1]
        rslt[insert_position] = key

    return rslt


def binary_insertion_sort2[T: SupportsLT](
    src: Sequence[T],
) -> list[T]:
    """Sorting using the binary insertion sort."""
    rslt = list(src)
    for i in range(1, len(rslt)):
        bisect.insort(rslt, rslt.pop(i), 0, i)
    return rslt


def shell_sort[T: SupportsLT](src: Sequence[T]) -> list[T]:
    """Sorting using the shell sort."""
    rslt = list(src)
    h = len(rslt) // 2

    while h > 0:
        # 配列の後半に注目する
        for i in range(h, len(rslt)):
            # 基準となる添え字の相対的な距離から前半の添え字を算出
            j = i - h

            # ここ大体挿入ソートと一緒
            insert_value = rslt[i]
            while j >= 0 and rslt[j] > insert_value:
                rslt[j + h] = rslt[j]
                j -= h
            rslt[j + h] = insert_value

        h //= 2
    return rslt


def shell_sort2[T: SupportsLT](src: Sequence[T]) -> list[T]:
    """Sort using Shell sort with the Knuth gap sequence.

    Uses the gap sequence h = (3^k − 1) / 2  (i.e. 1, 4, 13, 40, 121, …),
    which Knuth showed gives O(n^(3/2)) comparisons.  Because consecutive gaps
    are never multiples of each other the elements are well-shuffled between
    passes, making this variant faster than the halving-gap variant
    (:func:`shell_sort`) in practice.
    """
    rslt = list(src)
    if len(rslt) < 2:  # noqa: PLR2004
        return rslt
    h = (3 ** math.floor(math.log(2 * len(rslt) - 1, 3)) - 1) // 2

    while h > 0:
        for i in range(h, len(rslt)):
            j = i - h
            insert_value = rslt[i]
            while j >= 0 and rslt[j] > insert_value:
                rslt[j + h] = rslt[j]
                j -= h
            rslt[j + h] = insert_value
        h //= 3

    return rslt


if __name__ == "__main__":
    print(test := [random.randint(0, 60) for _ in range(30)])

    # print(bubble_sort(test))
    # print(bubble_sort2(test))
    # print(bubble_sort3(test))
    # print(shaker_sort(test))
    # print(selection_sort(test))
    # print(shuttle_sort(test, 0, len(test) - 1))
    # print(test)
    # print(binary_insertion_sort(test))
    # print(shell_sort(test))
    # print(shell_sort2(test))
    # partition_using_qsort(test)
    # print(quick_sort2(test, 0, len(test) - 1))
    # print(merge_sort(test) == sorted(test))
