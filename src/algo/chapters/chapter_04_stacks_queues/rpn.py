def main():
    expression = "5+4*4-2*4%3/1"
    postfix: list[str] = []
    stack: list[str] = []

    for c in expression:
        print(stack)
        match c:
            case c if c.isdigit():
                postfix.append(c)
            case c if c in "+-":
                while stack and stack[-1] in "+-*/%^":
                    postfix.append(stack.pop())
                stack.append(c)
            case c if c in "*/%":
                while stack and stack[-1] in "*/%^":
                    postfix.append(stack.pop())
                stack.append(c)
            case _:
                raise ValueError(f"Invalid character: {c}")
                break
    else:
        if stack:
            postfix.append(stack.pop())

    return postfix


if __name__ == "__main__":
    print(main())
