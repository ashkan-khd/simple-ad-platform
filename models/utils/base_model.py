from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Dict


class BaseModel(ABC):
    __id: int = -1
    _next_ind = 1

    def __init__(self) -> None:
        self.__id = self.__class__._next_ind
        self.__class__._next_ind += 1


    @staticmethod
    @abstractmethod
    def get_objects() -> Dict[int, BaseModel]:
        pass

    @property
    def id(self) -> int:
        return self.__id
