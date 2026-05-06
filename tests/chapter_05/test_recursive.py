"""Tests for recursive functions in recursive.py."""

from algo.chapters.chapter_05_recursion.recursive import recursive1, recursive2, recursive3


def _capture(func, n: int, capsys) -> str:  # type: ignore[no-untyped-def]
    """Run func(n) and return captured stdout."""
    func(n)
    return capsys.readouterr().out


def test_all_agree_n0(capsys) -> None:  # type: ignore[no-untyped-def]
    """All three functions print nothing for n=0."""
    out1 = _capture(recursive1, 0, capsys)
    out2 = _capture(recursive2, 0, capsys)
    out3 = _capture(recursive3, 0, capsys)
    assert out1 == out2 == out3


def test_all_agree_n1(capsys) -> None:  # type: ignore[no-untyped-def]
    """All three functions print the same output for n=1."""
    out1 = _capture(recursive1, 1, capsys)
    out2 = _capture(recursive2, 1, capsys)
    out3 = _capture(recursive3, 1, capsys)
    assert out1 == out2 == out3


def test_all_agree_n4(capsys) -> None:  # type: ignore[no-untyped-def]
    """All three functions print the same output for n=4."""
    out1 = _capture(recursive1, 4, capsys)
    out2 = _capture(recursive2, 4, capsys)
    out3 = _capture(recursive3, 4, capsys)
    expected = "1 2 1 3 1 2 1 4 1 2 1 "
    assert out1 == expected
    assert out1 == out2 == out3
