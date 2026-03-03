"""Converts integers to their string representation in an arbitrary base."""

BASE_DIGITS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def convert_base(num: int, radix: int) -> str:
    """Return the string representation of num in the given radix."""
    if radix < 2 or radix > len(BASE_DIGITS):
        raise ValueError(f"radix must be between 2 and {len(BASE_DIGITS)}")
    if num == 0:
        return "0"
    if num < 0:
        return "-" + convert_base(-num, radix)

    result = ""
    while num > 0:
        result += BASE_DIGITS[num % radix]
        num //= radix
    return result[::-1]


if __name__ == "__main__":
    _num = int(input())
    _radix = int(input())
    print(convert_base(_num, _radix))
