class ListeDeChoix:
    def __init__(self, nom):
        self.nom = nom
    def __str__(self):
        return f"Bienvenu dans la liste de choix {self.nom}"
    
listeDeChoixTest = ListeDeChoix("Piège")
print(listeDeChoixTest)