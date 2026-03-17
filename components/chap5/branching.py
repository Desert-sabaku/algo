"""List all possible combinations of queens in each line."""

import sys
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


def set_position(i: int) -> None:
    """Arrange the queens in i-th column."""
    for j in range(COLUMN_COUNT):
        POSITION[i] = j
        if i != 7:
            set_position(i + 1)
        else:
            print(*POSITION)


def set_position_simply() -> list[str]:
    """Arrange the queens in i-th column. Without a side effect."""
    return [
        convert_base(i, COLUMN_COUNT).zfill(COLUMN_COUNT) for i in range(COLUMN_COUNT**COLUMN_COUNT)
    ]


if __name__ == "__main__":
    # set_position(0)
    set_position_simply()
