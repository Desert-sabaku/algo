"""Tests for memoized recursive function."""

from algo.chapters.chapter_05_recursion.memoization import recursive


def test_memoization_n0(capsys) -> None:  # type: ignore[no-untyped-def]
    """recursive(0) prints nothing."""
    recursive(0)
    assert capsys.readouterr().out == ""


def test_memoization_fresh_state(capsys) -> None:  # type: ignore[no-untyped-def]
    """Each call with default memo starts fresh (no cross-test pollution)."""
    recursive(4)
    out1 = capsys.readouterr().out
    recursive(4)
    out2 = capsys.readouterr().out
    assert out1 == out2
