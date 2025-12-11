import pytest
from script.classes.inventaire import Inventaire

class TestInventaire:
    def test_creation_inventaire(self):
        inv = Inventaire()
        assert inv._argent == 0
        assert len(inv.objets) == 0


    def test_argent(self):
        foo = Inventaire()
        foo.argent = 12
        assert foo.argent == 12
        assert foo._argent == 12
        foo._argent = 5
        assert foo.argent == 5


    def test_argent_cas_limites(self):
        doo = Inventaire()
        doo.argent = -100
        assert doo.argent == -100
        assert doo._argent == -100

        """assert inv.getObjets() == ""

        inv.addArgent(12)
        inv.addObjets("obj1")
        assert inv.getArgent() == 12
        assert inv.getObjets() == "obj1, "

        inv.addArgent(5)
        inv.addObjets("obj2")
        assert inv.getArgent() == 17
        assert inv.getObjets() == "obj1, obj2," """