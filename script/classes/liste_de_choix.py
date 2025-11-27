class ListeDeChoix:
    """Classe représentant un node de l'histoire avec ses choix"""
    
    def __init__(self, id_node, description):
        self.id = id_node
        self.description = description
        self.propositions = []
    
    def ajouter_proposition(self, texte: str, consequence: str, 
                           suivant = None, 
                           prerequis = None,
                           defaite = False):
        """Ajoute une proposition de choix"""
        proposition = {
            "texte": texte,
            "prerequis": prerequis,
            "consequence": consequence,
            "suivant": suivant,
            "defaite": defaite
        }
        self.propositions.append(proposition)
    
    def obtenir_propositions_disponibles(self, hero, affinites):
        """Retourne la liste des propositions disponibles selon les prérequis"""
        disponibles = []
        
        for prop in self.propositions:
            if self._verifier_prerequis(prop["prerequis"], hero, affinites):
                disponibles.append(prop)
        
        return disponibles
    
    def _verifier_prerequis(self, prerequis, 
                           hero, affinites):
        """Vérifie si les prérequis d'un choix sont satisfaits"""
        if prerequis is None:
            return True
        
        # Vérifier objet requis
        if "objet" in prerequis:
            if not hero.inventaire.contient(prerequis["objet"]):
                return False
        
        # Vérifier caractéristique minimale
        if "caracteristique" in prerequis:
            carac_nom = prerequis["caracteristique"]
            carac_min = prerequis.get("valeur_min", 0)
            if hero.caracteristiques.get(carac_nom, 0) < carac_min:
                return False
        
        # Vérifier affinité avec PNJ
        if "pnj" in prerequis:
            pnj_nom = prerequis["pnj"]
            affinite_min = prerequis.get("affinite_min", 0)
            if affinites.get(pnj_nom, 0) < affinite_min:
                return False
        
        # Vérifier or minimum
        if "or_min" in prerequis:
            if hero.inventaire.or_ < prerequis["or_min"]:
                return False
        
        return True
    


