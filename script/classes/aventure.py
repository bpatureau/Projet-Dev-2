from .liste_de_choix import *
from .hero import *
import re


class pnjNonExistant(Exception):
    pass

class Aventure:
    def __init__(self, nom:str, hero):
        self.nom = nom
        self._hero = hero
        self.pnj = {}
        self.en_cours = False
        self.node_courant = None
        self.historique_nodes = []
        self.nodes={}
        self.win=False
        self.lose=False
    
    # Propriétés pour harmoniser les noms utilisés dans main.py
    @property
    def node_actuel(self):
        """Alias pour node_courant"""
        return self.node_courant
    
    @property
    def historique(self):
        """Alias pour historique_nodes"""
        return self.historique_nodes
    
    @property
    def pnj_affinites(self):
        """Alias pour pnj"""
        return self.pnj
    
    @property
    def victoire(self):
        """Alias pour win"""
        return self.win
    
    @property
    def defaite(self):
        """Alias pour lose"""
        return self.lose
    
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
        if nom_pnj not in self.pnj:
            raise pnjNonExistant(f"PNJ '{nom_pnj}' non trouvé dans l'aventure.")
        nouvelle_affinite = self.pnj[nom_pnj] + variation
        self.pnj[nom_pnj] = max(0, min(100, nouvelle_affinite))
    def afficher_affinites(self):
        for nom_pnj, affinite in self.pnj.items():
            print(f"{nom_pnj}: {affinite}")
    def afficher_affinite_sup(self, affinite_min: int):
        pnj_amis = filter(lambda p: p[1] >= affinite_min, self.pnj.items())
        noms = map(lambda p: p[0], pnj_amis)
        return(list(noms))
    def get_pnj(self):
        return self.pnj
    @property
    def hero(self):
        return self._hero
    @hero.setter
    def hero(self, new_hero):
        self._hero = new_hero
    
    def ajouter_node(self, node):
        self.nodes[node.id] = node
    def get_node(self, node_id):
        return self.nodes.get(node_id, None)
    def set_node_courant(self, node_id):
        if node_id in self.nodes:
            self.node_courant = self.nodes[node_id]
            self.historique_nodes.append(self.node_courant)
            return True
        return False

    def faire_choix(self, choix_index):
        if self.node_courant is None:
            return "Aucun node courant défini."
        
        propositions = self.node_courant.obtenir_propositions_disponibles(self._hero, self.pnj)
        if choix_index < 0 or choix_index > len(propositions):
            return "Choix invalide."
        choix = propositions[choix_index]
        if choix.get("defaite", False):
            self.en_cours = False
            self.lose = True
        if choix["suivant"]:
            if choix["suivant"] == "victoire":
                self.en_cours = False
                self.win = True
            else:
                self.set_node_courant(choix["suivant"])
        return choix["consequence"]
    
    def demarrer(self):
        """Démarre l'aventure"""
        self.en_cours = True
    
    def terminer(self):
        """Termine l'aventure"""
        self.en_cours = False
    
    def charger_node(self, node_id):
        """Charge un node comme node courant"""
        return self.set_node_courant(node_id)
    
    def executer_choix(self, choix_index):
        """Exécute un choix (wrapper pour faire_choix)"""
        return self.faire_choix(choix_index)


def creationAventure():
    nomAventure = input("Entrez le nom de votre aventure: ")
    hero = creationhero()
    aventure = Aventure(nomaventure, hero)
    return aventure