from .inventaire import Inventaire

#Ensemble des variables globales
listeClasse = ["Guerrier", "Barde", "Mage"]
nomhero = {}
inventaireinit = Inventaire()
#--------------------------------------------
# Fonction de choix de classe de départ de l'instance de Hero, qui influence les compétences de départ
def choixclassehero():
    choix = input("Entrez votre choix parmi Guerrier (1), Barde (2) et Mage (2): ")
    if choix == "1":
        return listeClasse[0]
    elif choix == "2":
        return listeClasse[1]
    elif choix == "3":
        return listeClasse[2]
    else:
        return choixclassehero()
# --------------------------------------------
# Fonction de création de perso Hero par un input pour le nom du hero
def creationhero():
    nom = input("Entrez votre nom: ")
    if not nom:
        nom = "Aventurier"
    classe = choixclassehero()
    nomhero[nom] = Hero(nom, classe, inventaireinit)
    return nomhero[nom]
#--------------------------------------------
class Hero:
    """
    Personage
            type : class
            desc :
                Crée un nouveau personage en choisissant un nom et une classe de personnage.
            Attributs :
                - _nom
                - _classe
                - _competence (force, charisme, intelligence), en fonction de la classe
                - _inventaire
    """
    def __init__(self, nominit :str , classeinit : str, inventaireinit):
        """
        PRE :
            - nominit est un string
            - classinit est un string contenant soit Guerrier, Barde ou Mage
            - inventaireinit est une instance de classe
        POST :
            - assigne à l'instance de Hero les attributs _nom, _classe, _competence et _inventaire
        """
        if not isinstance(nominit, str):
            raise TypeError("nominit n'est pas un string")
        else:
            self._nom = nominit

        if not isinstance(classeinit, str):
            raise TypeError("classeinit n'est pas un string")
        else:
            self._classe = classeinit

        self._inventaire = inventaireinit

        if classeinit == 'Guerrier':
            self._competence = {"force": 20, "charisme": 10, "intelligence": 10}
        elif classeinit == 'Barde':
            self._competence = {"force": 10, "charisme": 20, "intelligence": 10}
        elif classeinit == 'Mage':
            self._competence = {"force": 10, "charisme": 10, "intelligence": 20}
        else:
            raise ValueError("Classe invalide")
    # --------------------------------------------
    @property #getter
    def get_nom(self):
        return self._nom
    @property #getter
    def get_competence(self):
        return self._competence
    @property #getter
    def get_classe(self):
        return self._classe
    @property #getter
    def get_inventaire(self):
        return self._inventaire
    @get_competence.setter
    def get_competence(self, competence):
        self._competence = competence
    # --------------------------------------------
    def afficher_info(self):
        info = f"\n{'=' * 50}\n"
        info += f"HÉROS: {self._nom}\n"
        info += f"{'=' * 50}\n"
        info += f"Classe: {self._classe}\n | "
        info += f"Force: {self._competence['force']} | "
        info += f"Intelligence: {self._competence['intelligence']} | "
        info += f"Charisme: {self._competence['charisme']}\n"
        info += f"argent: {self._inventaire.or_} | Objets: {len(self._inventaire.loot)}\n"
        info += f"{'=' * 50}\n"
        return info

    def modif_competence(self, competence, signe, nbr):
        """
        Fonction de modification de competence de personnage en donnant le nom de la competence, + ou - pour indiquer l'ajout
        ou la diminution de la competence et nbr.

        PRE
            - competence est un string et existe dans l'attribut objet _competence de Hero
            - signe est un string et a deux valeurs possible + et -
            - nbr est un integer

        POST
            - assigne la competence modifiée à l'attribut objet _competence de Hero et peut pas être en dessous de zero
        """
        if competence not in self._competence:
           raise ValueError(f"Erreur : La compétence '{competence}' n'existe pas.")
        if signe == "+":
            self._competence[competence] += nbr
        elif signe == "-":
            self._competence[competence] = max(0, self._competence[competence] - nbr)
        else:
            raise ValueError("signe est invalide")
#--------------------------------------------