"""Fixed-capacity stack implementation using ``collections.deque``."""

import random
from collections import deque
from typing import Iterator


class FixedStack[T]:
    """Fixed Stack

    Implementation using delegation of deque
    """

    def __init__(self, capacity: int = 256) -> None:
        """Initialize a stack with the given maximum ``capacity``."""
        if capacity <= 0:
            raise ValueError("Capacity must be at least 1.")

        self.capacity = capacity
        self.__stack: deque[T] = deque(maxlen=capacity)

    # Pythonならこの程度自動生成してくれるんじゃね？
    # と思ったが、そういうわけでもなさそう。
    # 委譲の場合しっかり手書きがいる。
    def __len__(self) -> int:
        """Return the current number of elements in the stack."""
        return len(self.__stack)

    def __contains__(self, item: T) -> bool:
        """Return ``True`` if ``item`` exists in the stack."""
        return item in self.__stack

    def __iter__(self) -> Iterator[T]:
        """Iterate over stack items from bottom to top."""
        return iter(self.__stack)

    def is_empty(self) -> bool:
        """Return ``True`` when the stack contains no elements."""
        return not self.__stack

    def is_full(self) -> bool:
        """Return ``True`` when the stack reached its capacity."""
        return len(self.__stack) == self.__stack.maxlen

    def push(self, value: T) -> None:
        """Push ``value`` onto the stack."""
        self.__stack.append(value)

    def pop(self) -> T:
        """Pop and return the top element.

        Raises:
            IndexError: If the stack is empty.
        """
        return self.__stack.pop()

    def find(self, value: T) -> int:
        """Return the index of ``value`` in the internal storage order.

        Raises:
            ValueError: If ``value`` is not present in the stack.
        """
        n = len(self.__stack)
        for offset, v in enumerate(reversed(self.__stack)):
            if v == value:
                return n - offset - 1
        raise ValueError(f"{value} is not in stack")


if __name__ == "__main__":
    stack = FixedStack[int]()
    print(f"{stack.capacity=}")
    print(f"{len(stack)}")
    for i in range(10):
        stack.push(i)

    print(f"{list(stack)}")

    x = random.randint(1, 10)
    print(f"random {x}")

    print(f"{stack.find(x)}")

    try:
        stack.find(999)
    except ValueError as e:
        print(e)
