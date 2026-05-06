"""Implementation of the solution of the tower of Hanoi."""

from typing import Literal

type DiskInfo = dict[Literal["count", "src", "dst"], int]


def _hanoi(disk_count: int, src_axis: int, dst_axis: int) -> list[DiskInfo]:
    """Internal recursive helper; handles the disk_count=1 base case."""
    middle_axis = 6 - src_axis - dst_axis
    if disk_count == 1:
        return [{"count": 1, "src": src_axis, "dst": dst_axis}]
    left_moves = _hanoi(disk_count - 1, src_axis, middle_axis)
    center_entry: DiskInfo = {"count": disk_count, "src": src_axis, "dst": dst_axis}
    right_moves = _hanoi(disk_count - 1, middle_axis, dst_axis)
    return left_moves + [center_entry] + right_moves


def move(disk_count: int, src_axis: int, dst_axis: int) -> list[DiskInfo]:
    """Return the order of move to solve the tower of Hanoi."""
    if disk_count <= 1:
        raise ValueError("disk_count must be at least 2.")
    if src_axis not in (1, 2, 3) or dst_axis not in (1, 2, 3) or src_axis == dst_axis:
        raise ValueError("src_axis and dst_axis must be different values in {1, 2, 3}.")
    return _hanoi(disk_count, src_axis, dst_axis)


if __name__ == "__main__":
    print("==TOWER OF HANOI==")

    # 円盤1, 2, 3を1軸から3軸へ移動
    N = 3
    moves_log = move(N, 1, 3)

    for move_entry in moves_log:
        print(
            # Too long to write one line.
            "Move the "
            f"{move_entry['count']}th disk from the "
            f"{move_entry['src']}th axis to the "
            f"{move_entry['dst']}th axis."
        )
