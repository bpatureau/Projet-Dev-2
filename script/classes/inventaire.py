class Inventaire:
    def __init__(self):
        self.argent = 0
        self.objets = []

    def __str__(self):
        return (f"argent : {self.argent} \n"
                f"objets : {self.objets}")

    @property
    def getArgent(self):
        return self.argent

    def getObjets(self):
        out=""
        for objet in self.objets:
            out+=f"{objet}, "
        return out

    def addArgent(self, num):
        self.argent+=num
        return self.argent

    def addObjets(self, obj):
        self.objets.append(obj)
        return self.objets
#-----------------------------------
inventaireTest = Inventaire()
print(inventaireTest)
