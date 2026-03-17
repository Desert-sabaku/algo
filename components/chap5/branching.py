"""List all possible combinations of queens in each line."""

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


if __name__ == "__main__":
    set_position(0)
