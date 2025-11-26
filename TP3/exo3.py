import random

# Tirage aléatoire du nombre mystère entre 0 et 100
nombre_mystere = random.randint(0, 100)

# Initialisation du compteur de tentatives
tentatives = 0

print("Bienvenue dans le jeu du nombre mystère !")
print("Je pense à un nombre entre 0 et 100. Devinez lequel !")

# Boucle principale du jeu
while True:
    # Demander à l'utilisateur de deviner
    essai = int(input("Votre proposition : "))
    tentatives += 1  # incrémenter le compteur
    
    if essai < nombre_mystere:
        print("C'est plus grand !")
    elif essai > nombre_mystere:
        print("C'est plus petit !")
    else:
        print(f"Félicitations ! Vous avez trouvé le nombre mystère en {tentatives} essais !")
        break  # sortir de la boucle si trouvé