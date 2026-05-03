"""Trial `Node` implementation for hash with a code test."""

from __future__ import annotations

from collections.abc import Hashable
from dataclasses import InitVar, dataclass, field
from typing import final


@dataclass(slots=True)
@final
class Node[KEY: Hashable, VALUE]:
    """Node for a singly linked list used in hash table chaining.

    Inheritance prohibited. Unhashable. Static guarantees-centric and not guaranteed at runtime.

    Attributes:
        key_init (`KEY`): Hash key. Becomes read-only. It's available to access by `key`.
        value (`VALUE`): Node value.
        next_node (`Node[KEY, VALUE] | None`): Link to the next node.
    """

    key_init: InitVar[KEY]
    _key: KEY = field(init=False)
    value: VALUE
    next_node: Node[KEY, VALUE] | None = None

    def __post_init__(self, key_init: KEY) -> None:
        self._key = key_init

    @property
    def key(self) -> KEY:
        """Read-only key."""
        return self._key
