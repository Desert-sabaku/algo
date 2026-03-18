"""
List all possible arrangements of the queens so that no two queens occupy the same row or column.
"""

from collections.abc import Iterator
from itertools import islice

COLUMN_COUNT = 8
TOTAL_PATTERN = COLUMN_COUNT**COLUMN_COUNT
DIAGONAL_COUNT = 2 * COLUMN_COUNT - 1

POSITION = [0] * COLUMN_COUNT
IS_QUEEN_PLACED_HORIZONTAL = [False] * COLUMN_COUNT
IS_QUEEN_PLACED_POSITIVE_DIAGONAL = [False] * DIAGONAL_COUNT
IS_QUEEN_PLACED_NEGATIVE_DIAGONAL = [False] * DIAGONAL_COUNT


def get_positive_diagonal_index(column_index: int, row_index: int) -> int:
    """Return the index for the positive-sloped diagonal (/)."""
    return column_index + row_index


def get_negative_diagonal_index(column_index: int, row_index: int) -> int:
    """Return the index for the negative-sloped diagonal (\\)."""
    return column_index - row_index + COLUMN_COUNT - 1


def can_place_queen(column_index: int, row_index: int) -> bool:
    """Check whether a queen can be safely placed at the given position."""
    positive_diagonal_index = get_positive_diagonal_index(column_index, row_index)
    negative_diagonal_index = get_negative_diagonal_index(column_index, row_index)
    return (
        not IS_QUEEN_PLACED_HORIZONTAL[row_index]
        and not IS_QUEEN_PLACED_POSITIVE_DIAGONAL[positive_diagonal_index]
        and not IS_QUEEN_PLACED_NEGATIVE_DIAGONAL[negative_diagonal_index]
    )


def set_queen_state(column_index: int, row_index: int, is_placed: bool) -> None:
    """Mark or unmark occupancy for row and diagonals."""
    positive_diagonal_index = get_positive_diagonal_index(column_index, row_index)
    negative_diagonal_index = get_negative_diagonal_index(column_index, row_index)
    IS_QUEEN_PLACED_HORIZONTAL[row_index] = is_placed
    IS_QUEEN_PLACED_POSITIVE_DIAGONAL[positive_diagonal_index] = is_placed
    IS_QUEEN_PLACED_NEGATIVE_DIAGONAL[negative_diagonal_index] = is_placed


def generate_queen_positions(column_index: int = 0) -> Iterator[list[int]]:
    """Arrange the queens in i-th column."""
    for row_index in range(COLUMN_COUNT):
        if can_place_queen(column_index, row_index):
            POSITION[column_index] = row_index
            if column_index != COLUMN_COUNT - 1:
                set_queen_state(column_index, row_index, True)
                yield from generate_queen_positions(column_index + 1)
                set_queen_state(column_index, row_index, False)
            else:
                yield POSITION.copy()


def print_first_n_solutions(solution_count: int) -> int:
    """Print up to solution_count solutions and return how many were printed."""
    printed_count = 0
    for printed_count, solution in enumerate(
        islice(generate_queen_positions(), solution_count),
        start=1,
    ):
        for j in range(COLUMN_COUNT):
            for i in range(COLUMN_COUNT):
                print("♕" if solution[i] == j else "□", end="")
            print()
        print()
    return printed_count


if __name__ == "__main__":
    DISPLAY_SOLUTION_COUNT = 97
    shown_count = print_first_n_solutions(DISPLAY_SOLUTION_COUNT)
    print(f"Displayed {shown_count} solution(s).")
