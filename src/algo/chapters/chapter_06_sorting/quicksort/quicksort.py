import random
from copy import deepcopy
from typing import Sequence

from algo.chapters.core.supports_less_than import SupportsLT


def partition_using_qsort[T: SupportsLT](src: list[T]) -> None:
    """
    This function demonstrates the partitioning process of quicksort.
    It does not sort the list, but rather shows how the list is partitioned around a pivot.

    There are two methods of performing the partitioning:
    - Lomuto Partition Scheme
    - Hoare Partition Scheme

    This function uses the Hoare Partition Scheme, which is more efficient and does not require additional space for a temporary array.
    """
    left = 0
    right = len(src) - 1
    pivot = src[len(src) // 2]

    while left <= right:
        # このwhileループは、src[left] >= pivot となるまで left を進める
        while src[left] < pivot:
            left += 1
        while pivot < src[right]:
            right -= 1
        if left <= right:
            src[left], src[right] = src[right], src[left]
            left += 1
            right -= 1

    print(src)
    print("A pivot: ", pivot)
    print("A group with values equal to or less than the pivot: ", src[:left])

    if left > right + 1:
        print("A group matching the pivot value: ", src[right + 1 : left])

    print("A group with values equal to or greater than the pivot: ", src[right + 1 :])


def quick_sort_impl[T: SupportsLT](src: list[T], left: int, right: int) -> None:
    pl, pr = left, right
    pivot = src[(left + right) // 2]

    while pl <= pr:
        while src[pl] < pivot:
            pl += 1
        while pivot < src[pr]:
            pr -= 1
        if pl <= pr:
            src[pl], src[pr] = src[pr], src[pl]
            pl += 1
            pr -= 1

    # 終了条件
    if left < pr:
        quick_sort_impl(src, left, pl)
    if pl < right:
        quick_sort_impl(src, pl, right)


def quick_sort[T: SupportsLT](src: Sequence[T]) -> list[T]:
    rslt = list(src)
    quick_sort_impl(rslt, 0, len(rslt) - 1)
    return rslt


