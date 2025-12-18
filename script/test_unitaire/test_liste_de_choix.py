import pytest
from classes.liste_de_choix import ListeDeChoix

class InventaireTest:
    """Classe pour simuler un inventaire"""
    def __init__(self, objets=None, or_=0):
        self.objets = objets or []
        self.or_ = or_
    
    def contient(self, objet):
        return objet in self.objets


class HeroTest:
    """Classe pour simuler un héros"""
    def __init__(self, objets=None, or_=0, caracteristiques=None):
        self.inventaire = InventaireTest(objets, or_)
        self.caracteristiques = caracteristiques or {}

class TestInit:
    """Tests du init de ListeDeChoix"""
    def test_creation_node_valide(self):
        node = ListeDeChoix("debut", "Vous êtes à l'entrée")
        assert node.id == "debut"
        assert node.propositions == []
        assert "Vous êtes à l'entrée" in node.description
    
    def test_id_vide(self):
        with pytest.raises(ValueError, match="ne peut pas être vide"):
            ListeDeChoix("", "Description")
    
    def test_id_avec_espaces(self):
        with pytest.raises(ValueError, match="espaces"):
            ListeDeChoix("node avec espaces", "Description")
    
    def test_id_avec_quotes(self):
        """Test : ID avec quotes doit lever ValueError"""
        with pytest.raises(ValueError, match="quotes"):
            ListeDeChoix("node'test", "Description")
    
    def test_description_non_string(self):
        """Test : Description non-string doit lever TypeError"""
        with pytest.raises(TypeError, match="chaîne de caractères"):
            ListeDeChoix("test", 123)
    
    def test_id_valides(self):
        """Test : IDs valides avec tirets, underscores, etc."""
        node1 = ListeDeChoix("node-1", "Test")
        node2 = ListeDeChoix("node_2", "Test")
        node3 = ListeDeChoix("Node123", "Test")
        
        assert node1.id == "node-1"
        assert node2.id == "node_2"
        assert node3.id == "Node123"