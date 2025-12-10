from liste_de_choix import *
from hero import *

class Aventure:
    def __init__(self, nom:str, hero:Hero):
        self.nom = nom
        self.hero = hero
        self.pnjs = {}
        self.choixActuel=[]
    def __str__(self):
        return f"""Bienvenu dans l'aventure {self.nom},
 le héros {self.hero},
 avec les PNJ: {', '.join(self.pnjs.keys())},
 j'ai comme choix actuel: {self.choixActuel} """
    def get_PNJ(self):
        return self.pnjs
    
def creationAventure():
    nomAventure = input("Entrez le nom de votre aventure: ")
    hero = creationhero()
    aventure = Aventure(nomAventure, hero)
    return aventure

aventureTest = creationAventure()   
aventureTest.createChoixActuel()
print(aventureTest)
