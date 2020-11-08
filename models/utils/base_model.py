from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List


class BaseModel(ABC):
    __id: int = -1

    def __init__(self, objects: list) -> None:
        self.__id = (objects[-1].__id + 1 if len(objects) != 0 else 1)

    @staticmethod
    @abstractmethod
    def get_objects() -> List[BaseModel]:
        pass

    def get_id(self) -> int:
        return self.__id
