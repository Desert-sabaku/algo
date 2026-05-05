"""Tests for queen bounding (brute force with row/column uniqueness)."""

from algo.chapters.chapter_05_recursion.eight_queen_problem.bounding import set_all_positions


def test_eight_columns_count() -> None:
    """8-column bounding arrangement has 8! = 40320 solutions."""
    results = set_all_positions(8)
    assert len(results) == 40320


def test_four_columns_count() -> None:
    """4-column has 4! = 24 solutions."""
    results = set_all_positions(4)
    assert len(results) == 24


def test_solutions_have_no_duplicate_rows() -> None:
    """Each position uses each row index exactly once."""
    for pos in set_all_positions(4):
        assert len(set(pos)) == 4
