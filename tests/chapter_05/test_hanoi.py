"""Tests for Tower of Hanoi move function."""

import pytest

from algo.chapters.chapter_05_recursion.hanoi import move


def test_two_disks_move_count() -> None:
    """2 disks require exactly 3 moves."""
    result = move(2, 1, 3)
    assert len(result) == 3


def test_three_disks_move_count() -> None:
    """3 disks require exactly 7 moves (2^3 - 1)."""
    result = move(3, 1, 3)
    assert len(result) == 7


def test_n_disks_move_count() -> None:
    """n disks require exactly 2^n - 1 moves."""
    for n in range(2, 8):
        result = move(n, 1, 3)
        assert len(result) == 2**n - 1


def test_two_disks_sequence() -> None:
    """2-disk Hanoi from axis 1 to 3 follows correct move sequence."""
    result = move(2, 1, 3)
    # disk 1: 1->2, disk 2: 1->3, disk 1: 2->3
    assert result[0]["src"] == 1 and result[0]["dst"] == 2
    assert result[1]["src"] == 1 and result[1]["dst"] == 3
    assert result[2]["src"] == 2 and result[2]["dst"] == 3


def test_disk_count_one_raises() -> None:
    """disk_count=1 raises ValueError (due to <=1 guard)."""
    with pytest.raises(ValueError):
        move(1, 1, 3)


def test_disk_count_zero_raises() -> None:
    """disk_count=0 raises ValueError."""
    with pytest.raises(ValueError):
        move(0, 1, 3)


def test_same_axis_raises() -> None:
    """src and dst being the same axis raises ValueError."""
    with pytest.raises(ValueError):
        move(3, 1, 1)


def test_invalid_axis_raises() -> None:
    """Axis values outside {1,2,3} raise ValueError."""
    with pytest.raises(ValueError):
        move(3, 0, 3)
    with pytest.raises(ValueError):
        move(3, 1, 4)
