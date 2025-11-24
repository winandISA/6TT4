
# ------------------------------------------------------------
# Société de livraison
# ------------------------------------------------------------

class SocieteLivraison:
    def __init__(self):
        self.__transports = []

    def ajouter_transport(self, transport):
        self.__transports.append(transport)

    def get_transports(self):
        return self.__transports

    def afficher_options(self, distance_km, masse_kg, conditions_defavorables):
        print(f"--- Options pour distance={distance_km} km, masse={masse_kg} kg ---")
        for t in self.__transports:
            if not t.est_eligible(distance_km, masse_kg, conditions_defavorables):
                print(f"{t.get_nom():12s} | ERREUR: Transport non éligible pour cette masse.")
            else:
                cout = t.calculer_cout(distance_km, masse_kg)
                delai = t.calculer_delai(distance_km, conditions_defavorables)
                print(f"{t.get_nom():12s} | Coût: {cout:6.2f} € | Délai: {delai:5.2f} h")

    def filtrer_eligibles(self, distance_km, masse_kg, conditions_defavorables):
        eligibles = []
        for t in self.__transports:
            if t.est_eligible(distance_km, masse_kg, conditions_defavorables):
                t.calculer_cout(distance_km, masse_kg)
                eligibles.append(t)
        return eligibles

    def meilleur_transport(self, distance_km, masse_kg, conditions_defavorables):
        eligibles = self.filtrer_eligibles(distance_km, masse_kg, conditions_defavorables)
        if not eligibles:
            return None

        meilleur = None
        meilleur_cout = 0
        meilleur_delai = 0

        # On parcourt tous les autres pour trouver le meilleur
        for t in eligibles:
            cout = t.calculer_cout(distance_km, masse_kg)
            delai = t.calculer_delai(distance_km, conditions_defavorables)

            # On compare d'abord le coût, puis le délai si égalité
            if cout < meilleur_cout or (cout == meilleur_cout and delai < meilleur_delai):
                meilleur = t
                meilleur_cout = cout
                meilleur_delai = delai
        return meilleur

