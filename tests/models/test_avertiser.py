import unittest

from models import Advertiser


class TestAdvertiser(unittest.TestCase):

    @staticmethod
    def add_clicks(advertiser: Advertiser, clicks: int):
        for i in range(clicks):
            advertiser.inc_clicks()

    def test_get_total_clicks(self):
        self.add_clicks(Advertiser(), 20)
        self.add_clicks(Advertiser(), 42)
        self.add_clicks(Advertiser(), 23)
        self.assertEqual(20 + 42 + 23, Advertiser.get_total_clicks())
        Advertiser.get_objects().clear()

    def test_id_inc(self):
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

