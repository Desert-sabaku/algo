"""Implementation of the solution of the tower of Hanoi."""

from typing import Literal

type DiskInfo = dict[Literal["count", "src", "dst"], int]


def move(disk_count: int, src_axis: int, dst_axis: int) -> list[DiskInfo]:
    """Return the order of move to solve the tower of Hanoi."""
    # 1, 2, 3 軸があるものとして、「srcでもdstでもない残り」の軸を求め、それを中間軸とする
    middle_axis = 6 - src_axis - dst_axis

    if disk_count == 1:
        move_entry: DiskInfo = {"count": disk_count, "src": src_axis, "dst": dst_axis}  # pylint: disable=redefined-outer-name
        return [move_entry]

    # 底を除く 1 ~ n-1 の円盤を src 軸から middle 軸へ移動
    left_moves = move(disk_count - 1, src_axis, middle_axis)
    center_entry: DiskInfo = {"count": disk_count, "src": src_axis, "dst": dst_axis}
    center_move = [center_entry]

    # 底を除く 1 ~ n-1 の円盤を middle 軸から dst 軸へ移動
    right_moves = move(disk_count - 1, middle_axis, dst_axis)

    return left_moves + center_move + right_moves


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
