from pytest import raises
from unittest.mock import patch
from script.classes.hero import Hero, choixclassehero, creationhero, nomhero, inventaireinit

class TestHero:
    def test_creation_hero_guerrier(self):
        hero = Hero("Conan", "Guerrier", inventaireinit)

        assert hero.get_nom == "Conan"
        assert hero.get_classe == "Guerrier"
        assert hero.get_competence == {"force": 20, "charisme": 10, "intelligence": 10}

    def test_creation_hero_barde(self):
        hero = Hero("Magret", "Barde", inventaireinit)

        assert hero.get_nom == "Magret"
        assert hero.get_classe == "Barde"
        assert hero.get_competence == {"force": 10, "charisme": 20, "intelligence": 10}

    def test_creation_hero_detective(self):
        hero = Hero("Oudini", "Mage", inventaireinit)

        assert hero.get_nom == "Oudini"
        assert hero.get_classe == "Mage"
        assert hero.get_competence == {"force": 10, "charisme": 10, "intelligence": 20}

    # --------------------------------------------
    def test_modif_competence_augmentation(self):
        hero = Hero("Conan", "Guerrier", inventaireinit)
        hero.modif_competence("force", "+", 3)

        assert hero.get_competence["force"] == 23

    def test_modif_competence_diminution(self):
        hero = Hero("Ragnar le rouge", "Barde", inventaireinit)
        hero.modif_competence("force", "-", 1)

        assert hero.get_competence["force"] == 9  # 10 - 1 = 9

    def test_modif_competence_ne_descend_pas_sous_zero(self):
        hero = Hero("Samurai Jack", "Guerrier", inventaireinit)
        hero.modif_competence("force", "-", 25)

        assert hero.get_competence["force"] == 0  # Ne peut pas être négatif
#--------------------------------------------
class TestChoixClasseHero:
    @patch('script.classes.hero.input', return_value='1')
    def test_choix_classe_guerrier(self, mock_input):
        classe = choixclassehero()
        assert classe == "Guerrier"

    @patch('script.classes.hero.input', return_value='2')
    def test_choix_classe_barde(self, mock_input):
        classe = choixclassehero()
        assert classe == "Barde"

    @patch('script.classes.hero.input', return_value='3')
    def test_choix_classe_detective(self, mock_input):
        classe = choixclassehero()
        assert classe == "Mage"

    @patch('script.classes.hero.input', side_effect=['5', '1'])
    def test_choix_classe_invalide_puis_valide(self, mock_input):
        """
        Scénario :
        1. L'utilisateur tape '5' (invalide)
        2. L'utilisateur tape '1' (valide)
        call_count vérifie qu'il y a bien eu 2 tests
        """
        classe = choixclassehero()
        assert classe == "Guerrier"
        assert mock_input.call_count == 2  # Appelé 2 fois


class TestCreationHero:
    """
    test qui crée plusieurs hero
    """
    @patch('script.classes.hero.input', return_value='Merlin')
    @patch('script.classes.hero.choixclassehero', return_value='Mage')
    def test_creation_hero_fonction(self, mock_choix, mock_input):
        nomhero.clear()  #enlève tous les héros cré précédemment

        hero = creationhero()

        assert hero.get_nom == "Merlin"
        assert hero.get_classe == "Mage"
        assert "Merlin" in nomhero
        assert nomhero["Merlin"] == hero

    @patch('script.classes.hero.input', return_value='Lancelot')
    @patch('script.classes.hero.choixclassehero', return_value='Guerrier')
    def test_creation_hero_retour_instance(self, mock_choix, mock_input):
        nomhero.clear() #enlève tous les héros cré précédemment

        hero = creationhero()
        assert isinstance(hero, Hero)
        assert len(nomhero) == 1