"""List all possible combinations of queens in each line."""

COLUMN_COUNT = 8
TOTAL_PATTERN = COLUMN_COUNT**COLUMN_COUNT
POSITION = [0] * COLUMN_COUNT


def set_position(column_index: int) -> None:
    """Arrange the queens in i-th column."""
    for row_index in range(COLUMN_COUNT):
        POSITION[column_index] = row_index
        if column_index != 7:  # noqa: PLR2004
            set_position(column_index + 1)
        else:
            print(*POSITION)


if __name__ == "__main__":
    # Generator[Y, S, R]
    # Y: yield する型。この場合 str になる。
    # S: send で受け取る型。引数的な奴。この場合 None。
    # R: 最後 return する型。反復の最後の返り値。この場合 None。
    queen_positions_generator = (f"{i:08o}" for i in range(TOTAL_PATTERN))
    for _ in range(10):
        print(next(queen_positions_generator))
