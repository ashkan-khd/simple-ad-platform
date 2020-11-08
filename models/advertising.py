from abc import ABC


class BaseAdvertising(ABC):
    _clicks: int = 0
    _views: int = 0

    def get_clicks(self) -> int:
        return self._clicks

    def get_views(self) -> int:
        return self._views

    def inc_clicks(self):
        self._clicks += 1

    def inc_views(self):
        self._views += 1
