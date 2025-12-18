import re
class ListeDeChoix:
    """Classe représentant un node de l'histoire avec ses choix"""
    
    def __init__(self, id_node, description):
        if not id_node:
            raise ValueError("L'id_node ne peut pas être vide")
        if re.search(r'[\s\'"\\]', str(id_node)):
                raise ValueError("L'id_node ne peut pas contenir d'espaces, quotes ou backslashes")
        if not isinstance(description, str):
            raise TypeError(f"La description doit être une chaîne de caractères (str), pas {type(description).__name__}")
        
        self.id = id_node
        self.__description = description
        self.propositions = []
    
    def ajouter_proposition(self, texte: str, consequence: str, 
                           suivant = None, 
                           prerequis = None,
                           defaite = False):
        """Ajoute une proposition de choix"""
        if not texte or not isinstance(texte, str):
            raise ValueError("Le texte de la proposition doit être une chaîne non vide")
        if not consequence or not isinstance(consequence, str):
            raise ValueError("La conséquence doit être une chaîne non vide")
        if not isinstance(defaite, bool):
            raise ValueError("Le paramètre 'defaite' doit être un booléen")
        
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
            try:
                if self._verifier_prerequis(prop["prerequis"], hero, affinites):
                    disponibles.append(prop)
            except (AttributeError, KeyError, TypeError):
                # Si une proposition a un problème, on la saute au lieu de crasher
                continue
        
        return disponibles
    
    def _verifier_prerequis(self, prerequis, hero, affinites):
        """Vérifie si les prérequis d'un choix sont satisfaits"""
        if prerequis is None:
            return True
        
        if not isinstance(prerequis, dict):
            raise ValueError("Les prerequis doivent être un dictionnaire")
        
        try:
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
        except (AttributeError, KeyError):
            # En cas d'erreur, on refuse l'accès au choix
            return False
    
    @property
    def description(self):
        description = f"\n{'#'*60}\n"
        description += f"{self.__description}\n"
        description += f"{'#'*60}\n\n"
        return description
    
    @description.setter
    def description(self, value):
        if not isinstance(value, str):
            raise TypeError(f"La description doit être une chaîne de caractères (str), pas {type(value).__name__}")
        self.__description = value

    def afficher(self, hero, affinites):
        """Retourne l'affichage du node avec les choix disponibles"""
        affichage = f"{self.description}\n"
        
        try:
            propositions_dispo = self.obtenir_propositions_disponibles(hero, affinites)
        except (ValueError) as e:
            affichage += f"⚠️ Erreur: {e}\n"
            return affichage
        
        if not propositions_dispo:
            affichage += "Aucun choix disponible...\n"
            return affichage
        
        affichage += "Que voulez-vous faire?\n"
        affichage += "-" * 50 + "\n"
        
        lignes = map(
            lambda item: f"{item[0]}. {item[1]['texte']}\n",
            enumerate(propositions_dispo, 1)
        )
        affichage += "".join(lignes)
        
        affichage += "-" * 50 + "\n"
        
        return affichage