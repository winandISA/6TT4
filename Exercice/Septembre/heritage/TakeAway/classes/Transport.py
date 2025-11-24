
class Transport:
    def __init__(self, nom, vitesse_kmh, cout_base):
        self.__nom = nom
        self.__vitesse_kmh = vitesse_kmh
        self.__cout_base = cout_base

    # ---------- Getters ----------
    def get_nom(self):
        return self.__nom

    def get_vitesse_kmh(self):
        return self.__vitesse_kmh

    def get_cout_base(self):
        return self.__cout_base

    # ---------- Méthodes ----------
    def calculer_delai(self, distance_km, conditions_defavorables=False):
        """Calcule le délai en heures (arrondi à 2 décimales)."""
        heures = distance_km / self.__vitesse_kmh
        return round(heures, 2)

    def calculer_cout(self, distance_km, masse_kg):
        """Méthode générique à redéfinir dans les sous-classes."""
        raise NotImplementedError("Cette méthode doit être redéfinie dans la sous-classe.")

    def est_eligible(self, distance_km, masse_kg, conditions_defavorables):
        """Retourne True si le transport peut effectuer la livraison."""
        return True


# ------------------------------------------------------------
# Sous-classes
# ------------------------------------------------------------

class Velo(Transport):
    def __init__(self, nom, vitesse_kmh, cout_base):
        super().__init__(nom, vitesse_kmh, cout_base)
        self.__coefficient = 0.5
        self.__masse_max = 10

    def calculer_cout(self, distance_km, masse_kg):
        if masse_kg > self.__masse_max:
            raise ValueError(f"{self.get_nom()} : masse {masse_kg} kg > {self.__masse_max} kg.")
        return round(self.get_cout_base() + distance_km * self.__coefficient, 2)

    def est_eligible(self, distance_km, masse_kg, conditions_defavorables):
        return masse_kg <= self.__masse_max


class Camionnette(Transport):
    def __init__(self, nom, vitesse_kmh, cout_base):
        super().__init__(nom, vitesse_kmh, cout_base)
        self.__coefficient = 1.0
        self.__supplement_lourd = 10

    def calculer_cout(self, distance_km, masse_kg):
        cout = self.get_cout_base() + distance_km * self.__coefficient
        if masse_kg > 50:
            cout += self.__supplement_lourd
        return round(cout, 2)


class Drone(Transport):
    def __init__(self, nom, vitesse_kmh, cout_base):
        super().__init__(nom, vitesse_kmh, cout_base)
        self.__coefficient = 2.0
        self.__masse_max = 2

    def calculer_delai(self, distance_km, conditions_defavorables=False):
        heures = distance_km / self.get_vitesse_kmh()
        if conditions_defavorables:
            heures *= 1.2  # +20%
        return round(heures, 2)

    def calculer_cout(self, distance_km, masse_kg):
        if masse_kg > self.__masse_max:
            raise ValueError(f"{self.get_nom()} : masse {masse_kg} kg > {self.__masse_max} kg.")
        return round(self.get_cout_base() + distance_km * self.__coefficient, 2)

    def est_eligible(self, distance_km, masse_kg, conditions_defavorables):
        return masse_kg <= self.__masse_max


