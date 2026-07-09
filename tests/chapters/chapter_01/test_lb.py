"""Tests for asterisk line pattern function."""

import pytest

from algo.chapters.chapter_01_basics.lb import asterisk_lines


def test_exact_multiple() -> None:
    """6 asterisks, 3 per line -> 2 full lines."""
    result = asterisk_lines(6, 3)
    assert result == ["***", "***"]


def test_with_remainder() -> None:
    """7 asterisks, 3 per line -> 2 full + 1 partial."""
    result = asterisk_lines(7, 3)
    assert result == ["***", "***", "*"]


def test_zero_asterisks() -> None:
    """0 asterisks -> empty list."""
    assert asterisk_lines(0, 3) == []


def test_invalid_words_raises() -> None:
    """words <= 0 raises ValueError."""
    with pytest.raises(ValueError):
        asterisk_lines(5, 0)
