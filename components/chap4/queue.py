"""Fixed-length queue implementation"""

from typing import Iterator, cast

_EMPTY_SLOT = object()


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

        def __init__(self, front: int, rear: int, size: int) -> None:
            self.front = front
            self.rear = rear
            self.size = size
            super().__init__(f"Queue invariant broken (front={front}, rear={rear}, count={size}).")

    def __init__(self, capacity: int = 256) -> None:
        """Initialize queue storage with the given maximum ``capacity``."""
        if capacity <= 0:
            raise ValueError("Capacity must be at least 1.")

        self._capacity = capacity
        self._queue: list[T | object] = [_EMPTY_SLOT] * capacity
        # Q. `front`と`rear`の値から`size`は一意に決まりそうだが
        # 独立に`size`属性を定義する必要性はあるのか
        # A. `front`と`rear`の値が同じだと
        # `queue`が空か満杯か区別できない
        # したがって一意に定まらない。
        self._size = 0
        self._front = 0
        self._rear = 0

    def __len__(self) -> int:
        """Return the number of enqueued elements."""
        return self._size

    def _iter_active_indices(self) -> Iterator[int]:
        """Yield physical indices of active queue elements in logical order."""
        for offset in range(self._size):
            # 下の式、わけわからんくてプログラマは不安よな。
            # 松本動きます。
            # 配列は`0`から`capacity - 1`まで
            # 論理順序的には`i`番目の要素は`front`から`i`先。
            # ただ、末尾を超えてしまう。
            # 例：`capacity=8`, `front=6`, `i=3`なら`front+i=9`
            # 実際には`9`ではなく`0`にもどって`1`
            # 「末尾を超えたら先頭に戻る」は剰余で書ける
            yield (self._front + offset) % self._capacity

    def __contains__(self, item: T) -> bool:
        """Return ``True`` if ``item`` exists in the queue."""
        for index in self._iter_active_indices():
            if self._queue[index] == item:
                return True
        return False

    def is_empty(self) -> bool:
        """Return ``True`` when the queue has no elements."""
        return self._size == 0

    def is_full(self) -> bool:
        """Return ``True`` when the queue reached ``capacity``."""
        return self._size == self._capacity

    def enqueue(self, value: T) -> None:
        """Insert ``value`` at the rear of the queue.

        Raises:
            FullError: If the queue is full.
        """
        if self.is_full():
            raise self.FullError(f"Failed to enqueue {value} because the queue is full.")

        self._queue[self._rear] = value
        self._rear += 1

        # ring buffer 実装のため
        # 例えば0~11のスロットを持つサイズ12である`queue`のスロット11にデータをぶち込むと
        # `rear`は12を指して`capacity`と等しくなる。
        if self._rear == self._capacity:
            self._rear = 0

        self._size += 1

    def dequeue(self) -> T:
        """Remove and return the front element.

        Raises:
            EmptyError: If the queue is empty.
            InvariantBrokenError: If internal queue state is inconsistent.
        """
        if self.is_empty():
            raise self.EmptyError("Failed to dequeue because the queue is empty.")

        value = self._queue[self._front]
        if value is _EMPTY_SLOT:
            raise self.InvariantBrokenError(self._front, self._rear, self._size)

        self._queue[self._front] = _EMPTY_SLOT
        self._front += 1
        if self._front == self._capacity:
            self._front = 0

        self._size -= 1
        return cast(T, value)

    def peek(self) -> T:
        """Return the front element without removing it.

        Raises:
            EmptyError: If the queue is empty.
            InvariantBrokenError: If internal queue state is inconsistent.
        """
        if self.is_empty():
            raise self.EmptyError("Failed to peek because the queue is empty.")

        value = self._queue[self._front]
        if value is _EMPTY_SLOT:
            raise self.InvariantBrokenError(self._front, self._rear, self._size)

        return cast(T, value)

    def find(self, value: T) -> int | None:
        """Return the internal physical index of ``value`` or ``None``."""
        for index in self._iter_active_indices():
            if self._queue[index] == value:
                return index
        return None

    def count(self, value: T) -> int:
        """Count how many times ``value`` appears in the queue."""
        count = 0
        for index in self._iter_active_indices():
            if self._queue[index] == value:
                count += 1
        return count

    def clear(self) -> None:
        """Remove all elements and reset cursor positions."""
        self._queue = [_EMPTY_SLOT] * self._capacity
        self._size = self._front = self._rear = 0

    @property
    def elements(self) -> list[T]:
        """Return queue contents in logical FIFO order as a list."""
        result = [self._queue[index] for index in self._iter_active_indices()]

        if any(v is _EMPTY_SLOT for v in result):
            raise self.InvariantBrokenError(self._front, self._rear, self._size)

        return [cast(T, v) for v in result]


def _run_self_tests() -> None:
    """Run lightweight in-file tests for ``FixedQueue`` behavior."""
    q = FixedQueue[int](3)
    assert q.is_empty()
    assert len(q) == 0

    q.enqueue(10)
    q.enqueue(20)
    assert q.peek() == 10
    assert 10 in q
    assert 99 not in q
    assert q.count(10) == 1
    assert q.find(20) is not None
    assert q.elements == [10, 20]

    assert q.dequeue() == 10
    q.enqueue(30)
    q.enqueue(40)
    assert q.is_full()
    assert q.elements == [20, 30, 40]

    try:
        q.enqueue(50)
    except FixedQueue.FullError:
        pass
    else:
        raise AssertionError("enqueue should raise FullError when queue is full")

    assert q.dequeue() == 20
    assert q.dequeue() == 30
    assert q.dequeue() == 40

    try:
        q.dequeue()
    except FixedQueue.EmptyError:
        pass
    else:
        raise AssertionError("dequeue should raise EmptyError when queue is empty")

    q.enqueue(1)
    q.enqueue(2)
    q.clear()
    assert q.is_empty()
    assert q.elements == []

    q_none = FixedQueue[int | None](3)
    q_none.enqueue(None)
    q_none.enqueue(1)
    assert q_none.peek() is None
    assert q_none.dequeue() is None
    assert q_none.dequeue() == 1


if __name__ == "__main__":
    _run_self_tests()
    print("All FixedQueue self-tests passed.")
