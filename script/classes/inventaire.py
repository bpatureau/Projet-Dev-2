class Inventaire:
    argent=0
    objets=[]
    def __init__(self, nom):
        self.nom = nom
    def __str__(self):
        return f"Je suis l'inventaire de {self.nom} et j'ai {self.argent} argent"
    def getAgrent(self):
        return argent

inventaireTest = Inventaire("Conan")
print(inventaireTest)