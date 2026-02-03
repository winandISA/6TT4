#5
class A:
    def __init__(self):
        self.x = 5
obj = A()
print(obj.x)
#10
class A:
    def __init__(self):
        print('A')
class B(A):
    def __init__(self):
        super().__init__()
        print('B')
obj = B()

#12
class Voiture:
    def __init__(self, marque):
        self.marque = marque
v = Voiture('Renault')
print(v.marque)

#15
class Animal:
    def parler(self):
        print('Je parle')
a = Animal()
a.parler()

#16
class Personne:
    def __init__(self, nom):
        self.nom = nom
p = Personne('Alice')
print(p.nom)

#17
class C:
    def __init__(self):
        self.val = 10
    def afficher(self):
        print(self.val)
c = C()
c.afficher()

#18
class Compte:
    def __init__(self, solde):
        self.solde = solde
c = Compte(100)
print(c.solde)
#19
class Livre:
    def __init__(self, titre):
        self.titre = titre
l = Livre('Python')
print(l.titre)
#20
class Rectangle:
    def __init__(self, l, h):
        self.l = l
        self.h = h
    def surface(self):
        return self.l * self.h
r = Rectangle(3, 4)
print(r.surface())
