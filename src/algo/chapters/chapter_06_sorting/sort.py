"""Implementations of sorting using various algorithms."""

import random
from copy import deepcopy
from typing import MutableSequence

from algo.chapters.core.supports_less_than import SupportsLT


def bubble_sort[T: SupportsLT](seq: MutableSequence[T]) -> MutableSequence[T]:
    """Sorting using the straight exchange sort"""
    right = len(seq) - 1
    cp = deepcopy(seq)
    for i in range(right):
        for j in range(right, i, -1):
            if cp[j - 1] > cp[j]:
                cp[j - 1], cp[j] = cp[j], cp[j - 1]
    return cp


def bubble_sort2[T: SupportsLT](seq: MutableSequence[T]) -> MutableSequence[T]:
    """Sorting using the straight exchange sort"""
    length = len(seq)
    cp = deepcopy(seq)
    for i in range(length - 1):
        exchange_count = 0
        for j in range(length - 1, i, -1):
            if cp[j - 1] > cp[j]:
                cp[j - 1], cp[j] = cp[j], cp[j - 1]
                exchange_count += 1
        if exchange_count == 0:
            return cp
    return cp


def bubble_sort3[T: SupportsLT](seq: MutableSequence[T]) -> MutableSequence[T]:
    """Sorting using the straight exchange sort."""
    cp = deepcopy(seq)
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


def shaker_sort[T: SupportsLT](seq: MutableSequence[T]) -> MutableSequence[T]:
    """Sorting using the bi-direction bubble sort."""
    cp = deepcopy(seq)
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


def selection_sort[T: SupportsLT](seq: MutableSequence[T]) -> MutableSequence[T]:
    """Sorting using the bi-direction bubble sort."""
    length = len(seq)
    cp = deepcopy(seq)
    for i in range(length - 1):
        m = i
        # 最小の値を探す
        for j in range(i + 1, length):
            if cp[j] < cp[m]:
                m = j
        cp[i], cp[m] = cp[m], cp[i]

    return cp


if __name__ == "__main__":
    print(test := [random.randint(0, 100) for _ in range(20)])

    print(bubble_sort(test))
    print(bubble_sort2(test))
    print(bubble_sort3(test))
    print(shaker_sort(test))
    print(selection_sort(test))
