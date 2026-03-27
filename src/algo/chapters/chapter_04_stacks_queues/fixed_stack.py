"""Fixed-length stack implementation with explicit exceptions."""

from __future__ import annotations

from typing import Callable, cast


class FixedStack[T]:
    """Fixed-length stack.

    Raises:
        Empty: On pop/peek from an empty stack.
        Full: On push to a full stack.
    """

    class Empty(Exception):
        """Raised when stack operations are requested on an empty stack."""

    class Full(Exception):
        """Raised when pushing to a stack that is already full."""

    def __init__(self, capacity: int = 256) -> None:
        """Initialize an empty fixed stack with a positive capacity."""

        if capacity <= 0:
            raise ValueError("Capacity must be at least 1.")

        self.capacity = capacity
        self.stack: list[T | None] = [None] * capacity
        self.pointer = 0

    def __len__(self) -> int:
        """Return the number of elements currently in the stack."""

        return self.pointer

    def is_empty(self) -> bool:
        """Return whether the stack contains no elements."""

        return self.pointer == 0

    def is_full(self) -> bool:
        """Return whether the stack has reached its capacity."""

        return self.pointer == self.capacity

    def push(self, value: T) -> None:
        """Push one value onto the stack.

        Raises:
            Full: If the stack is already full.
        """

        if self.is_full():
            raise FixedStack.Full

        self.stack[self.pointer] = value
        self.pointer += 1

    def pop(self) -> T:
        """Pop and return the latest value.

        Raises:
            Empty: If the stack is empty.
        """

        if self.is_empty():
            raise FixedStack.Empty

        self.pointer -= 1
        value = self.stack[self.pointer]
        self.stack[self.pointer] = None
        return cast(T, value)

    def peek(self) -> T:
        """Return the latest value without removing it.

        Raises:
            Empty: If the stack is empty.
        """

        if self.is_empty():
            raise FixedStack.Empty

        value = self.stack[self.pointer - 1]
        return cast(T, value)

    def clear(self) -> None:
        """Remove all elements from the stack."""

        self.stack = [None] * self.capacity
        self.pointer = 0

    def find(self, value: T) -> int | None:
        """Return storage index of value, or None when not found."""

        for i in range(self.pointer - 1, -1, -1):
            if self.stack[i] == value:
                return i
        return None

    def count(self, value: T) -> int:
        """Count how many times value appears in the stack."""

        return self.stack[: self.pointer].count(value)

    def __contains__(self, value: object) -> bool:
        """Return whether value exists in the stack."""

        return value in self.stack[: self.pointer]

    def dump(self) -> None:
        """Print all values from bottom to top."""

        print(self.stack[: self.pointer])


type Action = Callable[[FixedStack[int]], None]


def _demo() -> None:
    """Run a simple menu demo and show exception handling behavior."""

    print("=== FixedStack メニュー式テスト ===")

    while True:
        try:
            capacity = int(input("スタックのサイズを入力してください: "))
            if capacity > 0:
                break
            print("1以上の整数を入力してください。")
        except ValueError:
            print("整数を入力してください。")

    stack = FixedStack[int](capacity)
    actions: dict[str, Action] = {
        "1": _handle_push,
        "2": _handle_pop,
        "3": _handle_peek,
        "4": _handle_dump,
    }

    while True:
        print("\n[1] push [2] pop [3] peek [4] dump [0] 終了")
        menu = input("番号を選んでください: ").strip()

        if menu == "0":
            print("終了します。")
            return

        action = actions.get(menu)
        if action is None:
            print("0~4の番号で入力してください。")
            continue

        action(stack)


def _handle_push(stack: FixedStack[int]) -> None:
    """Handle one push operation from user input."""

    try:
        value = int(input("pushする整数: "))
        stack.push(value)
        print(f"{value} をpushしました。")
    except ValueError:
        print("整数を入力してください。")
    except FixedStack.Full:
        print("スタックが満杯です。")


def _handle_pop(stack: FixedStack[int]) -> None:
    """Handle one pop operation and display result."""

    try:
        popped = stack.pop()
        print(f"popしました: {popped}")
    except FixedStack.Empty:
        print("スタックが空です。")


def _handle_peek(stack: FixedStack[int]) -> None:
    """Handle one peek operation and display result."""

    try:
        top = stack.peek()
        print(f"先頭の値: {top}")
    except FixedStack.Empty:
        print("スタックが空です。")


def _handle_dump(stack: FixedStack[int]) -> None:
    """Handle one dump operation."""

    stack.dump()


if __name__ == "__main__":
    _demo()
