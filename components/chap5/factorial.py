"""Implementation of a factorial function using a recursive algorithm."""

import math


def factorial(n: int) -> int:
    """Return the factorial of the input number."""
    if n < 0:
        raise ValueError("n must be a non-negative number.")

    return n * factorial(n - 1) if n > 0 else 1


if __name__ == "__main__":
    N = int(input("N: "))
    print(factorial(N))

    print("Answer by built-in function:", math.factorial(N))
