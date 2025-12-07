#Ensemble des variables globales
listeClasse = ["Inspecteur", "Commissaire", "Détective"]
nomhero = {}
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
    nomhero[nom] = Hero(nom, classe)
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
    def __init__(self, nom :str , classe : str ):
        self.nom = nom
        self.classe = classe
        if classe == 'Inspecteur':
            self.competence = {"force":0,"charisme":1,"intelligence":2, "agilité":1}
        elif classe == 'Commissaire':
            self.competence = {"force": 2, "charisme": 1, "intelligence": 0, "agilité": 1}
        else: # Détective
            self.competence = {"force": 0, "charisme": 2, "intelligence": 2, "agilité": 0}
        # self.inventaire = appel inventaire.py et lier à instance d'inventaire
    def __str__(self):
        return (f"nom : {self.nom} classe : {self.classe} \n"
                f"force : {self.competence['force']} \n"
                f"charisme : {self.competence['charisme']} \n"
                f"intelligence : {self.competence['intelligence']} \n"
                f"agilité : {self.competence['agilité']}")

    def modifcompetence(self, competence, signe, nbr):
        """
        Fonction de modification de competence de personnage en donnant le nom du personnage
            nom : str # le nom de l'instance
            competence : str # le nom de la compétence à modifier
            signe : bollean # augmenter ("+") ou diminuer ("-") une competence
            nbr : int # de combien augmenter/diminuer
        """
        if competence not in self.competence:
            print(f"Erreur : La compétence '{competence}' n'existe pas.")
            return
        if signe == "+":
            self.competence[competence] += nbr
        else: #max(0, résultat)-> le plus grand des deux est prix entre 0 et le résultat du calcul, donc 0 est le min
            self.competence[competence] = max(0, self.competence[competence] - nbr)
# --------------------------------------------