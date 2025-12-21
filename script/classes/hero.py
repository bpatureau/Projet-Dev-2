from .inventaire import Inventaire

#Ensemble des variables globales
listeClasse = ["Guerrier", "Barde", "Mage"]
nomhero = {}
inventaireinit = Inventaire()
#--------------------------------------------
# Fonction de choix de classe de dÃ©part de l'instance de Hero, qui influence les compÃ©tences de dÃ©part
def choixclassehero():
    choix = input("Entrez votre choix parmi Guerrier (a), Barde (b) et Mage (c): ")
    if choix == "a":
        return listeClasse[0]
    elif choix == "b":
        return listeClasse[1]
    elif choix == "c":
        return listeClasse[2]
    else:
        return choixclassehero()
# --------------------------------------------
# Fonction de crÃ©ation de perso Hero par un input pour le nom du hero
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
            description :
                CrÃ©e un nouveau personage en choisissant un nom et une classe de personnage.
            Variable :
                - nom
                - competence (force, charisme, intelligence et agilitÃ©), en fonction de la classe
                - inventaire
    """
    def __init__(self, nominit :str , classeinit : str, inventaireinit):
        self._nom = nominit
        self._classe = classeinit
        if classeinit == 'Guerrier':
            self._competence = {"force": 20, "charisme": 10, "intelligence": 10}
        elif classeinit == 'Barde':
            self._competence = {"force": 10, "charisme": 20, "intelligence": 10}
        else:  # Mage
            self._competence = {"force": 10, "charisme": 10, "intelligence": 20}

        self.inventaire = inventaireinit

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
        return self.inventaire
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
        info += f"Argent: {self.inventaire.or_} | Objets: {len(self.inventaire.loot)}\n"
        info += f"{'=' * 50}\n"
        return info

    def modif_competence(self, competence, signe, nbr):
        """
        Fonction de modification de competence de personnage en donnant le nom du personnage
            nom : str # le nom de l'instance
            competence : str # le nom de la compÃ©tence Ã  modifier
            signe : bollean # augmenter ("+") ou diminuer ("-") une competence
            nbr : int # de combien augmenter/diminuer
        """
        if competence not in self._competence:
            print(f"Erreur : La compÃ©tence '{competence}' n'existe pas.")
            return
        if signe == "+":
            self._competence[competence] += nbr
        else: #max(0, résultat)-> le plus grand des deux est prix entre 0 et le résultat du calcul, donc 0 est le min
            self._competence[competence] = max(0, self._competence[competence] - nbr)
#--------------------------------------------
