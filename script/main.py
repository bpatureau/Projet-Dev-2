from classes import Hero, ListeDeChoix, Aventure, creationhero
import json
import os
from pathlib import Path

class InterfaceCLI:

    def __init__(self):
        self.aventure = None

    def afficher_titre(self):
        titre = ("\n" + "="*60)
        titre += "L'ASCENSION DU HÉROS - AVENTURE TEXTUELLE"
        titre += (f"="*60 + "\n")
        print(titre)

    def creer_nouvelle_partie(self):
        """
         Méthode effectuée lors de la sélection dans le menu d'une nouvelle partie.
         Cherche s'il y a des aventures dans le dossier aventures et les affiche.
         Appelle la méthode initialiser_monde avec le fichier json choisis.
        """
        self.afficher_titre()
        aventures = self.charger_aventures_disponibles()

        if not aventures:
            print("❌ Aucune aventure disponible dans le dossier 'aventures/'")
            print("Veuillez ajouter des fichiers JSON d'aventure dans ce dossier.")
            input("\nAppuyez sur Entrée pour retourner au menu...")
            return

        print("Aventures disponibles:")
        print("-" * 60)
        for i, av in enumerate(aventures, 1):
            print(f"{i}. {av['nom']}")
            print(f"   {av['description']}")
            print()

        while True:
            choix = input(f"Choisissez une aventure (1-{len(aventures)}): ").strip()
            if choix.isdigit() and 1 <= int(choix) <= len(aventures):
                aventure_choisie = aventures[int(choix) - 1]
                break
            print("Choix invalide!")

        hero = creationhero()
        self.aventure = Aventure(aventure_choisie["nom"], hero)

        if not self.initialiser_monde(aventure_choisie["fichier"]):
            print("\n❌ Erreur lors du chargement de l'aventure.")
            input("Appuyez sur Entrée pour retourner au menu...")
            self.aventure = None
            return

        print(f"\n✓ Aventure '{aventure_choisie['nom']}' chargée avec succès!")
        print(hero.afficher_info())

    def charger_aventures_disponibles(self):
        """
        Retourne la liste des aventures disponibles dans le dossier aventures/
        Si le dossier contenant les aventures préfaite n'existe pas, crée un dossier vide
        """
        aventures_dir = Path("aventures")

        if not aventures_dir.exists():
            print(f"⚠️ Le dossier 'aventures' n'existe pas. Création du dossier...")
            aventures_dir.mkdir(exist_ok=True)
            return []

        aventures = []
        for fichier in aventures_dir.glob("*.json"): # cherche les fichiers JSON servant de DB à une aventure préfaite
            try:
                with open(fichier, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    aventures.append({
                        "fichier": str(fichier),
                        "nom": data.get("nom", fichier.stem),
                        "description": data.get("description", "Pas de description")
                    })
            except Exception as e:
                print(f"⚠️ Erreur lors du chargement de {fichier}: {e}")
        return aventures

    def initialiser_monde(self, fichier_aventure):
        """
        Initialise le monde du jeu depuis un fichier JSON sélectionné
        """
        if not self.aventure:
            return False

        try:
            with open(fichier_aventure, 'r', encoding='utf-8') as f:
                data = json.load(f)

            self.aventure.nom = data.get("nom", "Aventure Sans Nom")

            or_depart = data.get("or_depart", 0)
            self.aventure.hero.inventaire.or_ = or_depart

            for pnj_data in data.get("pnj", []):
                nom = pnj_data.get("nom")
                affinite = pnj_data.get("affinite_initiale", 50)
                self.aventure.ajouter_pnj(nom, affinite)

            for node_data in data.get("nodes", []):
                node = ListeDeChoix(
                    node_data["id"],
                    node_data["description"]
                )

                for prop_data in node_data.get("propositions", []):
                    node.ajouter_proposition(
                        texte=prop_data["texte"],
                        consequence=prop_data["consequence"],
                        suivant=prop_data.get("suivant"),
                        prerequis=prop_data.get("prerequis"),
                        defaite=prop_data.get("defaite", False)
                    )

                self.aventure.ajouter_node(node)

            node_depart = data.get("node_depart", "debut")
            if not self.aventure.charger_node(node_depart):
                print(f"⚠️ Impossible de charger le node de départ: {node_depart}")
                return False

            self.aventure.demarrer()
            return True

        except FileNotFoundError:
            print(f"❌ Fichier non trouvé: {fichier_aventure}")
            return False
        except json.JSONDecodeError as e:
            print(f"❌ Erreur de format JSON: {e}")
            return False
        except Exception as e:
            print(f"❌ Erreur lors du chargement: {e}")
            return False

    def boucle_jeu(self):
        """
        Boucle principale du jeu, affiche les options disponibles et réagis en fonction de l'input utilisateur
        """
        if not self.aventure or not self.aventure.en_cours:
            return

        while self.aventure.en_cours:
            if self.aventure.node_actuel:
                print(self.aventure.node_actuel.afficher(
                    self.aventure.hero,
                    self.aventure.pnj_affinites
                ))

            print(self.aventure.hero.afficher_info())

            print("\nOptions: [1-9] Faire un choix | [I] Inventaire | [H] Historique | [Q] Quitter")

            commande = input("\n> ").strip().upper()

            if commande == 'Q':
                confirmation = input("Voulez-vous vraiment quitter? (O/N): ").strip().upper()
                if confirmation == 'O':
                    self.aventure.terminer()
                    print("\nMerci d'avoir joué!")
                    break

            elif commande == 'I':
                print(self.aventure.hero.inventaire.afficher())
                input("\nAppuyez sur Entrée pour continuer...")

            elif commande == 'H':
                print(f"\n{'=' * 50}")
                print("HISTORIQUE DE L'AVENTURE")
                print(f"{'=' * 50}")
                print(f"Nombre de nodes explorés: {len(self.aventure.historique)}")
                for i, node in enumerate(self.aventure.historique, 1):
                    print(f"{i}. {node.id}")
                print(f"{'=' * 50}")
                input("\nAppuyez sur Entrée pour continuer...")

            elif commande.isdigit():
                index = int(commande) - 1
                resultat = self.aventure.executer_choix(index)

                print("\n" + ">" * 50)
                print(resultat)
                print(">" * 50 + "\n")

                input("\nAppuyez sur Entrée pour continuer...")

            else:
                print("Commande invalide!")

        if self.aventure.victoire:
            print("\n" + "=" * 60)
            print("VICTOIRE!")
            print("=" * 60)
            print(f"{self.aventure.hero.nom} a triomphé de l'aventure!")
            print(f"Nodes explorés: {len(self.aventure.historique)}")
            print("=" * 60 + "\n")

        elif self.aventure.defaite:
            print("\n" + "=" * 60)
            print("DÉFAITE")
            print("=" * 60)
            print(f"{self.aventure.hero.nom} n'a pas survécu à l'aventure...")
            print(f"Nodes explorés: {len(self.aventure.historique)}")
            print("=" * 60 + "\n")

    def menu_principal(self):
        """
        Affiche le menu principal d'avant chaque partie
        """
        while True:
            self.afficher_titre()
            print("1. Nouvelle Partie")
            print("2. Quitter")

            choix = input("\nVotre choix: ").strip()

            if choix == "1":
                self.creer_nouvelle_partie()
                self.boucle_jeu()
            elif choix == "2":
                print("\nAu revoir!")
                break
            else:
                print("\nChoix invalide!")
# -----------------------------------
def main():
    """
    Fonction pour lancer le jeu en instanciant la classe InterfaceCLI et en lançant la méthode menu_principal
    """
    interface = InterfaceCLI()
    interface.menu_principal()
if __name__ == '__main__':
    main()