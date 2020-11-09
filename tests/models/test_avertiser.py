import unittest

from models import Advertiser


class TestAdvertiser(unittest.TestCase):

    @staticmethod
    def re_init_models():
        Advertiser.get_objects().clear()

    @staticmethod
    def add_clicks(advertiser: Advertiser, clicks: int):
        for i in range(clicks):
            advertiser.inc_clicks()

    def test_get_total_clicks(self):
        self.re_init_models()
        clicks_list = [20, 42, 33, 14, 55]
        for clicks in clicks_list:
            self.add_clicks(Advertiser(), clicks)

        self.assertEqual(sum(clicks_list), Advertiser.get_total_clicks())
        Advertiser.get_objects().clear()

    def test_id_inc(self):
        self.re_init_models()
        try:
            Advertiser()
            advertisers = Advertiser.get_objects()
            self.assertEqual(1, len(advertisers))
            try:
                Advertiser()
                self.assertEqual(2, len(advertisers))
            except Exception:
                self.fail("Exception in making ID")
        except Exception:
            self.fail("Exception in making ID")

