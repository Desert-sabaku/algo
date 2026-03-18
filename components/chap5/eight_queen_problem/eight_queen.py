"""
List all possible arrangements of the queens so that no two queens occupy the same row or column.
"""

from collections.abc import Iterator
from itertools import islice
from typing import Protocol

DEFAULT_COLUMN_COUNT = 8
DEFAULT_DISPLAY_SOLUTION_COUNT = 97


class SolutionRenderer(Protocol):
    """Protocol for rendering a single queen solution."""

    def render(self, solution: list[int]) -> str:
        """Return a string representation for one solution."""
        raise NotImplementedError


class QueenBoardRenderer:
    """Render queen positions as a board string."""

    def __init__(
        self,
        column_count: int,
        queen_symbol: str = "♕",
        empty_symbol: str = "□",
    ) -> None:
        self.column_count = column_count
        self.queen_symbol = queen_symbol
        self.empty_symbol = empty_symbol

    def render(self, solution: list[int]) -> str:
        """Render one solution as a multi-line board."""
        rows: list[str] = []
        for row_index in range(self.column_count):
            row = "".join(
                self.queen_symbol if solution[column_index] == row_index else self.empty_symbol
                for column_index in range(self.column_count)
            )
            rows.append(row)
        return "\n".join(rows)


class EightQueenSolver:
    """Generate solutions for the N-Queens problem."""

    def __init__(self, column_count: int = DEFAULT_COLUMN_COUNT) -> None:
        self.column_count = column_count
        self.diagonal_count = 2 * column_count - 1
        self.total_pattern = column_count**column_count

    def _get_positive_diagonal_index(self, column_index: int, row_index: int) -> int:
        """Return the index for the positive-sloped diagonal (/)."""
        return column_index + row_index

    def _get_negative_diagonal_index(self, column_index: int, row_index: int) -> int:
        """Return the index for the negative-sloped diagonal (\\)."""
        return column_index - row_index + self.column_count - 1

    def _can_place_queen(
        self,
        column_index: int,
        row_index: int,
        is_queen_placed_horizontal: list[bool],
        is_queen_placed_positive_diagonal: list[bool],
        is_queen_placed_negative_diagonal: list[bool],
    ) -> bool:
        """Check whether a queen can be safely placed at the given position."""
        positive_diagonal_index = self._get_positive_diagonal_index(column_index, row_index)
        negative_diagonal_index = self._get_negative_diagonal_index(column_index, row_index)
        return (
            not is_queen_placed_horizontal[row_index]
            and not is_queen_placed_positive_diagonal[positive_diagonal_index]
            and not is_queen_placed_negative_diagonal[negative_diagonal_index]
        )

    def _set_queen_state(
        self,
        column_index: int,
        row_index: int,
        is_placed: bool,
        is_queen_placed_horizontal: list[bool],
        is_queen_placed_positive_diagonal: list[bool],
        is_queen_placed_negative_diagonal: list[bool],
    ) -> None:
        """Mark or unmark occupancy for row and diagonals."""
        positive_diagonal_index = self._get_positive_diagonal_index(column_index, row_index)
        negative_diagonal_index = self._get_negative_diagonal_index(column_index, row_index)
        is_queen_placed_horizontal[row_index] = is_placed
        is_queen_placed_positive_diagonal[positive_diagonal_index] = is_placed
        is_queen_placed_negative_diagonal[negative_diagonal_index] = is_placed

    def _generate_queen_positions(
        self,
        column_index: int,
        position: list[int],
        is_queen_placed_horizontal: list[bool],
        is_queen_placed_positive_diagonal: list[bool],
        is_queen_placed_negative_diagonal: list[bool],
    ) -> Iterator[list[int]]:
        """MAIN LOGIC. Arrange queens recursively starting from the given column."""
        for row_index in range(self.column_count):
            if self._can_place_queen(
                column_index,
                row_index,
                is_queen_placed_horizontal,
                is_queen_placed_positive_diagonal,
                is_queen_placed_negative_diagonal,
            ):
                position[column_index] = row_index
                if column_index != self.column_count - 1:
                    self._set_queen_state(
                        column_index,
                        row_index,
                        True,
                        is_queen_placed_horizontal,
                        is_queen_placed_positive_diagonal,
                        is_queen_placed_negative_diagonal,
                    )
                    yield from self._generate_queen_positions(
                        column_index + 1,
                        position,
                        is_queen_placed_horizontal,
                        is_queen_placed_positive_diagonal,
                        is_queen_placed_negative_diagonal,
                    )
                    self._set_queen_state(
                        column_index,
                        row_index,
                        False,
                        is_queen_placed_horizontal,
                        is_queen_placed_positive_diagonal,
                        is_queen_placed_negative_diagonal,
                    )
                else:
                    yield position.copy()

    def generate_queen_positions(self) -> Iterator[list[int]]:
        """Generate all queen placements for the configured board size."""
        position = [0] * self.column_count
        is_queen_placed_horizontal = [False] * self.column_count
        is_queen_placed_positive_diagonal = [False] * self.diagonal_count
        is_queen_placed_negative_diagonal = [False] * self.diagonal_count
        yield from self._generate_queen_positions(
            0,
            position,
            is_queen_placed_horizontal,
            is_queen_placed_positive_diagonal,
            is_queen_placed_negative_diagonal,
        )


class SolutionPresenter:
    """Present generated solutions without owning solving logic."""

    def __init__(self, solution_renderer: SolutionRenderer) -> None:
        self.solution_renderer = solution_renderer

    def print_first_n_solutions(
        self,
        solutions: Iterator[list[int]],
        solution_count: int,
    ) -> int:
        """Print up to solution_count solutions and return how many were printed."""
        printed_count = 0
        for printed_count, solution in enumerate(islice(solutions, solution_count), start=1):
            print(self.solution_renderer.render(solution))
            print()
        return printed_count


if __name__ == "__main__":
    solver = EightQueenSolver()
    board_renderer = QueenBoardRenderer(solver.column_count)
    presenter = SolutionPresenter(board_renderer)
    shown_count = presenter.print_first_n_solutions(
        solver.generate_queen_positions(),
        DEFAULT_DISPLAY_SOLUTION_COUNT,
    )
    print(f"Displayed {shown_count} solution(s).")
