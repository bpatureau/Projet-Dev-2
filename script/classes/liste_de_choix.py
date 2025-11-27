class ListeDeChoix:
    """Classe représentant un node de l'histoire avec ses choix"""
    
    def __init__(self, id_node, description):
        self.id = id_node
        self.__description = description
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
    
    @property
    def description(self):
        description = f"\n{'#'*60}\n"
        description += f"{self.__description}\n"
        description += f"{'#'*60}\n\n"
        return description
    
    def afficher(self, hero, affinites):
        """Retourne l'affichage du node avec les choix disponibles"""
        affichage = f"{self.description}\n"
        
        propositions_dispo = self.obtenir_propositions_disponibles(hero, affinites)
        
        if not propositions_dispo:
            affichage += "Aucun choix disponible...\n"
            return affichage
        
        affichage += "Que voulez-vous faire?\n"
        affichage += "-" * 50 + "\n"
        
        for i, prop in enumerate(propositions_dispo, 1):
            affichage += f"{i}. {prop['texte']}\n"
        
        affichage += "-" * 50 + "\n"
        
        return affichage
    
 # --- Classes factices pour tester ---

class InventaireTest:
    def __init__(self, objets=None, or_=0):
        self.objets = objets or []
        self.or_ = or_
    
    def contient(self, objet):
        return objet in self.objets


class HeroTest:
    def __init__(self, objets=None, or_=0, caracteristiques=None):
        self.inventaire = InventaireTest(objets, or_)
        self.caracteristiques = caracteristiques or {}


# --- Création d'un node pour les tests ---

node = ListeDeChoix(1, "Vous êtes devant une porte mystérieuse.")


# --- Ajout de propositions variées ---

node.ajouter_proposition(
    texte="Ouvrir la porte",
    consequence="La porte s'ouvre.",
    prerequis=None
)

node.ajouter_proposition(
    texte="Forcer la porte",
    consequence="Vous forcez la porte.",
    prerequis={"caracteristique": "force", "valeur_min": 5}
)

node.ajouter_proposition(
    texte="Utiliser la clé en argent",
    consequence="La clé ouvre la porte.",
    prerequis={"objet": "clé en argent"}
)

node.ajouter_proposition(
    texte="Soudoyer le garde",
    consequence="Le garde vous laisse passer.",
    prerequis={"pnj": "gardien", "affinite_min": 3}
)

node.ajouter_proposition(
    texte="Payer le garde",
    consequence="Vous payez le garde.",
    prerequis={"or_min": 10}
)


# --- Définition d'un héros test ---

hero = HeroTest(
    objets=["clé en argent"],
    or_=12,
    caracteristiques={"force": 4}
)

affinites = {"gardien": 2}


# --- Tests ---

print("\n=== PROPOSITIONS DISPONIBLES ===")
props = node.obtenir_propositions_disponibles(hero, affinites)
for p in props:
    print("-", p["texte"])

print("\n=== AFFICHAGE ===")
print(node.afficher(hero, affinites))

