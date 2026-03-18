"""Implementation a memoization"""

memo: list[str] = [""] * 128


def recursive(n: int) -> None:
    """Do the same move of `recursive.py` with a memo."""
    if n < -1 or n + 1 >= len(memo):
        raise ValueError(f"n must be between -1 and {len(memo) - 2}.")

    if memo[n + 1]:
        print(memo[n + 1], end="")
        return

    if n > 0:
        recursive(n - 1)
        print(n, end=" ")
        recursive(n - 2)
        memo[n + 1] = f"{memo[n]}{n}\n{memo[n - 1]}"
    else:
        # 実質的にn=0,-1のとき
        memo[n + 1] = ""


if __name__ == "__main__":
    recursive(4)
