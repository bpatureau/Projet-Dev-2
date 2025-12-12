import pytest
from unittest.mock import patch
from script.classes.hero import Hero, choixclassehero, creationhero, nomhero, inventaireinit

class TestHero:
    def test_creation_hero_inspecteur(self):
        hero = Hero("Sherlock", "Inspecteur", inventaireinit)

        assert hero.getnom == "Sherlock"
        assert hero.getclasse == "Inspecteur"
        assert hero.getcompetence == {"force": 0, "charisme": 1, "intelligence": 2, "agilité": 1}

    def test_creation_hero_commissaire(self):
        hero = Hero("Magret", "Commissaire", inventaireinit)

        assert hero.getnom == "Magret" #coin coin commissaire
        assert hero.getclasse == "Commissaire"
        assert hero.getcompetence == {"force": 2, "charisme": 1, "intelligence": 0, "agilité": 1}

    def test_creation_hero_detective(self):
        hero = Hero("Poirot", "Détective", inventaireinit)

        assert hero.getnom == "Poirot"
        assert hero.getclasse == "Détective"
        assert hero.getcompetence == {"force": 0, "charisme": 2, "intelligence": 2, "agilité": 0}

    def test_modif_competence_augmentation(self):
        hero = Hero("Holmes", "Inspecteur", inventaireinit)
        hero.modifcompetence("force", "+", 3)

        assert hero.getcompetence["force"] == 3

    def test_modif_competence_diminution(self):
        hero = Hero("Watson", "Commissaire", inventaireinit)
        hero.modifcompetence("force", "-", 1)

        assert hero.getcompetence["force"] == 1  # 2 - 1 = 1

    def test_modif_competence_ne_descend_pas_sous_zero(self):
        hero = Hero("Lestrade", "Inspecteur", inventaireinit)
        hero.modifcompetence("force", "-", 10)

        assert hero.getcompetence["force"] == 0  # Ne peut pas être négatif


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
        """Test qu'un choix invalide redemande jusqu'à obtenir un choix valide"""
        classe = choixclassehero()
        assert classe == "Inspecteur"
        assert mock_input.call_count == 2  # Appelé 2 fois


class TestCreationHero:
    @patch('script.classes.hero.input', return_value='Columbo')
    @patch('script.classes.hero.choixclassehero', return_value='Détective')
    def test_creation_hero_fonction(self, mock_choix, mock_input):
        nomhero.clear()  # Nettoyer avant le test

        hero = creationhero()

        assert hero.getnom == "Columbo"
        assert hero.getclasse == "Détective"
        assert "Columbo" in nomhero
        assert nomhero["Columbo"] == hero

    @patch('script.classes.hero.input', return_value='Morse')
    @patch('script.classes.hero.choixclassehero', return_value='Inspecteur')
    def test_creation_hero_retour_instance(self, mock_choix, mock_input):
        nomhero.clear()

        hero = creationhero()

        assert isinstance(hero, Hero)
        assert len(nomhero) == 1