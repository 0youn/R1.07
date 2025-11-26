# Version avec "for"

import time

# Demander à l'utilisateur un nombre entier positif
n = int(input("Entrez un nombre entier positif : "))

# Boucle for pour le compte à rebours
for i in range(n, -1, -1):  # de n jusqu'à 0 inclus
    print(i)
    time.sleep(1)  # pause d'1 seconde

print("Temps écoulé !")

# Version avec "while"
"""
import time

# Demander à l'utilisateur un nombre entier positif
n = int(input("Entrez un nombre entier positif : "))

# Boucle while pour le compte à rebours
while n >= 0:
    print(n)
    time.sleep(1)  # pause d'1 seconde
    n -= 1  # décrémenter n

print("Temps écoulé !")
"""