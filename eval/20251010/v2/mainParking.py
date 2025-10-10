from classes.Voiture import Voiture
from classes.Parking import Parking
from classes.TypeVehicule import TypeVehicule

monParking = Parking("monParking", 10, 2, 2)
v1STAN = Voiture("MA PLAQUE", "Audi TT", TypeVehicule.STANDARD)
monParking.garer(v1STAN)
for place in monParking.places_occupee():
    print(place)
print(monParking)

v1 = Voiture("AAA-111", "Audi TT", TypeVehicule.STANDARD)
v2 = Voiture("BBB-222", "Tesla", TypeVehicule.EV)
v3 = Voiture("CCC-333", "Peugeot 208", TypeVehicule.STANDARD)
v4 = Voiture("DDD-444", "Renault Zoé", TypeVehicule.EV)
v5 = Voiture("EEE-555", "Kia Soul", TypeVehicule.PMR)

monParking.garer(v1)
monParking.garer(v2)
monParking.garer(v3)
monParking.garer(v4)
monParking.garer(v5)

for place in monParking.places_occupee():
    print(place)
print(monParking)
monParking.sortir(v3)

for place in monParking.places_occupee():
    print(place)
print(monParking)