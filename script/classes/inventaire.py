class Inventaire:
    def __init__(self, nom):
        self.nom = nom
    def __str__(self):
        return f"Je suis l'inventaire de {self.nom}"

inventaireTest = Inventaire("Conan")
print(inventaireTest)