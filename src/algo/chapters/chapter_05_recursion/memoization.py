"""Implementation a memoization"""

_MEMO_SIZE = 128


def recursive(n: int, _memo: list[str] | None = None) -> None:
    """Do the same move of `recursive.py` with a memo."""
    memo: list[str] = _memo if _memo is not None else [""] * _MEMO_SIZE

    if n < -1 or n + 1 >= len(memo):
        raise ValueError(f"n must be between -1 and {len(memo) - 2}.")

    if memo[n + 1]:
        print(memo[n + 1], end="")
        return

    if n > 0:
        recursive(n - 1, memo)
        print(n, end=" ")
        recursive(n - 2, memo)
        memo[n + 1] = f"{memo[n]}{n}\n{memo[n - 1]}"
    else:
        memo[n + 1] = ""


if __name__ == "__main__":
    recursive(4)
