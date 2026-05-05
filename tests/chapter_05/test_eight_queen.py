"""Tests for the eight-queens solver."""

from algo.chapters.chapter_05_recursion.eight_queen_problem.eight_queen import (
    EightQueenSolver,
    PlacementState,
    QueenBoardRenderer,
)


def test_eight_queens_solution_count() -> None:
    """8x8 board produces exactly 92 solutions."""
    solver = EightQueenSolver(8)
    solutions = list(solver.generate_solutions())
    assert len(solutions) == 92


def test_four_queens_solution_count() -> None:
    """4x4 board produces exactly 2 solutions."""
    solver = EightQueenSolver(4)
    solutions = list(solver.generate_solutions())
    assert len(solutions) == 2


def test_solutions_have_correct_length() -> None:
    """Each solution has one entry per column."""
    solver = EightQueenSolver(5)
    for solution in solver.generate_solutions():
        assert len(solution) == 5


def test_solutions_no_duplicate_rows() -> None:
    """Each solution has unique row values (no two queens in same row)."""
    solver = EightQueenSolver(6)
    for solution in solver.generate_solutions():
        assert len(set(solution)) == 6


def test_solutions_no_diagonal_conflicts() -> None:
    """Each solution has no diagonal conflicts."""
    solver = EightQueenSolver(6)
    for solution in solver.generate_solutions():
        for col_a, row_a in enumerate(solution):
            for col_b, row_b in enumerate(solution):
                if col_a != col_b:
                    assert abs(col_a - col_b) != abs(row_a - row_b)


def test_placement_state_round_trip() -> None:
    """place then remove leaves state unchanged."""
    state = PlacementState(8)
    before_rows = state.occupied_rows.copy()
    state.place(0, 0)
    state.remove(0, 0)
    assert state.occupied_rows == before_rows
    assert state.queen_rows_by_column[0] == -1


def test_renderer_queen_count() -> None:
    """Rendered board contains exactly board_size queen symbols."""
    solver = EightQueenSolver(8)
    renderer = QueenBoardRenderer(8)
    solution = next(solver.generate_solutions())
    board = renderer.render(solution)
    assert board.count("♕") == 8
