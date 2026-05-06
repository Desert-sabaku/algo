"""Tests for cumulative_sum function."""

from algo.chapters.chapter_01_basics.total1 import cumulative_sum


def test_sum_1_to_5() -> None:
    """Sum from 1 to 5 is 15."""
    assert cumulative_sum(1, 5) == 15


def test_sum_reversed_args() -> None:
    """Arguments in wrong order are auto-corrected."""
    assert cumulative_sum(5, 1) == cumulative_sum(1, 5)


def test_sum_same_args() -> None:
    """Sum of a single value is that value."""
    assert cumulative_sum(3, 3) == 3


def test_sum_zero_range() -> None:
    """Sum from 0 to 0 is 0."""
    assert cumulative_sum(0, 0) == 0
