
import random

entree = "Appuie sur Entrée..."

print("Bienvenue !")
input(entree)
print()

print("Pense à un nombre compris entre 1 et 100 (entier évidemment)")
input()

choix_de_niveau = int(input("Choisis un niveau de difficulté : \n1. Facile \n2. Moyen \n3. Impossible \n"))

premier_essai = random.randint(1, 100)

if choix_de_niveau == 1:

    limite_min = 1
    limite_max = 100

    print("Mon premier essai :", premier_essai)

    réponse_1er_essai = input("Plus/Moins ou Correct ? ")

    while réponse_1er_essai != "Correct":

        if réponse_1er_essai == "Plus":
            limite_min = premier_essai + 1

        elif réponse_1er_essai == "Moins":
            limite_max = premier_essai - 1

        else:
            print("Réponse invalide ! Écris Plus, Moins ou Correct.")
            réponse_1er_essai = input()
            continue

        if limite_min > limite_max:
            print("Tes réponses sont incohérentes !")
            break

        deuxieme_essai = random.randint(limite_min, limite_max)

        print("Et maintenant ?", deuxieme_essai)

        premier_essai = deuxieme_essai

        réponse_1er_essai = input()

    if réponse_1er_essai == "Correct":
        print("Gg c'était cool ! (t'es éteint...)")
        print("Noob trop prévisible !")

elif choix_de_niveau == 2:
    print("Le niveau moyen arrive bientôt !")

elif choix_de_niveau == 3:
    print("Le niveau impossible arrive bientôt !")

else:
    print("Choix invalide ! Tu dois choisir 1, 2 ou 3.")
