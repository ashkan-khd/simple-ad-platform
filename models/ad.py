from __future__ import annotations

from typing import List

from models import Advertiser, BaseAdvertising
from models.utils import BaseModel, ForeignKey


class Ad(BaseAdvertising, BaseModel):

    __objects: List[Ad] = []

    @staticmethod
    def get_objects() -> List[Ad]:
        return Ad.__objects

    __title: str = ''
    __image_url: str = ''
    __link: str = ''
    __clicks: int = ''
    __view: int = ''
    __advertiser: ForeignKey = None

    def __init__(self, title: str = '', image_url: str = '', link: str = '', advertiser: Advertiser = None) -> None:
        super().__init__(Ad.__objects)
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
        self.__advertiser = ForeignKey(advertiser.get_id(), Advertiser)

    def describe_me(self):
        print("Ad entity holds necessary fields for an advertisement and it also has a foreign key to its advertiser.")

    def inc_clicks(self):
        super(Ad, self).inc_clicks()
        self.__advertiser.object().inc_clicks()

    def inc_views(self):
        super(Ad, self).inc_views()
        self.__advertiser.object().inc_views()
