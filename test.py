class perso():
    def __init__(self, nom, attaque):
        self.nom = nom
        self.attaque = attaque

    def attaque(self):
        return self.attaque

    def defend(self):
        return self.attaque

class mage(perso):
    def __init__(self, nom, attaque, pm):
        super().__init__(nom, attaque)
        self.pm = pm

    def attaque(self):
        return super().attaque() + 1

perso = perso("moi", 5)
print(perso.nom)
mago = mage("moi", 5, 40)
print(mago.nom, mago.pm)

mago.attaque()
mago.defend()

