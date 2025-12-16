from .liste_de_choix import *
from .hero import *
import re

class Aventure:
    def __init__(self, nom:str, hero):
        self.nom = nom
        self._hero = hero
        self.pnj = {}
        self.en_cours = False
    def __str__(self):
        return f"""Bienvenu dans l'aventure {self.nom},
 le héros {self.hero}"""
    def ajouter_pnj(self, nom_pnj: str, affinite_initiale = 0):
        if not re.match(r"^[A-Za-z]+$", nom_pnj):
            print("Nom de PNJ invalide.")
            return
        self.pnj[nom_pnj] = max(0, min(100, affinite_initiale))
    def switchAdventureState(self):
        self.en_cours = not self.en_cours
    def affinite_pnj(self, nom_pnj: str, variation: int):
        if nom_pnj in self.pnj:
            nouvelle_affinite = max(0, min(100, self.pnj[nom_pnj] + variation))
            self.pnj[nom_pnj] = nouvelle_affinite
    def afficher_affinites(self):
        for nom_pnj, affinite in self.pnj.items():
            print(f"{nom_pnj}: {affinite}")
    def afficher_affinite_sup(self, affinite_min: int):
        pnj_amis = filter(lambda p: p[1] >= affinite_min, self.pnj.items())
        noms = map(lambda p: p[0], pnj_amis)
        print("PNJ amis :", list(noms))

    @property
    def get_pnj(self):
        return self.pnj
    @property
    def hero(self):
        return self._hero
    @hero.setter
    def hero(self, new_hero):
        self._hero = new_hero
    






    
def creationAventure():
    nomAventure = input("Entrez le nom de votre aventure: ")
    hero = creationhero()
    aventure = Aventure(nomAventure, hero)
    return aventure

