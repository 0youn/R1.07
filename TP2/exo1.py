# Saisie des valeurs
x = int(input("Entrez x : "))
y = int(input("Entrez y : "))

# Affichage avant permutation
print("Avant permutation:")
print("x :", x)
print("y :", y)

# Permutation des valeurs
x, y = y, x

# Affichage après permutation
print("Après permutation:")
print("x :", x)
print("y :", y)