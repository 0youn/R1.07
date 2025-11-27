date = input("Entrez une date au format jjmmaaaa : ")

# Vérification du format général
if len(date) != 8:
    print("Format incorrect ! La date doit contenir exactement 8 chiffres.")
elif not date.isdigit():
    print("Format incorrect ! La date ne doit contenir que des chiffres.")
else:
    # Extraction des éléments
    jour = int(date[0:2])
    mois = int(date[2:4])
    annee = int(date[4:8])

    # Vérification du mois
    if mois < 1 or mois > 12:
        print("Date incorrecte : le mois doit être compris entre 1 et 12.")
    else:

        # Déterminer si l'année est bissextile
        bissextile = False
        if (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0):
            bissextile = True

        # Nombre de jours selon le mois
        if mois in [1, 3, 5, 7, 8, 10, 12]:
            max_jour = 31
        elif mois in [4, 6, 9, 11]:
            max_jour = 30
        else:  # février
            if bissextile:
                max_jour = 29
            else:
                max_jour = 28

        # Vérification du jour
        if jour < 1 or jour > max_jour:
            print("Date incorrecte : le jour n'est pas valide pour ce mois.")
        else:
            print("Date correcte !")