import unittest

from laender_match import alle_laender, finde_land


class FindeLandTest(unittest.TestCase):
    def pruefe(self, eingabe, alpha2):
        land = finde_land(eingabe)
        self.assertIsNotNone(land, f"{eingabe!r} wurde nicht gefunden")
        self.assertEqual(land.alpha2, alpha2, f"{eingabe!r}")

    def test_deutscher_und_englischer_name(self):
        self.pruefe("Deutschland", "DE")
        self.pruefe("Germany", "DE")
        self.pruefe("Spanien", "ES")
        self.pruefe("Spain", "ES")

    def test_gross_kleinschreibung_und_leerzeichen(self):
        self.pruefe("  deutschland ", "DE")
        self.pruefe("NEUSEELAND", "NZ")
        self.pruefe("new   zealand", "NZ")

    def test_iso_codes(self):
        self.pruefe("DE", "DE")
        self.pruefe("deu", "DE")
        self.pruefe("ch", "CH")
        self.pruefe("USA", "US")

    def test_umlaute_und_akzente(self):
        self.pruefe("Österreich", "AT")
        self.pruefe("Oesterreich", "AT")
        self.pruefe("Osterreich", "AT")
        self.pruefe("Türkei", "TR")
        self.pruefe("Cote d'Ivoire", "CI")
        self.pruefe("Großbritannien", "GB")
        self.pruefe("Grossbritannien", "GB")

    def test_alternativnamen(self):
        self.pruefe("Holland", "NL")
        self.pruefe("UK", "GB")
        self.pruefe("England", "GB")
        self.pruefe("Amerika", "US")
        self.pruefe("Weißrussland", "BY")
        self.pruefe("Trinidad & Tobago", "TT")

    def test_tippfehler(self):
        self.pruefe("Deutchland", "DE")
        self.pruefe("Frankriech", "FR")
        self.pruefe("Itlaien", "IT")
        self.pruefe("Switzerlnd", "CH")

    def test_aehnliche_laender_werden_nicht_verwechselt(self):
        self.pruefe("Island", "IS")
        self.pruefe("Irland", "IE")
        self.pruefe("Iceland", "IS")
        self.pruefe("Ireland", "IE")
        self.pruefe("Austria", "AT")
        self.pruefe("Australia", "AU")
        self.pruefe("Niger", "NE")
        self.pruefe("Nigeria", "NG")
        self.pruefe("Iran", "IR")
        self.pruefe("Iraq", "IQ")

    def test_kein_treffer(self):
        self.assertIsNone(finde_land(""))
        self.assertIsNone(finde_land("   "))
        self.assertIsNone(finde_land(None))
        self.assertIsNone(finde_land("XY"))
        self.assertIsNone(finde_land("Atlantis"))
        self.assertIsNone(finde_land("Kartoffel"))

    def test_rueckgabe_enthaelt_namen_und_codes(self):
        land = finde_land("Japan")
        self.assertEqual(land.alpha3, "JPN")
        self.assertEqual(land.name_de, "Japan")
        self.assertEqual(land.name_en, "Japan")

    def test_datenbestand(self):
        laender = alle_laender()
        self.assertGreaterEqual(len(laender), 195)
        self.assertEqual(len({l.alpha2 for l in laender}), len(laender))
        self.assertEqual(len({l.alpha3 for l in laender}), len(laender))


if __name__ == "__main__":
    unittest.main()
