"""Binary search implementation with profiling."""

import cProfile
import random
from typing import Sequence, TypeVar

from algo.chapters.core.supports_less_than import SupportsLT

T = TypeVar("T", bound=SupportsLT)

# 二分探索を実装する場合、不等号を実装している型のみが対象になる。
# したがって引数は、不等号を実装している型に縛る。
# ところで型を縛るとき、なるべく緩く縛るのが良しとされているため
# ここでは「大なりが実装されているか」で縛り、
# 小なりに関しては両辺を入れ替えることで対応する。
# 一般に、型の縛り方は第一に「厳密」第二に「自由」である。


def binary_search(seq: Sequence[T], key: T) -> int | None:
    """Return the index of key in a sorted sequence using binary search."""
    left, right = 0, len(seq) - 1
    while left <= right:
        mid = (left + right) // 2
        x = seq[mid]
        if x < key:
            left = mid + 1
        elif key < x:  # __gt__ 不要
            right = mid - 1
        else:
            return mid
    return None


if __name__ == "__main__":
    src = sorted([random.gauss() for _ in range(10000)])
    cProfile.run("binary_search(src, random.choice(src))")
