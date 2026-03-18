"""
List all possible arrangements of the queens so that no two queens occupy the same row or column.
"""

from collections.abc import Iterator, Sequence
from dataclasses import dataclass, field
from itertools import islice
from typing import Protocol

DEFAULT_BOARD_SIZE = 8
DEFAULT_MAX_SOLUTIONS_TO_PRINT = 97


@dataclass
class PlacementState:
    """Store and manipulate mutable state during backtracking.

    This object encapsulates all mutable placement data that changes while the
    solver explores the search tree.

    Attributes:
        board_size: Number of rows/columns on the board.
        queen_rows_by_column: Row index of the queen for each column.
        occupied_rows: Whether each row already contains a queen.
        occupied_positive_diagonals: Occupancy for diagonals with constant
            ``column + row``.
        occupied_negative_diagonals: Occupancy for diagonals with constant
            ``column - row`` (offset to keep indices non-negative).
    """

    board_size: int
    queen_rows_by_column: list[int] = field(init=False)
    occupied_rows: list[bool] = field(init=False)
    occupied_positive_diagonals: list[bool] = field(init=False)
    occupied_negative_diagonals: list[bool] = field(init=False)

    def __post_init__(self) -> None:
        """Initialize all mutable occupancy buffers for the given board size."""
        diagonal_count = 2 * self.board_size - 1
        self.queen_rows_by_column = [-1] * self.board_size
        self.occupied_rows = [False] * self.board_size
        self.occupied_positive_diagonals = [False] * diagonal_count
        self.occupied_negative_diagonals = [False] * diagonal_count

    def positive_diagonal_index(self, column_index: int, row_index: int) -> int:
        """Compute the index for the positive-sloped diagonal.

        Args:
            column_index: Zero-based column index.
            row_index: Zero-based row index.

        Returns:
            int: Index in ``occupied_positive_diagonals``.
        """
        return column_index + row_index

    def negative_diagonal_index(self, column_index: int, row_index: int) -> int:
        """Compute the index for the negative-sloped diagonal.

        Args:
            column_index: Zero-based column index.
            row_index: Zero-based row index.

        Returns:
            int: Index in ``occupied_negative_diagonals``.
        """
        return column_index - row_index + self.board_size - 1

    def can_place(self, column_index: int, row_index: int) -> bool:
        """Check whether a queen can be placed at ``(column_index, row_index)``.

        Args:
            column_index: Zero-based column index.
            row_index: Zero-based row index.

        Returns:
            bool: ``True`` if row and both diagonals are currently free.
        """
        positive_diagonal_index = self.positive_diagonal_index(column_index, row_index)
        negative_diagonal_index = self.negative_diagonal_index(column_index, row_index)
        return not (
            self.occupied_rows[row_index]
            or self.occupied_positive_diagonals[positive_diagonal_index]
            or self.occupied_negative_diagonals[negative_diagonal_index]
        )

    def place(self, column_index: int, row_index: int) -> None:
        """Place a queen and mark all related constraints as occupied.

        Args:
            column_index: Zero-based column index.
            row_index: Zero-based row index.
        """
        positive_diagonal_index = self.positive_diagonal_index(column_index, row_index)
        negative_diagonal_index = self.negative_diagonal_index(column_index, row_index)
        self.queen_rows_by_column[column_index] = row_index
        self.occupied_rows[row_index] = True
        self.occupied_positive_diagonals[positive_diagonal_index] = True
        self.occupied_negative_diagonals[negative_diagonal_index] = True

    def remove(self, column_index: int, row_index: int) -> None:
        """Remove a queen and clear all related occupied markers.

        Args:
            column_index: Zero-based column index.
            row_index: Zero-based row index.
        """
        positive_diagonal_index = self.positive_diagonal_index(column_index, row_index)
        negative_diagonal_index = self.negative_diagonal_index(column_index, row_index)
        self.queen_rows_by_column[column_index] = -1
        self.occupied_rows[row_index] = False
        self.occupied_positive_diagonals[positive_diagonal_index] = False
        self.occupied_negative_diagonals[negative_diagonal_index] = False


