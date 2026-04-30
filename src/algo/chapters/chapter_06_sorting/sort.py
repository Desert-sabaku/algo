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
    """Sorting using the straight exchange sort"""
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
    """Sorting using the straight exchange sort."""
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
    """Sorting using the shell sort."""
    # 間隔を、121, 40, 13, 4, 1のように減らしていく。
    # 間隔が互いに倍数とならないようにすれば、要素が十分にかき混ぜられ、効率化が期待できる。
    rslt = list(src)
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


def merge_sort_impl[T: SupportsLT](src: list[T], left: int, right: int) -> None:
    if left >= right:
        return

    middle = (left + right) // 2
    merge_sort_impl(src, left, middle)
    merge_sort_impl(src, middle + 1, right)

    # --- マージ ---
    i, j = left, middle + 1
    tmp: list[T] = []

    while i <= middle and j <= right:
        if src[i] < src[j]:
            tmp.append(src[i])
            i += 1
        else:
            tmp.append(src[j])
            j += 1

    while i <= middle:
        tmp.append(src[i])
        i += 1

    while j <= right:
        tmp.append(src[j])
        j += 1

    # ソートされた部分を src にコピー
    for k in range(len(tmp)):
        src[left + k] = tmp[k]

    while pl <= pr:
        while src[pl] < pivot:
            pl += 1
        while pivot < src[pr]:
            pr -= 1
        if pl <= pr:
            src[pl], src[pr] = src[pr], src[pl]
            pl += 1
            pr -= 1

    if left < pr:
        quick_sort_impl(src, left, pl)
    if pl < right:
        quick_sort_impl(src, pl, right)


def quick_sort[T: SupportsLT](src: Sequence[T]) -> list[T]:
    rslt = list(deepcopy(src))
    quick_sort_impl(rslt, 0, len(rslt) - 1)
    return rslt


def quick_sort2[T: SupportsLT](src: Sequence[T], start: int, end: int) -> list[T]:
    rslt = list(deepcopy(src))
    if end <= start:
        return rslt
    # if end - start < 9:
    #    return selection_sort(rslt[start : end + 1])

    def helper(src: list[T], left: int, mid: int, right: int) -> None:
        # left, mid, right の3箇所をソート
        if src[left] > src[mid]:
            src[left], src[mid] = src[mid], src[left]
        if src[left] > src[right]:
            src[left], src[right] = src[right], src[left]
        if src[mid] > src[right]:
            src[mid], src[right] = src[right], src[mid]

    stack = [(start, end)]

    while stack:
        left, right = stack.pop()

        # --- 三値の中央値の選択と配置 ---
        mid = (left + right) // 2
        helper(rslt, left, mid, right)

        # この時点で rslt[left] <= rslt[mid] <= rslt[right]
        # ピボット（中央値）を right - 1 へ退避
        pivot = rslt[mid]
        rslt[mid], rslt[right - 1] = rslt[right - 1], rslt[mid]

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
