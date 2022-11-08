import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_rahan_lataaminen(self):
        self.maksukortti.lataa_rahaa(200)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 12.00 euroa")

    def test_rahan_ottaminen_rahaa_tarpeeksi(self):
        self.maksukortti.ota_rahaa(500)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 5.00 euroa")

    def test_saldo_ei_muutu(self):
        self.maksukortti.ota_rahaa(1100)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")


    def test_rahat_riittävät_true(self):
        self.assertEqual(self.maksukortti.ota_rahaa(500), True)

    def test_rahat_riittävät_false(self):
        self.assertEqual(self.maksukortti.ota_rahaa(1100), False)

