"""Implementations of sorting using various algorithms."""

import bisect
import random
from copy import deepcopy
from typing import Sequence

from algo.chapters.core.supports_less_than import SupportsLT


def bubble_sort[T: SupportsLT](seq: Sequence[T]) -> list[T]:
    """Sorting using the straight exchange sort"""
    right = len(seq) - 1
    cp = list(deepcopy(seq))
    for i in range(right):
        for j in range(right, i, -1):
            if cp[j - 1] > cp[j]:
                cp[j - 1], cp[j] = cp[j], cp[j - 1]
    return cp


def bubble_sort2[T: SupportsLT](seq: Sequence[T]) -> list[T]:
    """Sorting using the straight exchange sort"""
    length = len(seq)
    cp = list(deepcopy(seq))
    for i in range(length - 1):
        exchange_count = 0
        for j in range(length - 1, i, -1):
            if cp[j - 1] > cp[j]:
                cp[j - 1], cp[j] = cp[j], cp[j - 1]
                exchange_count += 1
        if exchange_count == 0:
            return cp
    return cp


def bubble_sort3[T: SupportsLT](seq: Sequence[T]) -> list[T]:
    """Sorting using the straight exchange sort."""
    cp = list(deepcopy(seq))
    left = 0
    right = len(seq) - 1
    while left < right:
        last_swap_index = right
        for i in range(right, left, -1):
            if cp[i - 1] > cp[i]:
                cp[i - 1], cp[i] = cp[i], cp[i - 1]
                last_swap_index = i
        left = last_swap_index
    return cp


def shaker_sort[T: SupportsLT](seq: Sequence[T]) -> list[T]:
    """Sorting using the bi-direction bubble sort."""
    cp = list(deepcopy(seq))
    left = 0
    right = len(seq) - 1
    last = right
    while left < right:
        for i in range(right, left, -1):
            if cp[i - 1] > cp[i]:
                cp[i - 1], cp[i] = cp[i], cp[i - 1]
                last = i
        left = last

        for i in range(left, right):
            if cp[i] > cp[i + 1]:
                cp[i], cp[i + 1] = cp[i + 1], cp[i]
                last = i
        right = last

    return cp


def selection_sort[T: SupportsLT](seq: Sequence[T]) -> list[T]:
    """Sorting using the straight selection sort."""
    length = len(seq)
    cp = list(deepcopy(seq))
    for i in range(length - 1):
        m = i
        # 最小の値を探す
        for j in range(i + 1, length):
            if cp[j] < cp[m]:
                m = j
        cp[i], cp[m] = cp[m], cp[i]

    return cp


def shuttle_sort[T: SupportsLT](seq: Sequence[T]) -> list[T]:
    """Sorting using the straight insertion sort."""
    cp = list(deepcopy(seq))
    for i in range(1, len(cp)):
        insert_value = cp[i]

        # right shift
        j = i
        while j > 0 and insert_value < cp[j - 1]:
            cp[j] = cp[j - 1]
            j -= 1
        cp[j] = insert_value

    return cp


def binary_insertion_sort[T: SupportsLT](seq: Sequence[T]) -> list[T]:
    """Sorting using the binary insertion sort."""
    cp = list(deepcopy(seq))
    for i in range(1, len(cp)):
        key = cp[i]
        left, right = 0, i

        # 目的列はソート済みなので二分探索が可能
        # 範囲は [left, right)
        while left < right:
            middle = (left + right) // 2
            if key < cp[middle]:
                right = middle
            else:
                left = middle + 1

        insert_position = left

        # right shift
        for j in range(i, insert_position, -1):
            cp[j] = cp[j - 1]
        cp[insert_position] = key

    return cp


def binary_insertion_sort2[T: SupportsLT](
    seq: Sequence[T],
) -> list[T]:
    """Sorting using the binary insertion sort."""
    cp = list(deepcopy(seq))
    for i in range(1, len(cp)):
        bisect.insort(cp, cp.pop(i), 0, i)
    return cp


def shell_sort[T: SupportsLT](seq: Sequence[T]) -> list[T]:
    """Sorting using the shell sort."""
    cp = list(deepcopy(seq))
    length = len(cp)
    h = length // 2

    while h > 0:
        # 配列の後半に注目する
        for i in range(h, length):
            # 基準となる添え字の相対的な距離から前半の添え字を算出
            j = i - h

            # ここ大体挿入ソートと一緒
            insert_value = cp[i]
            while j >= 0 and cp[j] > insert_value:
                cp[j + h] = cp[j]
                j -= h
            cp[j + h] = insert_value

        h //= 2
    return cp


if __name__ == "__main__":
    print(test := [random.randint(0, 10) for _ in range(5)])

    # print(bubble_sort(test))
    # print(bubble_sort2(test))
    # print(bubble_sort3(test))
    # print(shaker_sort(test))
    # print(selection_sort(test))
    # print(shuttle_sort(test))
    # print(binary_insertion_sort(test))
    print(shell_sort(test))
