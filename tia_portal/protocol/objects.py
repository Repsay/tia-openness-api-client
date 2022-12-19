

from typing import Optional, Protocol, TypeVar, Generic

P = TypeVar("P")
_V = TypeVar("_V")

class TiaObject(Generic[_V], Protocol):
    @property
    def value(self) -> Optional[_V]:
        ...

    @value.setter
    def value(self, value: Optional[_V]) -> None:
        ...

    @value.getter
    def value(self) -> Optional[_V]:
        ...