# Auteur : Dehoux Arthur
# Titre : Coffee Shop - Fichier de test
# Description : Générer un système de gestion de produits pour un coffee shop.


from classes import (
    Produit,
    Boisson,
    BoissonAvecSupplement,
    ProduitSolide,
    Croissant,
    Muffin,
)


def afficher_details(Produit):
    """Affiche les informations principales d'un produit."""
    print(Produit.description())
    print(f"  Prix HT  : {Produit.calculer_prix_ht():.2f} €")
    print(f"  TVA      : {Produit.calculer_tva():.2f} €")
    print(f"  Prix TTC : {Produit.calculer_prix_ttc():.2f} €")

    # Si c'est un produit solide, on affiche s'il est servi chaud
    if isinstance(Produit, ProduitSolide):
        try:
            chaud = ProduitSolide.est_chaud(Produit)
            print(f"  Servi chaud : {'oui' if chaud else 'non'}")
        except AttributeError:
            # Au cas où est_chaud n'aurait pas été implémentée
            pass

    print("-" * 40)


def main():
    # Quelques exemples de produits à tester

    # Boissons simples
    cafe = Boisson("Café noir", 2.00)
    the = Boisson("Thé vert", 2.50)

    # Boisson avec supplément
    cafe_lait = BoissonAvecSupplement(
        "Café",      # nom
        2.00,        # prix_base
        "lait",      # supplément
        0.30         # coût du supplément
    )

    # Produits solides (pâtisseries)
    croissant_froid = Croissant("Croissant nature", 2.10, chauffe=False)
    croissant_chaud = Croissant("Croissant chaud", 2.10, chauffe=True)

    muffin_froid = Muffin("Muffin chocolat", 2.80, chauffe=False)
    muffin_chaud = Muffin("Muffin chocolat chaud", 2.80, chauffe=True)

    # Liste polymorphe de produits
    produits = [
        cafe,
        the,
        cafe_lait,
        croissant_froid,
        croissant_chaud,
        muffin_froid,
        muffin_chaud,
    ]

    # Affichage des détails pour chaque produit
    for p in produits:
        afficher_details(p)


if __name__ == "__main__":
    main()
