import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(100)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 1.0")

    def test_rahan_lataaminen(self):
        self.maksukortti.lataa_rahaa(100)
        self.assertEqual(str(self.maksukortti), "saldo: 2.0")

    def test_saldo_vahenee_jos_rahaa_tarpeeksi(self):
        self.maksukortti.ota_rahaa(50)
        self.assertEqual(str(self.maksukortti), "saldo: 0.5")

    def test_saldo_ei_muutu_jos_rahaa_ei_tarpeeksi(self):
        self.maksukortti.ota_rahaa(200)
        self.assertEqual(str(self.maksukortti), "saldo: 1.0")

    def test_true_jos_rahat_riittivat(self):
        self.assertEqual(self.maksukortti.ota_rahaa(50), True)

    def test_false_jos_rahat_eivat_riittaneet(self):
        self.assertEqual(self.maksukortti.ota_rahaa(200), False)