L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]

element_frequent = L1[0]
max_occ = L1.count(element_frequent)

for x in L1:
    occ = L1.count(x)

    # même règle : on ne change que si la fréquence est STRICTEMENT plus grande
    if occ > max_occ:
        max_occ = occ
        element_frequent = x

print(f"Le nombre le plus frequent dans la liste est le : {element_frequent} ({max_occ} x)")