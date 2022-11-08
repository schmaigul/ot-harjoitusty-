import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.kortti = Maksukortti(1000)

    def test_luodun_kassapaatteen_oikeus_rahamaara(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_luodun_kassapaatteen_oikeus_lounaita_myyty(self):
        lounaita_myyty = self.kassapaate.edulliset + self.kassapaate.maukkaat
        self.assertEqual(lounaita_myyty, 0)

    def test_oikea_rahamaara_kassa_edullinen_kateinen(self):
        self.kassapaate.syo_edullisesti_kateisella(300)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_oikea_lounaiden_maara_edullinen_kateinen(self):
        self.kassapaate.syo_edullisesti_kateisella(300)

        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_oikea_vaihtoraha_kassa_edullinen_kateinen(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(300), 60)

    def test_oikea_rahamaara_kassa_maukas_kateinen(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_oikea_lounaiden_maara_maukas_kateinen(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)

        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_oikea_vaihtoraha_kassa_maukas_kateinen(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)

    def test_maksu_ei_riittava_edullinen_vaihtoraha(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(200), 200)

    def test_maksu_ei_riittava_edullinen_rahamaara(self):
        self.kassapaate.syo_edullisesti_kateisella(200)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_maksu_ei_riittava_lounaiden_maara_edullinen(self):
        self.kassapaate.syo_edullisesti_kateisella(200)

        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maksu_ei_riittava_maukas_vaihtoraha(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(200), 200)

    def test_maksu_ei_riittava_maukas_rahamaara(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_maksu_ei_riittava_lounaiden_maara_maukas(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)

        self.assertEqual(self.kassapaate.maukkaat, 0)

    #Korttiosto läpi toiminta
    def test_korttiosto_edullinen_saldo(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 7.60 euroa")

    def test_korttiosto_edullinen_palautus(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.kortti), True)

    def test_korttiosto_edullinen_myydyt_lounaat(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_korttiosto_maukas_saldo(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 6.00 euroa")

    def test_korttiosto_maukas_palautus(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.kortti), True)

    def test_korttiosto_maukas_myydyt_lounaat(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    #Korttiosto toimii sekä edullisten että maukkaiden lounaiden osalta

    #--> Edulliset
    def test_korttiosto_edullinen_ei_lapi_korttisaldo(self):
        kortti = Maksukortti(200)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(str(kortti), "Kortilla on rahaa 2.00 euroa")

    def test_korttiosto_edullinen_ei_lapi_kassasaldo(self):
        kortti = Maksukortti(200)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_korttiosto_edullinen_ei_lapi_palautus(self):
        kortti = Maksukortti(200)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(kortti), False)

    def test_korttiosto_edullinen_ei_lapi_lounaiden_maara(self):
        kortti = Maksukortti(200)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassapaate.edulliset, 0)

    #--> Maukkaat
    def test_korttiosto_maukas_ei_lapi_korttisaldo(self):
        kortti = Maksukortti(200)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(str(kortti), "Kortilla on rahaa 2.00 euroa")

    def test_korttiosto_maukas_ei_lapi_kassasaldo(self):
        kortti = Maksukortti(200)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_korttiosto_maukkas_ei_lapi_palautus(self):
        kortti = Maksukortti(200)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(kortti), False)

    def test_korttiosto_edullinen_ei_lapi_lounaiden_maara(self):
        kortti = Maksukortti(200)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    #Rahan lataaminen

    def test_lataaminen_saldo(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, 100)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 11.00 euroa")
    
    def test_lataaminen_rahamaara(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100100)

    def test_lataaminen_ei_onnistu(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, -10)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
