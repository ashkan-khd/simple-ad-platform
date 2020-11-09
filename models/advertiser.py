from __future__ import annotations

from functools import reduce
from typing import Dict

from models import BaseAdvertising
from models.utils import BaseModel


class Advertiser(BaseAdvertising, BaseModel):
    __objects: Dict[int, Advertiser] = {}

    @staticmethod
    def get_objects() -> Dict[int, Advertiser]:
        return Advertiser.__objects

    @staticmethod
    def get_total_clicks() -> int:
        if len(Advertiser.__objects) == 0:
            return 0
        return reduce \
            (lambda cl1, cl2: cl1 + cl2,
             list(map(lambda advertiser_id: Advertiser.__objects[advertiser_id].get_clicks(), Advertiser.__objects)))

    __name: str = ''

    def __init__(self, name: str = '') -> None:
        super().__init__(Advertiser)
        Advertiser.__objects[self.id] = self
        self.__name = name

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str):
        self.__name = name

    def describe_me(self):
        print("Advertiser extends BaseAdvertising and BaseModel contains all the necessary fields for an advertiser "
              "entity.")

    @classmethod
    def help(cls) -> str:
        return 'Advertiser: \n' \
               '\tobjects: private, static, List<Advertiser>\n' \
               '\tname: private, string\n' \
               '\tclicks: private, int\n' \
               '\tviews: private, int\n'
