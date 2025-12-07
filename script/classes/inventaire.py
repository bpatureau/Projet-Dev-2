class Inventaire:
    def __init__(self):
        self.argent = 0
        self.objets = []
    def __str__(self):
        return (f"argent : {self.argent} \n"
                f"objets : {self.objets}")
    def getArgent(self):
        return self.argent
#-----------------------------------
#inventaireTest = Inventaire()
#print(inventaireTest)