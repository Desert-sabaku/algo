def convert_postfix(expression: str) -> list[str]:
    postfix: list[str] = []
    stack: list[str] = []

    for c in expression:
        match c:
            case c if c == "(":
                stack.append(c)
            case c if c == ")":
                while stack and stack[-1] != "(":
                    postfix.append(stack.pop())
                stack.pop()
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
            case c if c == "^":
                stack.append(c)
            case _:
                raise ValueError(f"Invalid character: {c}")
    postfix.extend(stack[::-1])
    stack.clear()

    return postfix


if __name__ == "__main__":
    print(convert_postfix("3+4*2/(1-5)^2^3"))
