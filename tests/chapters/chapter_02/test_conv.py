"""Tests for base conversion in conv.py."""

import pytest

from algo.chapters.chapter_02_complexity_primes.conv import convert_base


def test_binary() -> None:
    """convert_base(10, 2) returns binary string."""
    assert convert_base(10, 2) == "1010"


def test_hex() -> None:
    """convert_base(255, 16) returns hex string."""
    assert convert_base(255, 16) == "FF"


def test_zero() -> None:
    """convert_base(0, any_radix) returns '0'."""
    assert convert_base(0, 10) == "0"
    assert convert_base(0, 2) == "0"


def test_negative() -> None:
    """convert_base with negative number returns '-' prefix."""
    assert convert_base(-8, 2) == "-1000"


def test_decimal() -> None:
    """convert_base in base 10 is identity."""
    assert convert_base(42, 10) == "42"


def test_invalid_radix_low() -> None:
    """Radix below 2 raises ValueError."""
    with pytest.raises(ValueError):
        convert_base(10, 1)


def test_invalid_radix_high() -> None:
    """Radix above 36 raises ValueError."""
    with pytest.raises(ValueError):
        convert_base(10, 37)


def test_round_trip() -> None:
    """int(convert_base(n, r), r) == n for various values."""
    for num in [1, 7, 15, 100, 255, 1023]:
        for radix in [2, 8, 10, 16]:
            assert int(convert_base(num, radix), radix) == num
