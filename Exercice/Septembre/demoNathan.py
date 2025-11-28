# Rappel sur les if’s et les boucles.
# if
# if et while utilisent des conditions pour décider quel chemin le code va suivre.
# les opérateurs des conditions sont
# == pour tester une égalité
# != pour tester une différence
# >, >=, <, <= pour tester un ordre de grandeur.
# quand tu écris "a==5" le compilateur va renvoyer un booléen (True, False)


# Dans l'exemple suivant, c'est un peu comme si a avait une valeur de 7 et donc a == 10 renverra faux.
# donc ce code va toujours écrire B
if False:
   print("A")
else:
   print("B")


#if simple
#demander le type de jeu qu'il aime a un utilisateur et lui donner un exemple.
a = input("Quel type de jeu aimes-tu? FPS, BR, STR")
if a == "FPS":
   print("tu aimeras CSGO")
elif a == "BR":
   print("tu aimeras Fortnite")
else:
   print("tu aimeras Starcraft")



#if imbriqué
a = input("quel age as-tu?")
# utilise la méthode isdigit qui renvoie True si la string contient au moins un caractère ET que tous les caractères sont des chiffres.
if a.isdigit():
   a = int(a)
   if a < 18:
       print("tu es mineur")
   else:
       print("tu es majeur")
else:
   print("la valeur entrée n'est pas un nombre")


#if avec not, and et or
# not va inverser le résultat d'un test. True --> False et False--> True
# and renverra True si les deux propositions à droite et à gauche sont True
# or renverra True si au moins une des deux propositions à droite et à gauche est True
# La priorité de l'interprétation de ces 3 opérateurs est NOT, AND puis seulement OR.
# en cas de conditions complexes qui mélangent les opérateurs, une bonne pratique est d'entourer
# les différentes propositions avec des parenthèses pour améliorer la lisibilité.
a = 15
b = 10
if a > 10 or b > 10:
   print("cas 1")
elif a < 20 and b < 10:
   print("cas 2")
#dans cet exemple, si on ne met pas les parenthèses le résultat sera différent
elif ((not a < 20) or b > 10) and (a > 10 and b < 20):
   print("cas 3")
#dans cet exemple les parenthèses ne changent rien
elif ((not a < 20) and b > 10) or (a > 10 and b < 20):
   print("cas 3")
else:
   print("cas 4")


# Boucles
# while
# structure de base on utilise une condition pour décider la sortie.
# le programme va boucler 20 fois et afficher les nombres de 0 à 19
a = 0
while a < 20:
   print(a)
   a += 1


# structure qui se base sur une réponse d'un utilisateur
# le programme va continuer tant que l'utilisateur ne répondra pas oui
a = ""
while a != "oui":
   a = input("veux tu arrêter?(oui/non").lower() #utiliser lower ou upper force la réponse de l'utilisateur en minuscule/majuscule pour ne pas devoir gérer les problèmes de case
   if a == "non":
       print("ok, on continue")


# alternative avec un not
a = ""
while not a == "oui":
   a = input("veux tu arrêter?(oui/non").lower() #utiliser lower ou upper force la réponse de l'utilisateur en minuscule/majuscule pour ne pas devoir gérer les problèmes de case
   if a == "non":
       print("ok, on continue")



# structure contrôlée par un booléen (demande un contrôle supplémentaire mais plus lisible)
continuer = True
# ici, le compilateur râle un peu parce qu'on compare un booléen à True alors qu'on peut juste lui donner le booléen(alternative 1)
while continuer == True:
   a = input("veux tu arrêter?(oui/non").lower() #utiliser lower ou upper force la réponse de l'utilisateur en minuscule/majuscule pour ne pas devoir gérer les problèmes de case
   if a == "non":
       print("ok, on continue")
   else:
       continuer = False


# alternative 1 (plus correcte)
continuer = True
while continuer:
   a = input("veux tu arrêter?(oui/non").lower() #utiliser lower ou upper force la réponse de l'utilisateur en minuscule/majuscule pour ne pas devoir gérer les problèmes de case
   if a == "non":
       print("ok, on continue")
   else:
       continuer = False


# alternative 2 avec un booléen initialisé à False
trouver = False
while not trouver:
   a = input("as-tu trouvé?(oui/non").lower() #utiliser lower ou upper force la réponse de l'utilisateur en minuscule/majuscule pour ne pas devoir gérer les problèmes de case
   if a == "non":
       print("ok, on continue")
   else:
       trouver = True







# structure permettant de compter de 1 à 20 sauf si un nombre équivalent est généré
import random


continuer = True
a = 1
while continuer and a != "oui":
   print(a)
   if a == random.randint(1, 20):
       print("Les chiffres sont identiques")
       continuer = False


# A proscrire ABSOLUMENT cela risque de provoquer de gros problèmes de logique quand vos programmes deviendront complexes
# break sort de la boucle en cours
while True:
   a = input("veux tu arrêter?(oui/non").lower() #utiliser lower ou upper force la réponse de l'utilisateur en minuscule/majuscule pour ne pas devoir gérer les problèmes de case
   if a == "non":
       print("ok, on continue")
   else:
       break


#Boucle for
# le programme va boucler sur tous les éléments d'une liste.
# ici, chaque passage dans la boucle (itération) va placer dans la variable bonjour la valeur suivante de la liste l
l = ["Hello", "Bonjour", "Hola", "Hi"]
for bonjour in l:
   print(bonjour)


# cas particulier: range(5).
# range est une fonction qui renvoie une liste qui va contenir tous les nombres entre 0 et la valeur passée -1
# [0, 1, 2, 3, 4] pour range(5)
for i in range(5):
   print(i)


# for ne peut pas être interrompu (vu qu'on se refuse d'utiliser le break) donc il faut
# le réserver à un usage nécessitant de parcourir complètement une liste.
# une recherche d'un élément dans une liste sera plus optimisé avec un while bien écrit
# même si cela nécessite (un peu) plus de code.
