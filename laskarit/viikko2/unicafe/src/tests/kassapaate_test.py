import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(500)

    def test_luotu_kassapaate_on_olemassa(self):
        self.assertNotEqual(self.kassapaate, None)

    def test_luotu_kassapaate_oikea_rahamaara(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_luotu_kassapaate_oikea_lounasmaara_edullinen(self):
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_luotu_kassapaate_oikea_lounasmaara_maukas(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_kateinen_kassa_muuttuu_riittava_edullinen(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
    
    def test_kateinen_kassa_muuttuu_riittava_maukas(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        
    def test_kateinen_lounasmaara_muuttuu_riittava_edullinen(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.edulliset, 1)
        
    def test_kateinen_lounasmaara_muuttuu_riittava_maukas(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_kateinen_vaihtoraha_riittava_edullinen(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(300), 60)
    
    def test_kateinen_vaihtoraha_riittava_maukas(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)

    def test_kateinen_kassa_ei_muutu_ei_riittava_edullinen(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_kateinen_kassa_ei_muutu_ei_riittava_maukas(self):
        self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        
    def test_kateinen_lounasmaara_ei_muutu_ei_riittava_edullinen(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.edulliset, 0)
        
    def test_kateinen_lounasmaara_ei_muutu_ei_riittava_maukas(self):
        self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_kateinen_vaihtoraha_ei_riittava_edullinen(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(200), 200)
    
    def test_kateinen_vaihtoraha_ei_riittava_maukas(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(300), 300)
    
    def test_kortti_saldo_muuttuu_riittava_edullinen(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 260)
    
    def test_kortti_saldo_muuttuu_riittava_maukas(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 100)
    
    def test_kortti_lounasmaara_muuttuu_riittava_edullinen(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)
        
    def test_kortti_lounasmaara_muuttuu_riittava_maukas(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_kortti_palauttaa_true_riittava_edullinen(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)
        
    def test_kortti_palauttaa_true_riittava_maukas(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)

    def test_kortti_saldo_ei_muutu_ei_riittava_edullinen(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 20)

    def test_kortti_saldo_ei_muutu_ei_riittava_maukas(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 100)

    def test_kortti_lounasmaara_ei_muutu_ei_riittava_edullinen(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 2)
        
    def test_kortti_lounasmaara_ei_muutu_ei_riittava_maukas(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_kortti_palauttaa_false_ei_riittava_edullinen(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), False)
        
    def test_kortti_palauttaa_false_ei_riittava_maukas(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), False)
    
    def test_kortti_kassa_ei_muutu_edullinen(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kortti_kassa_ei_muutu_maukas(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_kortti_lataus_saldo_muuttuu(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 500)
        self.assertEqual(self.maksukortti.saldo, 1000)
    
    def test_kortti_lataus_kassa_muuttuu(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100500)

    def test_kortti_lataus_negatiivinen_saldo_ei_muutu(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -500)
        self.assertEqual(self.maksukortti.saldo, 500)
        
    def test_kortti_lataus_negatiivinen_kassa_ei_muutu(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)