import re


class PrerequisInvalideError(Exception):
    """Exception pour un prérequis invalide"""
    pass

class PropositionInvalideError(Exception):
    """Exception pour une proposition mal construite"""
    
    def __init__(self, champ, valeur_recue, type_attendu="str"):
        self.champ = champ
        self.valeur_recue = valeur_recue
        self.type_attendu = type_attendu
        self.type_recu = type(valeur_recue).__name__
        
        # Message dynamique généré automatiquement
        message = (
            f"Erreur sur le champ '{champ}' : "
            f"type {self.type_recu} reçu, {type_attendu} attendu. "
            f"Valeur : {repr(valeur_recue)}"
        )
        super().__init__(message)

class ListeDeChoix:
    """Classe représentant un node de l'histoire avec ses choix"""
    
    def __init__(self, id_node, description):
        """
        Crée un nouveau node de l'histoire.
        
        Préconditions:
            - id_node ne doit pas être vide
            - id_node ne doit pas contenir d'espaces, quotes ou backslashes
            - description doit être de type str
        
        Postconditions:
            - self.id contient l'id du node
            - self.__description contient la description
            - self.propositions est une liste vide
        """
        if not id_node:
            raise ValueError("L'id_node ne peut pas être vide")
        if re.search(r'[\s\'"\\]', str(id_node)):
                raise ValueError("L'id_node ne peut pas contenir d'espaces, quotes ou backslashes")
        if not isinstance(description, str):
            raise TypeError(f"La description doit être une chaîne de caractères (str), pas {type(description).__name__}")
        
        self.id = id_node
        self.__description = description
        self.propositions = []
    
    def ajouter_proposition(self, texte: str, consequence: str, suivant = None, prerequis = None, defaite = False):
        """
        Ajoute une proposition de choix au node.
        
        Préconditions:
            - texte doit être une chaîne non vide
            - consequence doit être une chaîne non vide
            - defaite doit être un booléen
            - prerequis doit être None ou un dictionnaire
        
        Postconditions:
            - Une nouvelle proposition est ajoutée à self.propositions
            - La proposition contient : texte, prerequis, consequence, suivant, defaite
            - len(self.propositions) a augmenté de 1
        """
        if not texte or not isinstance(texte, str):
            raise PropositionInvalideError("texte", texte, type_attendu="str non vide")
        if not consequence or not isinstance(consequence, str):
            raise PropositionInvalideError("consequence", consequence, type_attendu="str non vide")
        if not isinstance(defaite, bool):
            raise PropositionInvalideError("défaite", defaite, type_attendu="bool")
        
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
            raise PrerequisInvalideError("Les prerequis doivent être un dictionnaire")
        
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