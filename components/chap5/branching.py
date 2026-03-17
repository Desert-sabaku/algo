"""List all possible combinations of queens in each line."""

from collections.abc import Iterator

COLUMN_COUNT = 8
POSITION = [0] * COLUMN_COUNT


def set_position(column_index: int) -> None:
    """Arrange the queens in i-th column."""
    for row_index in range(COLUMN_COUNT):
        POSITION[column_index] = row_index
        if column_index != 7:
            set_position(column_index + 1)
        else:
            print(*POSITION)


def generate_queen_positions() -> Iterator[str]:
    """Yield a possible pattern of the queens arrangement."""
    for position_index in range(COLUMN_COUNT**COLUMN_COUNT):
        yield f"{position_index:08o}"


if __name__ == "__main__":
    queen_positions_generator = generate_queen_positions()
    for _ in range(10):
        print(next(queen_positions_generator))
