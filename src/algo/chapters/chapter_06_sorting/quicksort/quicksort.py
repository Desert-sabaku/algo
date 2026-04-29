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
