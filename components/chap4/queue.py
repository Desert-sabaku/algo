"""Fixed-length queue implementation"""


class FixedQueue[T]:
    """Fixed-capacity FIFO queue implemented as a ring buffer."""

    # 「親例外」を定義しておくと、例外処理の時に
    # except self.QueueErrorで両方拾える
    class QueueError(Exception):
        """Base class for queue operation errors."""

    class EmptyError(QueueError):
        """Raised when dequeue/peek is called on an empty queue."""

    class FullError(QueueError):
        """Raised when enqueue is called on a full queue."""

    # デバッグしやすいように状態を表示するゾ
    class InvariantBrokenError(QueueError, RuntimeError):
        """Raised when the internal ring-buffer state becomes inconsistent."""

        def __init__(self, front: int, rear: int, count: int) -> None:
            self.front = front
            self.rear = rear
            self.count = count
            super().__init__(f"Queue invariant broken (front={front}, rear={rear}, count={count}).")

    def __init__(self, capacity: int = 256) -> None:
        """Initialize queue storage with the given maximum ``capacity``."""
        if capacity <= 0:
            raise ValueError("Capacity must be at least 1.")

        self.capacity = capacity
        self.queue: list[T | None] = [None] * capacity
        # Q. cursorの値からcountは一意に決まりそうだが
        # 独立にcount属性を定義する必要性はあるのか
        # A. frontとrearの値が同じだと
        # queueが空の時と満杯の時が区別できない
        # したがって一意に定まらない。
        self.count = 0
        self.front = 0
        self.rear = 0

    def __len__(self) -> int:
        """Return the number of enqueued elements."""
        return self.count

    def is_empty(self) -> bool:
        """Return ``True`` when the queue has no elements."""
        return self.count == 0

    def is_full(self) -> bool:
        """Return ``True`` when the queue reached ``capacity``."""
        return self.count == self.capacity

    def enqueue(self, value: T) -> None:
        """Insert ``value`` at the rear of the queue.

        Raises:
            FullError: If the queue is full.
        """
        if self.is_full():
            raise self.FullError(f"Failed to enqueue {value} because the queue is full.")

        self.queue[self.rear] = value
        self.rear += 1

        # ring buffer 実装のため
        # 例えば0~11のスロットを持つサイズ12である`queue`のスロット11にデータをぶち込むと
        # `rear`は12を指して`capacity`と等しくなる。
        if self.rear == self.capacity:
            self.rear = 0

        self.count += 1

    def dequeue(self) -> T:
        """Remove and return the front element.

        Raises:
            EmptyError: If the queue is empty.
            InvariantBrokenError: If internal queue state is inconsistent.
        """
        if self.is_empty():
            raise self.EmptyError("Failed to dequeue because the queue is empty.")

        value = self.queue[self.front]
        if value is None:
            raise self.InvariantBrokenError(self.front, self.rear, self.count)

        # 内部状態を明示的に保つため、デキューされた要素を削除する。
        self.queue[self.front] = None
        self.front += 1
        if self.front == self.capacity:
            self.front = 0

        self.count -= 1
        return value

    def peek(self) -> T:
        """Return the front element without removing it.

        Raises:
            EmptyError: If the queue is empty.
            InvariantBrokenError: If internal queue state is inconsistent.
        """
        if self.is_empty():
            raise self.EmptyError("Failed to peek because the queue is empty.")

        value = self.queue[self.front]
        if value is None:
            raise self.InvariantBrokenError(self.front, self.rear, self.count)

        return value

    # TODO: find, count, clear, in, dump
