class Inventaire:
    def __init__(self):
        self._argent = 0
        self.objets = []

    def __str__(self):
        return (f"argent : {self.argent} \n"
                f"objets : {self.objets}")

    @property
    def argent(self):
        return self._argent

    @argent.setter
    def argent(self, num):
        self._argent = num

"""
    def getObjets(self):
        out=""
        for objet in self.objets:
            out+=f"{objet}, "
        return out


    def addObjets(self, obj):
        self.objets.append(obj)
        return self.objets
#-----------------------------------
inventaireTest = Inventaire()
print(inventaireTest)
"""