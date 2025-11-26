inferieur_10 = 0
entre_10_15 = 0
superieur_15 = 0

for i in range(10):
    valeur = float(input(f"Entrez la valeur réelle n°{i+1} (entre 0 et 20) : "))

    # Tant que la valeur n'est pas correcte, on redemande
    while valeur < 0 or valeur > 20:
        print("Valeur invalide ! Elle doit être comprise entre 0 et 20.")
        valeur = float(input(f"Entrez à nouveau la valeur n°{i+1} : "))

    # Classification
    if valeur < 10:
        inferieur_10 += 1
    elif valeur < 15:
        entre_10_15 += 1
    else:
        superieur_15 += 1

# Affichage des résultats
print("Nombre de valeurs < 10 :", inferieur_10)
print("Nombre de valeurs ≥ 10 et < 15 :", entre_10_15)
print("Nombre de valeurs ≥ 15 :", superieur_15)