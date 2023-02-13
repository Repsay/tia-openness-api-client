""" Composition protocol. This is a protocol for a composition of objects."""
from __future__ import annotations
from typing import Any, Optional, Protocol, Self, TypeVar, Iterator

from tia_portal.protocol.objects import TiaObject

T = TypeVar("T", covariant=True)


class Composition(TiaObject, Protocol[T]):
    """Composition protocol. This is a protocol for a composition of objects."""

    def __init__(self, parent: Any):
        ...

    def __iter__(self) -> Iterator[T]:
        ...

    def find(self, name: str) -> Optional[T]:
        ...


class CompositionItem(TiaObject, Protocol):
    """Composition item protocol. This is a protocol for an item in a composition of objects."""

    def __init__(self, parent: Composition[Self], name: str):  # type: ignore
        ...
