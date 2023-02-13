""" TIA Portal objects protocol. This is a protocol for TIA Portal objects."""
from abc import abstractmethod
from typing import Any, Optional, Protocol


class TiaObject(Protocol):
    """TIA Portal objects protocol. This is a protocol for TIA Portal objects."""

    @property
    @abstractmethod
    def value(self) -> Optional[Any]:
        ...

    @value.setter
    @abstractmethod
    def value(self, value: Optional[Any]) -> None:
        ...
