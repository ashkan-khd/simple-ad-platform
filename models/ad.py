from __future__ import annotations

from typing import Dict

from models import Advertiser, BaseAdvertising
from models.utils import BaseModel, ForeignKey


class Ad(BaseAdvertising, BaseModel):

    __objects: Dict[int, Ad] = {}
    __next_ind = 1

    @staticmethod
    def get_objects() -> Dict[int, Ad]:
        return Ad.__objects

    __title: str = ''
    __image_url: str = ''
    __link: str = ''
    __clicks: int = ''
    __view: int = ''
    __advertiser: ForeignKey = None

    def __init__(self, title: str = '', image_url: str = '', link: str = '', advertiser: Advertiser = None) -> None:
        super().__init__()
        Ad.__objects[self.id] = self
        Ad.__next_ind += 1
        self.__title = title
        self.__image_url = image_url
        self.__link = link
        self.set_advertiser(advertiser)

    def get_title(self) -> str:
        return self.__title

    def set_title(self, title: str):
        self.__title = title

    def get_image_url(self) -> str:
        return self.__image_url

    def set_image_url(self, image_url: str):
        self.__image_url = image_url

    def get_link(self) -> str:
        return self.__link

    def set_link(self, link: str):
        self.__link = link

    def set_advertiser(self, advertiser: Advertiser):
        if advertiser is None:
            self.__advertiser = None
            return
        self.__advertiser = ForeignKey(advertiser.id, Advertiser)

    @property
    def _get_next_ind(self):
        return Ad.__next_ind

    def describe_me(self):
        print("Ad entity holds necessary fields for an advertisement and it also has a foreign key to its advertiser.")

    def inc_clicks(self):
        super(Ad, self).inc_clicks()
        self.__advertiser.object().inc_clicks()

    def inc_views(self):
        super(Ad, self).inc_views()
        self.__advertiser.object().inc_views()
