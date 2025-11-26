N = int(input("Entrez un entier naturel N : "))

somme = 0
for i in range(N + 1):   # de 0 à N inclus
    somme += i

print("La somme des entiers de 0 à", N, "vaut :", somme)