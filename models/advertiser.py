from __future__ import annotations

from functools import reduce
from typing import List

from models import BaseModel, BaseAdvertising


class Advertiser(BaseAdvertising, BaseModel):
    __objects: List[Advertiser] = []

    @staticmethod
    def get_objects() -> List[Advertiser]:
        return Advertiser.__objects

    @staticmethod
    def get_total_clicks() -> int:
        if len(Advertiser.__objects) == 0:
            return 0
        return reduce\
            (lambda cl1, cl2: cl1 + cl2,
             list(map(lambda advertiser: advertiser._clicks, Advertiser.__objects)))

    __name: str = ''

    def __init__(self) -> None:
        super().__init__(Advertiser.__objects)
        Advertiser.__objects.append(self)

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str):
        self.__name = name

    @classmethod
    def help(cls) -> str:
        return 'Advertiser: \n' \
               '\tobjects: private, static, List<Advertiser>\n' \
               '\tname: private, string\n' \
               '\tclicks: private, int\n' \
               '\tviews: private, int\n'
