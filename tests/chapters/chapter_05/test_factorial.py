"""Tests for factorial in factorial.py."""

import math

import pytest

from algo.chapters.chapter_05_recursion.factorial import factorial


def test_base_cases() -> None:
    """factorial(0) == 1 and factorial(1) == 1."""
    assert factorial(0) == 1
    assert factorial(1) == 1


def test_known_values() -> None:
    """factorial(5) == 120."""
    assert factorial(5) == 120


def test_matches_math_factorial() -> None:
    """factorial matches math.factorial for n in 0..10."""
    for n in range(11):
        assert factorial(n) == math.factorial(n)


def test_negative_raises() -> None:
    """Negative n raises ValueError."""
    with pytest.raises(ValueError):
        factorial(-1)
