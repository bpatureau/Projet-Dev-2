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
class TestAjouterProposition:
    """Tests de la méthode ajouter_proposition"""
    
    def test_ajout_proposition_valide(self):
        node = ListeDeChoix("test", "Test")
        node.ajouter_proposition(
            texte="Aller à gauche",
            consequence="Vous allez à gauche"
        )
        
        assert len(node.propositions) == 1
        assert node.propositions[0]["texte"] == "Aller à gauche"
        assert node.propositions[0]["consequence"] == "Vous allez à gauche"
    
    def test_ajout_proposition_avec_prerequis(self):
        node = ListeDeChoix("test", "Test")
        node.ajouter_proposition(
            texte="Utiliser clé",
            consequence="La porte s'ouvre",
            prerequis={"objet": "clé"}
        )
        
        assert node.propositions[0]["prerequis"] == {"objet": "clé"}
    
    def test_ajout_proposition_avec_defaite(self):
        node = ListeDeChoix("test", "Test")
        node.ajouter_proposition(
            texte="Abandonner",
            consequence="Vous abandonnez",
            defaite=True
        )
        
        assert node.propositions[0]["defaite"] is True
    
    def test_texte_vide_leve_exception(self):
        """Test : Texte vide doit lever ValueError"""
        node = ListeDeChoix("test", "Test")
        
        with pytest.raises(ValueError, match="texte.*non vide"):
            node.ajouter_proposition(
                texte="",
                consequence="Test"
            )
    
    def test_consequence_vide(self):
        node = ListeDeChoix("test", "Test")
        
        with pytest.raises(ValueError, match="conséquence.*non vide"):
            node.ajouter_proposition(
                texte="Test",
                consequence=""
            )
    
    def test_defaite_non_booleen(self):
        node = ListeDeChoix("test", "Test")
        
        with pytest.raises(ValueError, match="booléen"):
            node.ajouter_proposition(
                texte="Test",
                consequence="Test",
                defaite="oui"
            )
    
    def test_ajout_multiple_propositions(self):
        node = ListeDeChoix("test", "Test")
        
        node.ajouter_proposition("Choix 1", "Conséquence 1")
        node.ajouter_proposition("Choix 2", "Conséquence 2")
        node.ajouter_proposition("Choix 3", "Conséquence 3")
        
        assert len(node.propositions) == 3