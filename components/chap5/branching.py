"""List all possible combinations of queens in each line."""

import sys
from collections.abc import Iterator
from pathlib import Path

try:
    from components.chap2.conv import convert_base
except ModuleNotFoundError:
    project_root = Path(__file__).resolve().parents[2]
    if str(project_root) not in sys.path:
        sys.path.insert(0, str(project_root))
    from components.chap2.conv import convert_base

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
        yield convert_base(position_index, COLUMN_COUNT).zfill(COLUMN_COUNT)


if __name__ == "__main__":
    queen_positions_generator = generate_queen_positions()
    for _ in range(10):
        print(next(queen_positions_generator))
