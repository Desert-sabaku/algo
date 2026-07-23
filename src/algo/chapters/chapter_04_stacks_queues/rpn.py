def main():
    # expression = "5+4*4-2^4%3/1"
    expression = "5+4"
    postfix: list[str] = []
    stack: list[str] = []

    for c in expression:
        match c:
            case c if c.isdigit():
                postfix.append(c)
            case c if c in "+-":
                stack.append(c)
            case _:
                raise ValueError(f"Invalid character: {c}")
    else:
        if stack:
            postfix.append(stack.pop())

    return postfix


if __name__ == "__main__":
    print(main())
