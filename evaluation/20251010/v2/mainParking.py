from classes.Voiture import Voiture
from classes.Parking import Parking
from classes.TypeVehicule import TypeVehicule

monParking = Parking("monParking", 10, 2, 2)
v1STAN = Voiture("MA PLAQUE", "Audi TT", TypeVehicule.STANDARD)
monParking.garer(v1STAN)
print(monParking.places_occupee())