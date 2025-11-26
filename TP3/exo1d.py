X = float(input("Entrez une valeur X supérieure à 1 : "))

somme = 0
N = 0

while somme + N <= X:
    somme += N
    N += 1

# Quand la boucle s'arrête, N est trop grand de 1, donc on retire 1
N -= 1

print("Le plus grand nombre N tel que la somme de 0 à N soit ≤ X est :", N)