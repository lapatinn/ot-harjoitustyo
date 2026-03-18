import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(500)

    # Kassapääte yleiset
    def test_aluksi_oikea_rahasumma(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_aluksi_ei_edullisia_myyty(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_aluksi_ei_maukkaita_myyty(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kassapaate_rahaa_euroina_toimii(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.00)
    # Kassapääte käteisostot
    def test_edullinen_kateisosto_kasvattaa_kassaa(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_maukas_kateisosto_kasvattaa_kassaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_edullinen_kateisosto_vaihtoraha_oikein(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(250), 10)

    def test_maukas_kateisosto_vaihtoraha_oikein(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(450), 50)

    def test_edullinen_kateisosto_kasvattaa_myytyja_lounaita(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_maukas_kateisosto_kasvattaa_myytyja_lounaita(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_edullinen_kateisosto_riittamaton_summa_ei_kasvata_kassaa(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_maukas_kateisosto_riittamaton_summa_ei_kasvata_kassaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_edullinen_kateisosto_riittamaton_summa_palauttaa_kaikki_rahat(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(200), 200)

    def test_maukas_kateisosto_riittamaton_summa_palauttaa_kaikki_rahat(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(300), 300)

    def test_edullinen_kateisosto_riittamaton_summa_ei_kasvata_lounaita(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukas_kateisosto_riittamaton_summa_ei_kasvata_lounaita(self):
        self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    # Kassapääte korttiostot
    def test_onnistunut_edullinen_korttiosto_palauttaa_true(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)

    def test_onnistunut_maukas_korttiosto_palauttaa_true(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)

    def test_onnistunut_edullinen_korttiosto_kasvattaa_lounaita(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_onnistunut_maukas_korttiosto_kasvattaa_lounaita(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_edullinen_kortilla_ei_tarpeeksi_rahaa_ei_muuta_kortin_saldoa(self):
        maksukortti = Maksukortti(200)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)

        self.assertEqual(maksukortti.saldo, 200)

    def test_maukas_kortilla_ei_tarpeeksi_rahaa_ei_muuta_kortin_saldoa(self):
        maksukortti = Maksukortti(200)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)

        self.assertEqual(maksukortti.saldo, 200)

    def test_edullinen_kortilla_ei_tarpeeksi_rahaa_ei_kasvata_lounaita(self):
        maksukortti = Maksukortti(200)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)

        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukas_kortilla_ei_tarpeeksi_rahaa_ei_kasvata_lounaita(self):
        maksukortti = Maksukortti(200)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)

        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_edullinen_kortilla_ei_tarpeeksi_rahaa_palauttaa_false(self):
        maksukortti = Maksukortti(200)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(maksukortti), False)
    
    def test_maukas_kortilla_ei_tarpeeksi_rahaa_palauttaa_false(self):
        maksukortti = Maksukortti(200)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(maksukortti), False)

    def test_edullinen_korttiosto_ei_muuta_kassan_rahamaaraa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_maukas_korttiosto_ei_muuta_kassan_rahamaaraa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    # Maksukortti
    def test_kortin_lataus_kasvattaa_kortin_saldoa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 100)
        self.assertEqual(self.maksukortti.saldo, 600)

    def test_kortin_lataus_kasvattaa_kassan_saldoa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100100)

    def test_kortin_lataus_negatiivisella_summalla_ei_kasvata_kortin_saldoa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -100)
        self.assertEqual(self.maksukortti.saldo, 500)