import pytest
from unittest.mock import patch

from classes.aventure import Aventure

class TestAventure:
    def test_creation_aventure(self):
        aventure = Aventure("Mystery Quest", "Hero")
        assert aventure.nom == "Mystery Quest"
        assert aventure.hero == "Hero"
        assert aventure.pnj == {}

    def test_ajouter_pnj(self):
        aventure = Aventure("Mystery Quest", "Hero")
        aventure.ajouter_pnj("Alice", 50)
        assert aventure.get_pnj()["Alice"] == 50

    def test_affinite_pnj(self):
        aventure = Aventure("Mystery Quest", "Hero")
        aventure.ajouter_pnj("Alice", 50)
        aventure.affinite_pnj("Alice", 20)
        assert aventure.get_pnj()["Alice"] == 70
        aventure.affinite_pnj("Alice", -100)
        assert aventure.get_pnj()["Alice"] == 0

    def test_switch_adventure_state(self):
        aventure = Aventure("Mystery Quest", "Hero")
        assert aventure.en_cours == False
        aventure.switchAdventureState()
        assert aventure.en_cours == True
        aventure.switchAdventureState()
        assert aventure.en_cours == False
    
    def test_affinites_sup(self):
        aventure = Aventure("Mystery Quest", "Hero")
        aventure.ajouter_pnj("Alice", 80)
        aventure.ajouter_pnj("Bob", 40) 
        assert aventure.afficher_affinite_sup(50) == ["Alice"]

    def test_ajouter_pnj_invalid_name(self, capsys):
        aventure = Aventure("Mystery Quest", "Hero")
        aventure.ajouter_pnj("Alice123", 50)
        captured = capsys.readouterr()
        assert "Nom de PNJ invalide." in captured.out
        assert aventure.get_pnj() == {}
    
    
