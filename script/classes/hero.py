from script.classes.inventaire import Inventaire

#Ensemble des variables globales
listeClasse = ["Inspecteur", "Commissaire", "Détective"]
nomhero = {}
inventaireinit = Inventaire()
#--------------------------------------------
# Fonction de choix de classe de départ de l'instance de Hero, qui influence les compétences de départ
def choixclassehero():
    choix = input("Entrez votre choix parmi Inspecteur (a), Commissaire (b) et Détective (c): ")
    if choix == "a":
        return listeClasse[0]
    elif choix == "b":
        return listeClasse[1]
    elif choix == "c":
        return listeClasse[2]
    else:
        return choixclassehero()
# --------------------------------------------
# Fonction de création de perso Hero par un input pour le nom du hero
def creationhero():
    nom = input("Entrez votre nom: ")
    classe = choixclassehero()
    nomhero[nom] = Hero(nom, classe, inventaireinit)
    return nomhero[nom]
#--------------------------------------------
class Hero:
    """
    Personage
            type : class
            description :
                Crée un nouveau personage en choisissant un nom et une classe de personnage.
            Variable :
                - nom
                - competence (force, charisme, intelligence et agilité), en fonction de la classe
                - inventaire
    """
    def __init__(self, nominit :str , classeinit : str, inventaireinit):
        self._nom = nominit
        self._classe = classeinit
        if classeinit == 'Inspecteur':
            self._competence = {"force": 20, "charisme": 10, "intelligence": 10}
        elif classeinit == 'Commissaire':
            self._competence = {"force": 10, "charisme": 20, "intelligence": 10}
        else:  # Détective
            self._competence = {"force": 10, "charisme": 10, "intelligence": 20}

        self.inventaire = inventaireinit

    @property
    def get_nom(self):
        return self._nom
    @property
    def get_competence(self):
        return self._competence
    @property
    def get_classe(self):
        return self._classe
    @property
    def get_inventaire(self):
        return self.inventaire

    def afficher_info(self):
        info = f"\n{'=' * 50}\n"
        info += f"HÉROS: {self._nom}\n"
        info += f"{'=' * 50}\n"
        info += f"Force: {self._competence['force']} | "
        info += f"Intelligence: {self._competence['intelligence']} | "
        info += f"Charisme: {self._competence['charisme']}\n"
        info += f"Or: {self.inventaire.or_} | Objets: {len(self.inventaire.loot)}\n"
        info += f"{'=' * 50}\n"
        return info

    def modif_competence(self, competence, signe, nbr):
        """
        Fonction de modification de competence de personnage en donnant le nom du personnage
            nom : str # le nom de l'instance
            competence : str # le nom de la compétence à modifier
            signe : bollean # augmenter ("+") ou diminuer ("-") une competence
            nbr : int # de combien augmenter/diminuer
        """
        if competence not in self._competence:
            print(f"Erreur : La compétence '{competence}' n'existe pas.")
            return
        if signe == "+":
            self._competence[competence] += nbr
        else: #max(0, résultat)-> le plus grand des deux est prix entre 0 et le résultat du calcul, donc 0 est le min
            self._competence[competence] = max(0, self._competence[competence] - nbr)