"""
List all possible arrangements of the queens so that no two queens occupy the same row or column.
"""

from collections.abc import Iterator
from dataclasses import dataclass, field
from itertools import islice
from typing import Protocol

DEFAULT_COLUMN_COUNT = 8
DEFAULT_DISPLAY_SOLUTION_COUNT = 97


class SolutionRenderer(Protocol):  # pylint: disable=too-few-public-methods
    """Protocol for rendering a single queen solution."""

    def render(self, solution: list[int]) -> str:
        """Return a string representation for one solution."""
        raise NotImplementedError


class QueenBoardRenderer:  # pylint: disable=too-few-public-methods
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


@dataclass
class PlacementState:
    """Track queen placement constraints."""

    column_count: int
    diagonal_count: int
    position: list[int] = field(init=False)
    horizontal: list[bool] = field(init=False)
    positive_diagonal: list[bool] = field(init=False)
    negative_diagonal: list[bool] = field(init=False)

    def __post_init__(self) -> None:
        self.position = [0] * self.column_count
        self.horizontal = [False] * self.column_count
        self.positive_diagonal = [False] * self.diagonal_count
        self.negative_diagonal = [False] * self.diagonal_count

    def get_positive_diagonal_index(self, column_index: int, row_index: int) -> int:
        """Return the index for the positive-sloped diagonal (/)."""
        return column_index + row_index

    def get_negative_diagonal_index(self, column_index: int, row_index: int) -> int:
        """Return the index for the negative-sloped diagonal (\\)."""
        return column_index - row_index + self.column_count - 1

    def can_place_queen(self, column_index: int, row_index: int) -> bool:
        """Check whether a queen can be safely placed at the given position."""
        positive_diagonal_index = self.get_positive_diagonal_index(column_index, row_index)
        negative_diagonal_index = self.get_negative_diagonal_index(column_index, row_index)
        return (
            not self.horizontal[row_index]
            and not self.positive_diagonal[positive_diagonal_index]
            and not self.negative_diagonal[negative_diagonal_index]
        )

    def set_queen_state(self, column_index: int, row_index: int, is_placed: bool) -> None:
        """Mark or unmark occupancy for row and diagonals."""
        positive_diagonal_index = self.get_positive_diagonal_index(column_index, row_index)
        negative_diagonal_index = self.get_negative_diagonal_index(column_index, row_index)
        self.horizontal[row_index] = is_placed
        self.positive_diagonal[positive_diagonal_index] = is_placed
        self.negative_diagonal[negative_diagonal_index] = is_placed


class EightQueenSolver:  # pylint: disable=too-few-public-methods
    """Generate solutions for the N-Queens problem."""

    def __init__(self, column_count: int = DEFAULT_COLUMN_COUNT) -> None:
        self.column_count = column_count
        self.diagonal_count = 2 * column_count - 1
        self.total_pattern = column_count**column_count

    def _generate_queen_positions(
        self,
        column_index: int,
        state: PlacementState,
    ) -> Iterator[list[int]]:
        """Arrange queens recursively starting from the given column."""
        for row_index in range(self.column_count):
            if state.can_place_queen(column_index, row_index):
                state.position[column_index] = row_index
                if column_index != self.column_count - 1:
                    state.set_queen_state(column_index, row_index, True)
                    yield from self._generate_queen_positions(
                        column_index + 1,
                        state,
                    )
                    state.set_queen_state(column_index, row_index, False)
                else:
                    yield state.position.copy()

    def generate_queen_positions(self) -> Iterator[list[int]]:
        """Generate all queen placements for the configured board size."""
        state = PlacementState(self.column_count, self.diagonal_count)
        yield from self._generate_queen_positions(0, state)


class SolutionPresenter:  # pylint: disable=too-few-public-methods
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
