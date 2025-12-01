# Auteur: Dehoux Arthur
# Titre: Coffee Shop - Module des classes de produits
# Description: Définit les classes de produits pour un coffee shop.

# Import
from abc import ABC, abstractmethod


class Produit(ABC):
    def __init__(self, nom: str, prix_base: float):
        """Initialise un produit avec un nom et un prix de base."""
        if prix_base < 0:
            raise ValueError("prix_base doit être positif")
        self.nom = str(nom)
        self.prix_base = float(prix_base)

    ### Méthodes abstraites ###
    @abstractmethod
    def calculer_prix_ht(self) -> float:
        """Calcule le prix hors TVA."""
        raise NotImplementedError

    @abstractmethod
    def calculer_tva(self) -> float:
        """Calcule la TVA."""
        raise NotImplementedError

    ### Méthodes concrètes ###
    def calculer_prix_ttc(self) -> float:
        """Calcule le prix toutes taxes comprises."""
        return self.calculer_prix_ht() + self.calculer_tva()

    def description(self) -> str:
        """Retourne une description du produit."""
        return f"Produit: {self.nom} - {self.calculer_prix_ttc():.2f}€ (TTC)"

