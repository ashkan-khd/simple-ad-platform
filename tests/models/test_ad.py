import unittest
from functools import reduce

from models import Advertiser
from models.ad import Ad


class TestAd(unittest.TestCase):

    @staticmethod
    def re_init_models():
        Advertiser.get_objects().clear()
        Ad.get_objects().clear()

    @staticmethod
    def add_clicks(ad: Ad, clicks: int):
        for i in range(clicks):
            ad.inc_clicks()

    @staticmethod
    def add_views(ad: Ad, views: int):
        for i in range(views):
            ad.inc_views()

    @staticmethod
    def create_advertiser_ad(advertiser: Advertiser, init_clicks: int, init_views: int):
        ad = Ad()
        ad.set_advertiser(advertiser)
        TestAd.add_clicks(ad, init_clicks)
        TestAd.add_views(ad, init_views)
        return ad

    @staticmethod
    def create_ads_from_clicks_list(advertiser, clicks_list):
        for click in clicks_list:
            TestAd.create_advertiser_ad(advertiser, click, 0)

    @staticmethod
    def create_ads_from_views_list(advertiser, views_list):
        for view in views_list:
            TestAd.create_advertiser_ad(advertiser, 0, view)

    def test_inc_clicks(self):
        self.re_init_models()

        advertiser = Advertiser()
        clicks = [20, 15, 30]
        self.create_ads_from_clicks_list(advertiser, clicks)

        self.assertEqual(reduce(lambda x, y: x + y, clicks), advertiser.get_clicks())

    def test_inc_views(self):
        self.re_init_models()

        advertiser = Advertiser()
        views = [40, 50, 10]
        self.create_ads_from_views_list(advertiser, views)

        self.assertEqual(reduce(lambda x, y: x + y, views), advertiser.get_views())

    def test_advertisers_total_clicks(self):
        self.re_init_models()

        advertiser1_clicks = [20, 10, 15, 60]
        self.create_ads_from_clicks_list(Advertiser(), advertiser1_clicks)

        advertiser2_clicks = [25, 5, 35, 40]
        self.create_ads_from_clicks_list(Advertiser(), advertiser2_clicks)

        self.assertEqual(reduce(lambda x, y: x + y, advertiser1_clicks + advertiser2_clicks),
                         Advertiser.get_total_clicks())
