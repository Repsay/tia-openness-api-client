from __future__ import annotations
from typing import Any, Generic, Optional, Protocol, Self, TypeVar

from objects import TiaObject

T = TypeVar("T", covariant=True)
_V = TypeVar("_V")
P = TypeVar("P")


class Composition(TiaObject[_V], Generic[T, _V], Protocol):
    def __init__(self, parent: Any):
        ...

    def __iter__(self) -> T:
        ...

class CompositionItem(TiaObject[_V], Generic[_V], Protocol):
    def __init__(self, parent: Composition[Self, _V], name: str):
        ...

    @staticmethod
    def find(object: Composition[T, Any], name: str) -> Optional[T]:
        ...