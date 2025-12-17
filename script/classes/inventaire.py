class Inventaire:
    def __init__(self):
        self.argent = 0
        self.loot = []
    
    @property
    def or_(self):
        """Alias pour argent (compatibilité)"""
        return self.argent
    
    @or_.setter
    def or_(self, valeur):
        self.argent = valeur
    
    def __str__(self):
        """
        Retourne l'affichage total de l'inventaire
        """
        affichage = f"\n{'=' * 50}\n"
        affichage += f"INVENTAIRE\n"
        affichage += f"{'=' * 50}\n"
        affichage += f"Argent: {self.argent} pièces\n"
        affichage += f"Objets ({len(self.loot)}):\n"
        if self.loot:
            for i, objet in enumerate(self.loot, 1):
                affichage += f"  {i}. {objet}\n"
        else:
            affichage += "  (vide)\n"
        affichage += f"{'=' * 50}\n"
        return affichage
    
    def afficher(self):
        """Méthode pour afficher l'inventaire (appelée dans main.py)"""
        return self.__str__()
# -----------------------------------
    @property
    def get_argent(self):
        return self.argent
    @get_argent.setter
    def get_argent(self, valeur):
        self.argent = valeur
# -----------------------------------
# fonction d'Inventaire
    def ajouter_objet(self, objet):
        """
        Ajoute un objet à la liste loot
        """
        self.loot.append(objet)
    def retirer_objet(self, objet):
        """
        Retire un objet de la liste loot
        """
        if objet in self.loot:
            self.loot.remove(objet)
            return True
        return False
    def contient(self, objet):
        """
        Vérifie si l'inventaire contient un objet précis
        """
        return objet in self.loot
    def ajouter_argent(self, montant):
        """
        Ajoute de l'argent
        """
        self.argent += montant
    def retirer_argent(self, montant):
        """
        Retire de l'argent si possible
        """
        if self.argent >= montant:
            self.argent -= montant
            return True
        return False