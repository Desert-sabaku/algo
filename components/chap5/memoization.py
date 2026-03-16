"""Implementation a memoization"""

memo: list[str] = [""] * 128


def recursive(n: int) -> None:
    """Do the same move of `recursive.py` with a memo."""
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
