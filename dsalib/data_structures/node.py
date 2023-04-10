"""Node class for data structures."""

from typing import Any


class Node:
    """Node class for data structures."""

    def __init__(self, value: Any, next_node: Any = None) -> None:
        self.value = value
        self.next_node = next_node
