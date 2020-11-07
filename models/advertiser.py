from __future__ import annotations

from functools import reduce
from typing import List

from models import BaseModel


class Advertiser(BaseModel):
    __objects: List[Advertiser] = []

    @staticmethod
    def get_objects():
        return Advertiser.__objects

    @staticmethod
    def get_total_clicks():
        if len(Advertiser.__objects) == 0:
            return 0
        return reduce\
            (lambda cl1, cl2: cl1 + cl2,
             list(map(lambda advertiser: advertiser.__clicks, Advertiser.__objects)))

    __name: str = ''
    __clicks: int = 0
    __views: int = 0

    def __init__(self) -> None:
        super().__init__(Advertiser.__objects)
        Advertiser.__objects.append(self)

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str):
        self.__name = name

    def get_clicks(self) -> int:
        return self.__clicks

    def get_views(self) -> int:
        return self.__views

    def inc_clicks(self):
        self.__clicks += 1

    def inc_views(self):
        self.__views += 1

    @classmethod
    def help(cls) -> str:
        return 'Advertiser: \n' \
               '\tobjects: private, static, List<Advertiser>\n' \
               '\tname: private, string\n' \
               '\tclicks: private, int\n' \
               '\tviews: private, int\n'
