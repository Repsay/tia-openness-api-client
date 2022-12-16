from enum import Enum


class TIAVersion(Enum):
    V15 = "15"
    V15_1 = "15_1"
    V16 = "16"
    V17 = "17"

    @property
    def value(self) -> str:
        return super().value
