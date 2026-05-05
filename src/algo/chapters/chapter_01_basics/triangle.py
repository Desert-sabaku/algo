"""Prints triangle patterns using asterisks."""


def triangle_rows(n: int) -> list[str]:
    """Return the four triangle patterns as a list of lines."""
    lines: list[str] = []
    for i in range(1, n + 1):
        lines.append("*" * i)
    lines.append("")
    for i in range(1, n + 1):
        lines.append(" " * (n - i) + "*" * i)
    lines.append("")
    for i in range(n, 0, -1):
        lines.append("*" * i)
    lines.append("")
    for i in range(n, 0, -1):
        lines.append(" " * (i - 1) + "*" * (n - i + 1))
    return lines


if __name__ == "__main__":
    N = int(input("Short side length: "))
    for line in triangle_rows(N):
        print(line)
