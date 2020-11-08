from __future__ import annotations

from typing import List

from models import BaseModel, ForeignKey, Advertiser, BaseAdvertising


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

    def __init__(self) -> None:
        super().__init__(Ad.__objects)

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
        self.__advertiser = ForeignKey(advertiser.get_id(), Advertiser)

    def inc_clicks(self):
        super(Ad, self).inc_clicks()
        self.__advertiser.object().inc_clicks()

    def inc_views(self):
        super(Ad, self).inc_views()
        self.__advertiser.object().inc_views()
