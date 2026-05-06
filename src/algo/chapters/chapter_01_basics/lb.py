"""Demonstrates asterisk display patterns."""


def asterisk_lines(asterisk_count: int, words: int) -> list[str]:
    """Return lines of asterisks with `words` asterisks per line."""
    if asterisk_count < 0:
        raise ValueError("asterisk_count must be non-negative")
    if words <= 0:
        raise ValueError("Number of asterisks per line must be greater than 0.")
    lines: list[str] = []
    for _ in range(asterisk_count // words):
        lines.append("*" * words)
    if rest := asterisk_count % words:
        lines.append("*" * rest)
    return lines


if __name__ == "__main__":
    ASTERISK_COUNT = int(input("Total number of asterisks: "))
    WORDS = int(input("Number of asterisks per line: "))
    for line in asterisk_lines(ASTERISK_COUNT, WORDS):
        print(line)
