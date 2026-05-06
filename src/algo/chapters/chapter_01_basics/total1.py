"""Prints cumulative sum from a to b with formatted output."""


def cumulative_sum(a: int, b: int) -> int:
    """Return the sum of all integers from a to b inclusive."""
    if a > b:
        a, b = b, a
    return sum(range(a, b + 1))


if __name__ == "__main__":
    _a = int(input("integer: "))
    _b = int(input("integer: "))
    if _a > _b:
        _a, _b = _b, _a
    total = 0
    for i in range(_a, _b + 1):
        if i < _b:
            print(f"{i} + ", end="")
        else:
            print(f"{i} = ", end="")
        total += i
    print(total)
