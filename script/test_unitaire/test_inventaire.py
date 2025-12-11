from script.classes.inventaire import Inventaire

class TestInventaire:
    def test_inventaire(self):
        inv = Inventaire()
        assert inv.getArgent == 0
        assert inv.getObjets() == ""

        inv.addArgent(12)
        inv.addObjets("obj1")
        assert inv.getArgent == 12
        assert inv.getObjets() == "obj1"

        inv.addArgent(5)
        inv.addObjets("obj2")
        assert inv.getArgent == 17
        assert inv.getObjets() == "obj1 obj2"