# Auteur: Dehoux Arthur
# Titre: Coffee Shop - Module des classes de produits solide
# Description: Définit les classes de produit solide pour un coffee shop.

# Import
from abc import ABC, abstractmethod
from ..produit import Produit


class ProduitSolide(Produit, ABC):
    def __init__(self, nom: str, prix_base: float, chauffe: bool):
        """Initialise un produit solide avec un nom, un prix de base et s'il est chauffé."""
        super().__init__(nom, prix_base)
        self.chauffe = chauffe

    def calculer_tva(self) -> float:
        """Calcule la TVA à partir du prix hors taxe (évite la récursion)."""
        return self.calculer_prix_ht() * 0.06

    def est_chaud(self) -> bool:
        """Retourne si le produit est servi chaud."""
        return self.chauffe


### Classes Filles de ProduitSolide ###

class Croissant(ProduitSolide):
    def __init__(self, nom: str, prix_base: float, chauffe: bool):
        """Initialise un croissant avec un nom, un prix de base et s'il est chauffé."""
        super().__init__(nom, prix_base, chauffe)
        if self.chauffe:
            self.prix_base += 0.20  # Supplément pour croissant chaud

    def calculer_prix_ht(self) -> float:
        """Calcule le prix hors TVA."""
        return self.prix_base


class Muffin(ProduitSolide):
    def __init__(self, nom: str, prix_base: float, chauffe: bool):
        """Initialise un muffin avec un nom, un prix de base et s'il est chauffé."""
        super().__init__(nom, prix_base, chauffe)
        if self.chauffe:
            self.prix_base += 0.30

    def calculer_prix_ht(self) -> float:
        """Calcule le prix hors TVA."""
        return self.prix_base
