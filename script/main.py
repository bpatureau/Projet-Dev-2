from classes import Hero, Inventaire, ListeDeChoix, Aventure


class InterfaceCLI:

    def __init__(self):
        self.aventure = None

    def afficher_titre(self):
        titre = ("\n" + "="*60)
        titre += (f"    L'ASCENSION DU HÉROS - AVENTURE TEXTUELLE")
        titre += (f"="*60 + "\n")
        print(titre)
# -----------------------------------
def main():
    """
    Fonction pour lancer le jeu
    """
    interface = InterfaceCLI()

if __name__ == '__ main __' :
    main()