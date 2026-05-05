"""Finds all divisor pairs of a given area."""


def divisors(area: int) -> list[tuple[int, int]]:
    """Return all divisor pairs (i, area // i) for the given positive area."""
    if area <= 0:
        raise ValueError("Area must be a positive integer.")
    result: list[tuple[int, int]] = []
    for i in range(1, area + 1):
        if i * i > area:
            break
        if area % i == 0:
            result.append((i, area // i))
    return result


if __name__ == "__main__":
    area = int(input("Enter the area of the square: "))
    for a, b in divisors(area):
        print(f"{a} x {b} = {area}")
