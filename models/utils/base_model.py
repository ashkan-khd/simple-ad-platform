from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Dict


class BaseModel(ABC):
    __id: int = -1

    def __init__(self) -> None:
        self.__id = self._get_next_ind

    @staticmethod
    @abstractmethod
    def get_objects() -> Dict[int, BaseModel]:
        pass

    @property
    def id(self) -> int:
        return self.__id

    @property
    @abstractmethod
    def _get_next_ind(self):
        pass
