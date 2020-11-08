import unittest

from models import Advertiser
from models.ad import Ad


class TestAd(unittest.TestCase):

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

    def test_inc_clicks(self):
        advertiser = Advertiser()
        ad1 = self.create_advertiser_ad(advertiser, 20, 10)
        self.assertEqual(20, ad1.get_clicks())
        self.assertEqual(10, ad1.get_views())
        ad2 = self.create_advertiser_ad(advertiser, 15, 5)
        ad3 = self.create_advertiser_ad(advertiser, 30, 10)
        self.assertEqual(ad1.get_clicks() + ad2.get_clicks() + ad3.get_clicks(), advertiser.get_clicks())
        self.assertEqual(ad1.get_views() + ad2.get_views() + ad3.get_views(), advertiser.get_views())

