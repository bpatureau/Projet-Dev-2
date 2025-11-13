class Aventure:
    def __init__(self, nom):
        self.nom = nom
    def __str__(self):
        return f"Bienvenu dans l'aventure {self.nom}"