class Hero:
    def __init__(self, nom):
        self.nom = nom
    def __str__(self):
        return f"Je suis le héro {self.nom}"
    
heroTest = Hero("Conan")
print(heroTest)
