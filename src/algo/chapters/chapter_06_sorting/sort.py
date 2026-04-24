"""Implementations of sorting using various algorithms."""

import bisect
import random
import math
from copy import deepcopy
from typing import Sequence

from algo.chapters.core.supports_less_than import SupportsLT


def bubble_sort[T: SupportsLT](seq: Sequence[T]) -> list[T]:
    """Sorting using the straight exchange sort"""
    cp = list(deepcopy(seq))
    for i in range(len(cp)):
        for j in range(len(cp) - i - 1):
            if cp[j] > cp[j + 1]:
                cp[j], cp[j + 1] = cp[j + 1], cp[j]
    return cp


def bubble_sort2[T: SupportsLT](seq: Sequence[T]) -> list[T]:
    """Sorting using the straight exchange sort"""
    cp = list(deepcopy(seq))
    for i in range(len(cp)):
        swaped = False
        for j in range(len(cp) - i - 1):
            if cp[j] > cp[j + 1]:
                cp[j], cp[j + 1] = cp[j + 1], cp[j]
                swaped = True
        if not swaped:
            return cp
    return cp


def bubble_sort3[T: SupportsLT](seq: Sequence[T]) -> list[T]:
    """Sorting using the straight exchange sort."""
    cp = list(deepcopy(seq))
    end_index = len(cp) - 1

    while end_index > 0:
        last_swap_index = 0
        for j in range(end_index):
            if cp[j] > cp[j + 1]:
                cp[j], cp[j + 1] = cp[j + 1], cp[j]
                last_swap_index = j
        end_index = last_swap_index

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
    cp = list(deepcopy(seq))
    for i in range(len(cp) - 1):
        m = i
        # 最小の値を探す
        for j in range(i + 1, len(cp)):
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
    h = len(cp) // 2

    while h > 0:
        # 配列の後半に注目する
        for i in range(h, len(cp)):
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


def shell_sort2[T: SupportsLT](seq: Sequence[T]) -> list[T]:
    """Sorting using the shell sort."""
    # 間隔を、121, 40, 13, 4, 1のように減らしていく。
    # 間隔が互いに倍数とならないようにすれば、要素が十分にかき混ぜられ、効率化が期待できる。
    cp = list(deepcopy(seq))
    h = (3 ** math.floor(math.log(2 * len(cp) - 1, 3)) - 1) // 2

    while h > 0:
        for i in range(h, len(cp)):
            j = i - h
            insert_value = cp[i]
            while j >= 0 and cp[j] > insert_value:
                cp[j + h] = cp[j]
                j -= h
            cp[j + h] = insert_value
        h //= 3

    return cp


if __name__ == "__main__":
    print(test := [random.randint(0, 10) for _ in range(10)])

    # print(bubble_sort(test))
    # print(bubble_sort2(test))
    # print(bubble_sort3(test))
    # print(shaker_sort(test))
    # print(selection_sort(test))
    # print(shuttle_sort(test))
    # print(binary_insertion_sort(test))
    print(shell_sort(test))
    print(shell_sort2(test))
