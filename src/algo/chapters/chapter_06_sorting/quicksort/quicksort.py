import random
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


def quick_sort2[T: SupportsLT](src: Sequence[T], start: int, end: int) -> list[T]:
    rslt = list(src)

    def helper(src: list[T], left: int, right: int) -> T:
        """Implementation of the median-of-three sort.
        The pivot is placed at position `right-1`.
        After partitioning the array, it is the caller's responsibility to return this pivot to its correct position.

        Args:
            src (list[T]): Input array
            left (int): The index at the start of the array
            right (int): The index at the end of the array

        Returns:
            T: The pivot
        """
        # left, mid, right の3箇所をソート
        mid = left + (right - left) // 2

        if src[left] > src[mid]:
            src[left], src[mid] = src[mid], src[left]
        if src[left] > src[right]:
            src[left], src[right] = src[right], src[left]
        if src[mid] > src[right]:
            src[mid], src[right] = src[right], src[mid]

        # left, ..., mid, right
        # mid で必ず止まる。番兵として機能する。
        src[mid], src[right - 1] = src[right - 1], src[mid]
        return src[right - 1]

    stack = [(start, end)]

    while stack:
        left, right = stack.pop()

        # --- 三値の中央値の選択と配置 ---
        pivot = helper(rslt, left, right)

        # 走査範囲は left + 1 から right - 2
        pl = left + 1
        pr = right - 2

        # --- 分割 ---
        while True:
            # rslt[left] が pivot_val 以下のため、pl は必ず止まる（番兵）
            while rslt[pl] < pivot:
                pl += 1
            # rslt[right] が pivot_val 以上のため、pr は必ず止まる（番兵）
            while pivot < rslt[pr]:
                pr -= 1

            if pl >= pr:
                break
            rslt[pl], rslt[pr] = rslt[pr], rslt[pl]
            pl += 1
            pr -= 1

        # ピボットを正しい位置（pl）に戻す
        rslt[pl], rslt[right - 1] = rslt[right - 1], rslt[pl]

        # 分割後の範囲をスタックへ
        if left < pl - 1:
            stack.append((left, pl - 1))
        if pl + 1 < right:
            stack.append((pl + 1, right))

    return rslt


if __name__ == "__main__":
    seq = [random.randint(0, 100) for _ in range(10)]
    print(quick_sort2(seq, 0, len(seq) - 1))
