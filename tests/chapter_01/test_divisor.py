"""Tests for divisors function."""

import pytest

from algo.chapters.chapter_01_basics.divisor import divisors


def test_divisors_12() -> None:
    """divisors(12) returns all factor pairs."""
    result = divisors(12)
    assert (1, 12) in result
    assert (2, 6) in result
    assert (3, 4) in result


def test_divisors_1() -> None:
    """divisors(1) returns [(1, 1)]."""
    assert divisors(1) == [(1, 1)]


def test_divisors_prime() -> None:
    """divisors of a prime returns [(1, prime)]."""
    assert divisors(7) == [(1, 7)]


def test_divisors_nonpositive_raises() -> None:
    """Non-positive area raises ValueError."""
    with pytest.raises(ValueError):
        divisors(0)
    with pytest.raises(ValueError):
        divisors(-1)
