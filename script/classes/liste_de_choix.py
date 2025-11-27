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
    