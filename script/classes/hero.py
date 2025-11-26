#Ensemble des variables globales
listeClasse = ["Inspecteur", "Commissaire", "Détective"]

# --------------------------------------------
# Fonction de création de perso Hero
def creationhero():
    nom = input("Entrez votre nom: ")
    classe = choixclassehero()
    nouveauhero = Hero(nom, classe)

    return nouveauhero

#--------------------------------------------
# Fonction de choix de classe de départ de l'instance de Hero
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

#--------------------------------------------
"""
Personage
        type : class
        description :
            À chaque nouvelle partie crée un nouveau personage en choisissant un nom et une classe de personnage.
        Variable :
            - nom
            - competence (force, charisme, intelligence et agilité), en fonction de la classe
            - inventaire
            
"""
class Hero:
    def __init__(self, nom :str , classe : str ):
        self.nom = nom
        self.classe = classe
        if classe == 'Inspecteur':
            self.competence = {"force":0,"charisme":1,"intelligence":2, "agilité":1}
        elif classe == 'Commissaire':
            self.competence = {"force": 2, "charisme": 1, "intelligence": 0, "agilité": 1}
        else: # Détective
            self.competence = {"force": 0, "charisme": 2, "intelligence": 2, "agilité": 0}

        #self. inventaire = appel inventaire.py et lier à instance d'inventaire

    def __str__(self):
        return f"{self.nom} est un {self.classe} personage et à {self.competence['force']} de force"
# --------------------------------------------
#TEST

michel = creationhero()
print(michel)
#--------------------------------------------