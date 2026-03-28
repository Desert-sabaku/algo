"""Implementations of sorting using various algorithms."""

import cProfile
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


if __name__ == "__main__":
    print(test := [random.randint(0, 10) for _ in range(1000)])

    cProfile.run("bubble_sort(test)")
