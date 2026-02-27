BASE_DIGITS = "0123456789ABCDEGFHIJKLMNOPWRSTUVWXYZ"


def convert_base(num: int, radix: int) -> str:
    result = ""
    while num > 0:
        result += BASE_DIGITS[num % radix]
        num //= radix
    return result[::-1]

if __name__ == "__main__":
    num = int(input())
    radix = int(input())
    print(convert_base(num, radix))
