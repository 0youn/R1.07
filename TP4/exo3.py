# Taille maximale des vecteurs
nMax = 3   # ou 10 si tu veux reproduire exactement l'exemple

# Déclaration des deux listes vides
v1 = []
v2 = []

# Demande de la taille effective
n = int(input(f"Quelle est la taille de vos vecteurs [entre 1 et {nMax}] ? "))

# Vérification de la validité de n
while n < 1 or n > nMax:
    print("Erreur : la valeur doit être comprise entre 1 et", nMax)
    n = int(input(f"Quelle est la taille de vos vecteurs [entre 1 et {nMax}] ? "))

# Saisie du premier vecteur
print("Saisie du premier vecteur :")
for i in range(n):
    valeur = float(input(f"v1[{i}] = "))
    v1.append(valeur)

# Saisie du second vecteur
print("Saisie du second vecteur :")
for i in range(n):
    valeur = float(input(f"v2[{i}] = "))
    v2.append(valeur)

# Calcul du produit scalaire
produit_scalaire = 0
for i in range(n):
    produit_scalaire += v1[i] * v2[i]

# Affichage du résultat
print(f"Le produit scalaire de v1 par v2 vaut {produit_scalaire}.")