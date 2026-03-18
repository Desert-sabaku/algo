"""
List all possible arrangements of the queens so that no two queens occupy the same row or column.
"""

COLUMN_COUNT = 8
TOTAL_PATTERN = COLUMN_COUNT**COLUMN_COUNT

POSITION = [0] * COLUMN_COUNT
IS_QUEEN_PLACED = [False] * COLUMN_COUNT


def set_position(column_index: int = 0) -> None:
    """Arrange the queens in i-th column."""
    for row_index in range(COLUMN_COUNT):
        if not IS_QUEEN_PLACED[row_index]:
            POSITION[column_index] = row_index
            if column_index != COLUMN_COUNT - 1:
                IS_QUEEN_PLACED[row_index] = True
                set_position(column_index + 1)
                # Clean up
                IS_QUEEN_PLACED[row_index] = False
            else:
                print(POSITION)


if __name__ == "__main__":
    set_position(0)
