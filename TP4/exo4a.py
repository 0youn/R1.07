# Initialisation

L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]

element_frequent = L1[0]
max_occ = 0

# Parcours de la liste
for i in range(len(L1)):
    courant = L1[i]

    # Comptage manuel du nombre d'occurrences
    occ = 0
    for j in range(len(L1)):
        if L1[j] == courant:
            occ += 1

    # On garde le premier élément ayant la fréquence max
    if occ > max_occ:
        max_occ = occ
        element_frequent = courant

print(f"Le nombre le plus frequent dans la liste est le : {element_frequent} ({max_occ} x)")