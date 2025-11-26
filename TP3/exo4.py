# Fonction pour calculer la factorielle avec une boucle for
def factorielle_for(n):
    resultat = 1
    print(f"Calcul de {n}! avec la boucle FOR :")
    for i in range(1, n + 1):
        resultat *= i
        print(f"Étape {i} : {resultat}")
    return resultat

# Fonction pour calculer la factorielle avec une boucle while
def factorielle_while(n):
    resultat = 1
    i = 1
    print(f"Calcul de {n}! avec la boucle WHILE :")
    while i <= n:
        resultat *= i
        print(f"Étape {i} : {resultat}")
        i += 1
    return resultat

# Programme principal
n = int(input("Entrez un entier positif pour calculer sa factorielle : "))

# Choix du type de boucle
choix = input("Voulez-vous utiliser la boucle 'for' ou 'while' ? ").strip().lower()

if choix == "for":
    factorielle = factorielle_for(n)
elif choix == "while":
    factorielle = factorielle_while(n)
else:
    print("Choix invalide. Veuillez taper 'for' ou 'while'.")
    factorielle = None

if factorielle is not None:
    print(f"\nLa factorielle de {n} est : {factorielle}")