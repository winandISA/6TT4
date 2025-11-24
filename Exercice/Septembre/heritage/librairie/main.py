# ============================================================
# Script de tests "manuel" pour SocieteLibrairie
# (teste toutes les méthodes publiques demandées)
# ============================================================

# On suppose que les classes suivantes existent et respectent l'énoncé :
# Article, Univers, Goodie(Article, Univers), Livre(Article, Univers),
# Manga(Livre), Classique(Livre), SocieteLibrairie.

def afficher_liste_articles(titre, articles):
    print(f"\n{titre}")
    if not articles:
        print("  (aucun)")
        return
    for a in articles:
        # On affiche nom, univers, prix, stock
        try:
            nom = a.get_nom()
            uni = a.get_nom_univers()
            prix = a.get_prix()
            stock = a.get_stock()
            print(f"  - {nom} [{uni}] | {prix:.2f} € | stock={stock}")
        except Exception:
            # Si certains getters ne sont pas présents exactement comme ça,
            # adapter ici au besoin.
            print("  - (article inexploitable avec les getters attendus)")

def test_societe_librairie():
    # ------------------------------------------------------------
    # 1) Initialisation : 2 univers
    # ------------------------------------------------------------
    # Dans l’héritage multiple, l’univers est porté par chaque Article concret.
    # On prépare juste les noms d’univers que l’on va utiliser.
    U1 = "Marvel"
    U2 = "Les Tuniques Bleues"

    # ------------------------------------------------------------
    # 2) Création d’articles (goodies, mangas, classiques)
    # ------------------------------------------------------------
    # Goodies (héritent de Article et Univers)
    g1 = Goodie("T-shirt Iron Man", 19.99, 3, U1)
    g2 = Goodie("Mug Capitaine", 12.50, 1, U1)

    # Livres classiques
    c1 = Classique("Bluecoats Tome 1", 14.90, 2, "Cauvin & Lambil", 48, U2)
    c2 = Classique("Bluecoats Tome 2", 14.90, 0, "Cauvin & Lambil", 48, U2)  # stock 0 pour tester l'achat impossible

    # Manga
    m1 = Manga("Spider-Manga Vol.1", 7.90, 5, "A. Auteur", 180, U1, sens_lecture="droite->gauche")

    # ------------------------------------------------------------
    # 3) Société et ajout des articles (ajouter_article)
    # ------------------------------------------------------------
    societe = SocieteLibrairie()
    societe.ajouter_article(g1)
    societe.ajouter_article(g2)
    societe.ajouter_article(c1)
    societe.ajouter_article(c2)
    societe.ajouter_article(m1)

    # (Résultat attendu)
    # Les 5 articles sont désormais connus de la société.

    # ------------------------------------------------------------
    # 4) Recherche par nom (chercher_article_par_nom)
    # ------------------------------------------------------------
    print("\n=== Test: chercher_article_par_nom ===")
    art = societe.chercher_article_par_nom("T-shirt Iron Man")
    print("Trouvé (T-shirt Iron Man) ?" , "Oui" if art is not None else "Non")
    # Attendu: Oui

    art = societe.chercher_article_par_nom("Inexistant")
    print("Trouvé (Inexistant) ?" , "Oui" if art is not None else "Non")
    # Attendu: Non

    # ------------------------------------------------------------
    # 5) Recherche par univers (chercher_articles_par_univers)
    # ------------------------------------------------------------
    print("\n=== Test: chercher_articles_par_univers ===")
    marvel = societe.chercher_articles_par_univers(U1)
    afficher_liste_articles(f"Articles de l'univers {U1} (attendu: T-shirt, Mug, Spider-Manga)", marvel)
    # Attendu: 3 articles Marvel (g1, g2, m1)

    tuniques = societe.chercher_articles_par_univers(U2)
    afficher_liste_articles(f"Articles de l'univers {U2} (attendu: Bluecoats Tome 1, Tome 2)", tuniques)
    # Attendu: 2 articles (c1, c2)

    vide = societe.chercher_articles_par_univers("DC")
    afficher_liste_articles("Articles de l'univers DC (attendu: aucun)", vide)
    # Attendu: aucun

    # ------------------------------------------------------------
    # 6) Achat d’un article (acheter_article) + vérification du stock
    # ------------------------------------------------------------
    print("\n=== Test: acheter_article ===")

    def stock_de(nom):
        a = societe.chercher_article_par_nom(nom)
        return a.get_stock() if a else None

    # Avant achat
    print("Stock avant (T-shirt Iron Man) :", stock_de("T-shirt Iron Man"))  # Attendu: 3

    # Achat 1
    societe.acheter_article("T-shirt Iron Man")
    print("Après 1 achat (T-shirt Iron Man) :", stock_de("T-shirt Iron Man"))  # Attendu: 2

    # Achat 2
    societe.acheter_article("T-shirt Iron Man")
    print("Après 2 achats (T-shirt Iron Man) :", stock_de("T-shirt Iron Man"))  # Attendu: 1

    # Achat 3
    societe.acheter_article("T-shirt Iron Man")
    print("Après 3 achats (T-shirt Iron Man) :", stock_de("T-shirt Iron Man"))  # Attendu: 0

    # Achat 4 (stock déjà à 0 → ne doit pas passer)
    societe.acheter_article("T-shirt Iron Man")
    print("Après 4e tentative (T-shirt Iron Man) :", stock_de("T-shirt Iron Man"))  # Attendu: 0 (inchangé)

    # Test achat sur article déjà à 0
    print("\nStock avant (Bluecoats Tome 2) :", stock_de("Bluecoats Tome 2"))  # Attendu: 0
    societe.acheter_article("Bluecoats Tome 2")
    print("Après tentative d'achat (Bluecoats Tome 2) :", stock_de("Bluecoats Tome 2"))  # Attendu: 0 (inchangé)

    # Achat d’un article qui n’existe pas
    print("\nAchat d’un article inexistant :")
    societe.acheter_article("Superman Deluxe")  # Attendu: message d’erreur ou aucun effet

    # ------------------------------------------------------------
    # Fin
    # ------------------------------------------------------------
    print("\n=== Fin des tests ===")


if __name__ == "__main__":
    test_societe_librairie()
