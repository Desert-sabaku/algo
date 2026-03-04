"""Hash (open addressing) implementation with demonstration."""

from __future__ import annotations

from collections.abc import Hashable
from enum import Enum
from typing import TypeVar

KEY = TypeVar("KEY", bound=Hashable)
VALUE = TypeVar("VALUE")


class Status(Enum):
    """State of each bucket in the open-addressing hash table."""

    OCCUPIED = 0
    EMPTY = 1
    DELETED = 2


class Bucket[KEY, VALUE]:
    """Container that stores one key-value pair and its usage status."""

    __slots__ = ("_key", "_value", "_status")

    def __init__(
        self, key: KEY | None = None, value: VALUE | None = None, status: Status = Status.EMPTY
    ) -> None:
        """Initialize a bucket with optional key/value and status."""

        self._key = key
        self._value = value
        self._status = status

    @property
    def key(self) -> KEY | None:
        """Return the bucket key (read-only)."""

        return self._key

    @property
    def value(self) -> VALUE | None:
        """Return the bucket value."""

        return self._value

    @value.setter
    def value(self, new_value: VALUE) -> None:
        """Update the bucket value."""

        self._value = new_value

    @property
    def status(self) -> Status:
        """Return the bucket status."""

        return self._status

    @status.setter
    def status(self, new_status: Status) -> None:
        """Update the bucket status."""

        self._status = new_status


class OpenHash[KEY, VALUE]:
    """Hash table implementation using linear probing for collision handling."""

    def __init__(self, capacity: int) -> None:
        """Create an empty hash table with the given fixed capacity."""

        if capacity <= 0:
            raise ValueError("Capacity must be at least 1.")

        self._capacity = capacity
        self._buckets = [Bucket[KEY, VALUE]() for _ in range(capacity)]

    @property
    def capacity(self) -> int:
        """Return the capacity of the hash."""

        return self._capacity

    @property
    def buckets(self) -> list[Bucket[KEY, VALUE]]:
        """Return the buckets."""

        return self._buckets

    def _hash_value(self, key: KEY) -> int:
        """Return the primary hash index for the key."""

        return hash(key) % self._capacity

    def _rehash_value(self, hash_value: int) -> int:
        """Return the next index for linear probing."""

        return (hash_value + 1) % self._capacity

    def search_bucket(self, key: KEY) -> Bucket[KEY, VALUE] | None:
        """Find and return the bucket for the key, or ``None`` if not found."""

        hash_value = self._hash_value(key)
        current = self._buckets[hash_value]

        for _ in range(self._capacity):
            if current.status == Status.EMPTY:
                break
            if current.status == Status.OCCUPIED and current.key == key:
                return current

            hash_value = self._rehash_value(hash_value)
            current = self._buckets[hash_value]

        return None

    def search(self, key: KEY) -> VALUE | None:
        """Return the value for the key, or ``None`` when the key is absent."""

        current = self.search_bucket(key)

        if current is None:
            return None

        return current.value

    def add(self, key: KEY, value: VALUE) -> bool:
        """Insert a key-value pair if the key does not exist already."""

        if self.search(key) is not None:
            return False

        hash_value = self._hash_value(key)
        current = self._buckets[hash_value]

        for _ in range(self._capacity):
            if current.status in (Status.EMPTY, Status.DELETED):
                self._buckets[hash_value] = Bucket(key, value, Status.OCCUPIED)
                return True
            hash_value = self._rehash_value(hash_value)
            current = self._buckets[hash_value]

        return False

    def remove(self, key: KEY) -> bool:
        """Delete the key by marking its bucket as deleted."""

        current = self.search_bucket(key)
        if current is None:
            return False
        current.status = Status.DELETED
        return True

    def dump(self) -> None:
        """Print all bucket states for debugging and demonstration."""

        for i in range(self._capacity):
            print(f"{i:2} ", end="")
            if self.buckets[i].status == Status.OCCUPIED:
                print(f"{self.buckets[i].key} ({self.buckets[i].value})")
            elif self.buckets[i].status == Status.EMPTY:
                print("UNREGISTERED")
            else:
                print("DELETED")


def _demo() -> None:
    """Run a short demonstration of open addressing hash operations."""

    table = OpenHash[str, int](7)

    print("== Add ==")
    print("add('apple', 100):", table.add("apple", 100))
    print("add('banana', 200):", table.add("banana", 200))
    print("add('cherry', 300):", table.add("cherry", 300))
    print("add('apple', 999):", table.add("apple", 999))
    table.dump()

    print("\n== Search ==")
    print("search('banana'):", table.search("banana"))
    print("search('grape'):", table.search("grape"))

    print("\n== Remove ==")
    print("remove('banana'):", table.remove("banana"))
    print("remove('grape'):", table.remove("grape"))
    table.dump()


if __name__ == "__main__":
    _demo()
