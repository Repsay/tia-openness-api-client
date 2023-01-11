from abc import abstractmethod
from typing import Any, Optional, Protocol


class TiaObject(Protocol):
    @property
    @abstractmethod
    def value(self) -> Optional[Any]:
        ...

    @value.setter
    @abstractmethod
    def value(self, value: Optional[Any]) -> None:
        ...
