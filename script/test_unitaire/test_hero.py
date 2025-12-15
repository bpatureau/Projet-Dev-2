import pytest
from unittest.mock import patch
from script.classes.hero import Hero, choixclassehero, creationhero, nomhero, inventaireinit

class TestHero:
    def test_creation_hero_inspecteur(self):
        hero = Hero("Sherlock", "Inspecteur", inventaireinit)

        assert hero.get_nom == "Sherlock"
        assert hero.get_classe == "Inspecteur"
        assert hero.get_competence == {"force": 20, "charisme": 10, "intelligence": 10}

    def test_creation_hero_commissaire(self):
        hero = Hero("Magret", "Commissaire", inventaireinit)

        assert hero.get_nom == "Magret" #coin coin commissaire
        assert hero.get_classe == "Commissaire"
        assert hero.get_competence == {"force": 10, "charisme": 20, "intelligence": 10}

    def test_creation_hero_detective(self):
        hero = Hero("Poirot", "Détective", inventaireinit)

        assert hero.get_nom == "Poirot"
        assert hero.get_classe == "Détective"
        assert hero.get_competence == {"force": 10, "charisme": 10, "intelligence": 20}

    # --------------------------------------------
    def test_modif_competence_augmentation(self):
        hero = Hero("Holmes", "Inspecteur", inventaireinit)
        hero.modif_competence("force", "+", 3)

        assert hero.get_competence["force"] == 23

    def test_modif_competence_diminution(self):
        hero = Hero("Watson", "Commissaire", inventaireinit)
        hero.modif_competence("force", "-", 1)

        assert hero.get_competence["force"] == 9  # 10 - 1 = 9

    def test_modif_competence_ne_descend_pas_sous_zero(self):
        hero = Hero("Lestrade", "Inspecteur", inventaireinit)
        hero.modif_competence("force", "-", 25)

        assert hero.get_competence["force"] == 0  # Ne peut pas être négatif
#--------------------------------------------
class TestChoixClasseHero:
    @patch('script.classes.hero.input', return_value='a')
    def test_choix_classe_inspecteur(self, mock_input):
        classe = choixclassehero()
        assert classe == "Inspecteur"

    @patch('script.classes.hero.input', return_value='b')
    def test_choix_classe_commissaire(self, mock_input):
        classe = choixclassehero()
        assert classe == "Commissaire"

    @patch('script.classes.hero.input', return_value='c')
    def test_choix_classe_detective(self, mock_input):
        classe = choixclassehero()
        assert classe == "Détective"

    @patch('script.classes.hero.input', side_effect=['z', 'a'])
    def test_choix_classe_invalide_puis_valide(self, mock_input):
        """
        Scénario :
        1. L'utilisateur tape 'z' (invalide)
        2. L'utilisateur tape 'a' (valide)
        call_count vérifie q'ils y a bien eu 2 tests
        """
        classe = choixclassehero()
        assert classe == "Inspecteur"
        assert mock_input.call_count == 2  # Appelé 2 fois


class TestCreationHero:
    """
    test qui crée plusieurs hero
    """
    @patch('script.classes.hero.input', return_value='Columbo')
    @patch('script.classes.hero.choixclassehero', return_value='Détective')
    def test_creation_hero_fonction(self, mock_choix, mock_input):
        nomhero.clear()  # Nettoyer avant le test

        hero = creationhero()

        assert hero.get_nom == "Columbo"
        assert hero.get_classe == "Détective"
        assert "Columbo" in nomhero
        assert nomhero["Columbo"] == hero

    @patch('script.classes.hero.input', return_value='Morse')
    @patch('script.classes.hero.choixclassehero', return_value='Inspecteur')
    def test_creation_hero_retour_instance(self, mock_choix, mock_input):
        nomhero.clear()

        hero = creationhero()

        assert isinstance(hero, Hero)
        assert len(nomhero) == 1