class EightQueenSolver:  # pylint: disable=too-few-public-methods
    """Generate solutions for the N-Queens problem.

    The solver yields solutions lazily through backtracking, so callers can
    consume only as many solutions as needed.
    """

    def __init__(self, board_size: int = DEFAULT_BOARD_SIZE) -> None:
        """Initialize solver configuration.

        Args:
            board_size: Number of rows/columns on the board.
        """
        self.board_size = board_size

    def generate_solutions(self) -> Iterator[list[int]]:
        """Yield all valid queen placements for the configured board size.

        Yields:
            list[int]: A solution where each element is the row index of the
                queen for the corresponding column.
        """
        placement_state = PlacementState(self.board_size)
        yield from self._search(column_index=0, placement_state=placement_state)

    def _search(
        self,
        column_index: int,
        placement_state: PlacementState,
    ) -> Iterator[list[int]]:
        """Recursively explore queen placements from the current column.

        Args:
            column_index: Column currently being assigned.
            placement_state: Shared mutable state across recursion frames.

        Yields:
            list[int]: A complete valid placement.
        """
        for row_index in range(self.board_size):
            if placement_state.can_place(column_index, row_index):
                placement_state.place(column_index, row_index)
                if column_index == self.board_size - 1:
                    yield placement_state.queen_rows_by_column.copy()
                else:
                    yield from self._search(column_index + 1, placement_state)
                placement_state.remove(column_index, row_index)


class SolutionRenderer(Protocol):  # pylint: disable=too-few-public-methods
    """Define the rendering contract for a single solution."""

    def render(self, solution: Sequence[int]) -> str:
        """Return a string representation for one solution.

        Args:
            solution: Row index by column for one complete queen placement.

        Returns:
            str: Rendered board or equivalent textual representation.
        """
        raise NotImplementedError


class QueenBoardRenderer:  # pylint: disable=too-few-public-methods
    """Render a queen solution as a board of symbols."""

    def __init__(
        self,
        board_size: int,
        queen_symbol: str = "♕",
        empty_symbol: str = "□",
    ) -> None:
        """Initialize board renderer configuration.

        Args:
            board_size: Number of rows/columns on the board.
            queen_symbol: Symbol used for a queen cell.
            empty_symbol: Symbol used for an empty cell.
        """
        self.board_size = board_size
        self.queen_symbol = queen_symbol
        self.empty_symbol = empty_symbol

    def render(self, solution: Sequence[int]) -> str:
        """Render one solution as a multi-line board string.

        Args:
            solution: Row index by column for one complete queen placement.

        Returns:
            str: Multi-line text board.
        """
        rows: list[str] = []
        for row_index in range(self.board_size):
            row = "".join(
                self.queen_symbol if solution[column_index] == row_index else self.empty_symbol
                for column_index in range(self.board_size)
            )
            rows.append(row)
        return "\n".join(rows)


class SolutionPrinter:  # pylint: disable=too-few-public-methods
    """Handle output policy for generated solutions."""

    def __init__(self, renderer: SolutionRenderer) -> None:
        """Initialize printer with a rendering strategy.

        Args:
            renderer: Component used to convert each solution to text.
        """
        self.renderer = renderer

    def print_first_n(
        self,
        solutions: Iterator[Sequence[int]],
        max_solutions: int,
    ) -> int:
        """Print at most ``max_solutions`` items from a solution iterator.

        Args:
            solutions: Lazy iterator of complete queen placements.
            max_solutions: Upper bound for how many solutions to print.

        Returns:
            int: Number of solutions actually printed.
        """
        printed_count = 0
        for printed_count, solution in enumerate(islice(solutions, max_solutions), start=1):
            print(self.renderer.render(solution))
            print()
        return printed_count


if __name__ == "__main__":
    solver = EightQueenSolver()
    board_renderer = QueenBoardRenderer(solver.board_size)
    solution_printer = SolutionPrinter(board_renderer)
    shown_count = solution_printer.print_first_n(
        solver.generate_solutions(),
        DEFAULT_MAX_SOLUTIONS_TO_PRINT,
    )
    print(f"Displayed {shown_count} solution(s).")
