"""Implementation of a factorial function using a recursive algorithm."""

import math


def factorial(n: int) -> int:
    """Return the factorial of the input number."""
    if n < 0:
        raise ValueError("n must be a non-negative number.")

    return n * factorial(n - 1) if n > 0 else 1


if __name__ == "__main__":
    N = int(input())
    try:
        print(f"{N}の階乗は{math.factorial(N)}")
    except ValueError as e:
        print(f"{e}")

    try:
        assert math.factorial(N) == factorial(N)
    except AssertionError as e:
        print(e)
    else:
        print(f"{factorial.__name__} function passed the test.")
