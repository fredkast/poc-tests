import os, sys
import unittest
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from classes.Ferry import Ferry

class TestFerry(unittest.TestCase):
    def test_nommage_ferry(self):
        ferry = Ferry("QueenMary2", 10,100, 100)
        attendu = "QueenMary2"
        self.assertEqual(ferry.nom, attendu)

    def test_max_voiture(self):
        ferry = Ferry("QueenMary2", 10, 100, 100)
        attendu = 100
        self.assertEqual(ferry.voitures_max, attendu)

    def test_embarquer_voiture(self):
        ferry = Ferry("QueenMary2", 1, 100, 100)
        ferry.embarquer_voiture(1)
        attendu = 1
        self.assertEqual(ferry.voitures_a_bord, attendu)

    def test_debarquer_voiture(self):
        ferry = Ferry("QueenMary2", 1, 100, 100)
        ferry.debarquer_voiture(1)
        attendu = 0
        self.assertEqual(ferry.voitures_a_bord, attendu)

    def test_changer_cie(self):
        ferry = Ferry("QueenMary2", 1, 100, 100)
        ferry.changer_cie("Brittany Ferrie")
        attendu = "Brittany Ferrie"
        self.assertEqual(ferry.cie, attendu)

    def test_changer_trajet(self):
        ferry = Ferry("QueenMary2", 1, 100, 100)
        ferry.trajet("Roscoff", "New York")
        attendu = "New York"
        self.assertEqual(ferry.port_arrivee, attendu)

    def test_changer_capitaine(self):
        ferry = Ferry("QueenMary2", 1, 100, 100)
        ferry.changer_captaine("John DOE")
        attendu = "John DOE"
        self.assertEqual(ferry.nom_capitain, attendu)

    def test_modifier_volume_cabine(self):
        ferry = Ferry("QueenMary2", 1, 100, 100)
        ferry.modifier_volume_cabine(125)
        attendu = 125
        self.assertEqual(ferry.nombre_cabine, attendu)

if __name__ == "__main__":
    unittest.main()
