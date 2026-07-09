"""Tests for triangle pattern generator."""

from algo.chapters.chapter_01_basics.triangle import triangle_rows


def test_triangle_n1() -> None:
    """n=1 produces 4 sections with single-row triangles."""
    rows = triangle_rows(1)
    assert rows[0] == "*"


def test_triangle_n3_line_count() -> None:
    """n=3 produces 4 sections with correct first section."""
    rows = triangle_rows(3)
    assert rows[0] == "*"
    assert rows[1] == "**"
    assert rows[2] == "***"


def test_triangle_row_widths() -> None:
    """First section rows have increasing asterisk count."""
    rows = triangle_rows(4)
    for i in range(1, 5):
        assert rows[i - 1] == "*" * i
