# Auteur: Dehoux Arthur
# Titre: Coffee Shop - Module des classes de boissons
# Description: Définit les classes de Boisson pour un coffee shop.

# Import
from ..produit import Produit


class Boisson(Produit):

    TVA = 0.21  # Taux de TVA standard
    def calculer_prix_ht(self) -> float:
        """Calcule le prix hors TVA."""
        return self.prix_base

    def calculer_tva(self) -> float:
        """Calcule la TVA."""
        return self.calculer_prix_ht() * Boisson.TVA


### Classes FIlles de Boisson ###

class BoissonAvecSupplement(Boisson):
    def __init__(self, nom: str, prix_base: float, supplement: str, cout_supplement: float):
        """Initialise une boisson avec un supplément."""
        super().__init__(nom, prix_base)
        self.supplement = supplement
        self.cout_supplement = cout_supplement

    def calculer_prix_ht(self) -> float:
        """Calcule le prix hors TVA en incluant le supplément."""
        return super().calculer_prix_ht() + self.cout_supplement

    def calculer_tva(self) -> float:
        """Calcule la TVA en incluant le supplément."""
        return self.calculer_prix_ht() * Boisson.TVA

    def description(self) -> str:
        """Retourne une description de la boisson avec supplément."""
        return f"Boisson: {self.nom} avec {self.supplement} - {self.calculer_prix_ttc():.2f}€ (TTC)"
