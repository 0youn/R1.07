# Demande du nombre à l'utilisateur
x = float(input("Vous cherchez la table de multiplication de quel nombre ? "))

# Création de la liste contenant les résultats
resultats = []

# Remplissage de la liste avec les valeurs de x * i (i de 0 à 9)
for i in range(10):
    resultats.append(round(x * i, 1))   # arrondi à 1 décimale comme l'exemple

# Affichage de la table en relisant la liste
for i in range(10):
    print(f"{x} * {i} = {resultats[i]}")