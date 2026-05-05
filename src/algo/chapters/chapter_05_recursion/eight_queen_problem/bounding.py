"""
List all possible arrangements of the queens so that no two queens occupy the same row or column.
"""

COLUMN_COUNT = 8


def set_all_positions(column_count: int = COLUMN_COUNT) -> list[list[int]]:
    """Return all valid column-bounding queen arrangements (no shared row/column)."""
    position = [0] * column_count
    is_queen_placed = [False] * column_count
    results: list[list[int]] = []

    def _set_position(column_index: int = 0) -> None:
        for row_index in range(column_count):
            if not is_queen_placed[row_index]:
                position[column_index] = row_index
                if column_index != column_count - 1:
                    is_queen_placed[row_index] = True
                    _set_position(column_index + 1)
                    is_queen_placed[row_index] = False
                else:
                    results.append(position.copy())

    _set_position(0)
    return results


if __name__ == "__main__":
    for pos in set_all_positions():
        print(pos)
