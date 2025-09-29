from classes.Personnage import Personnage
from classes.Objet import Objet

mario = Personnage("Mario", 100, 15)
mario.addObjets(Objet("potion 20 pv", "soin", 20))
mario.addObjets(Objet("potion 30 pv", "soin", 30))

bowser = Personnage("Bowser", 100, 20)

while mario.pv != 0 and bowser.pv != 0:
    mario.subirDegat(bowser.pa)
    bowser.subirDegat(mario.pa)
    potions = mario.getObjets("soin")
    if len(potions) > 0:
        mario.utiliserObjet(potions[0])

if mario.pv != 0:
    print("Mario a gagné")
else:
    print("Bowser a gagné")