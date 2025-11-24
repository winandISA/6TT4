from classes.Entreprise import SocieteLivraison
from classes.Transport import *
# ------------------------------------------------------------
# Tests de démonstration
# ------------------------------------------------------------

societe = SocieteLivraison()
societe.ajouter_transport(Velo("Vélo", 20, 5))
societe.ajouter_transport(Camionnette("Camionnette", 70, 15))
societe.ajouter_transport(Drone("Drone", 60, 8))

# Cas 1
societe.afficher_options(distance_km=8, masse_kg=1, conditions_defavorables=False)
meilleur = societe.meilleur_transport(8, 1, False)
if meilleur:
    print("➡️  Meilleur choix :", meilleur.get_nom())

print()

# Cas 2
societe.afficher_options(distance_km=35, masse_kg=12, conditions_defavorables=True)
meilleur = societe.meilleur_transport(35, 12, True)
if meilleur:
    print("➡️  Meilleur choix :", meilleur.get_nom())
