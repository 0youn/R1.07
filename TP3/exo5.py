# Velo.py

def calculer_location(debut, fin):
    tarif_total = 0
    heures_1_euro = 0
    heures_2_euros = 0
    
    for heure in range(debut, fin):
        if 0 <= heure < 7 or 17 <= heure <= 24:
            tarif_total += 1
            heures_1_euro += 1
        else:  # 7 <= heure < 17
            tarif_total += 2
            heures_2_euros += 1
    
    print("Vous avez loué votre vélo pendant")
    if heures_1_euro > 0:
        print(f"{heures_1_euro} heure(s) au tarif horaire de 1.0 euro(s)")
    if heures_2_euros > 0:
        print(f"{heures_2_euros} heure(s) au tarif horaire de 2.0 euro(s)")
    print(f"Le montant total à payer est de {tarif_total:.1f} euro(s).")

# Programme principal
while True:
    try:
        debut = int(input("Donnez l’heure de début de la location (un entier) : "))
        fin = int(input("Donnez l’heure de fin de la location (un entier) : "))

        # Vérification des heures
        if not (0 <= debut <= 24) or not (0 <= fin <= 24):
            print("Les heures doivent être comprises entre 0 et 24 !\n")
            continue
        if debut == fin:
            print("Attention ! l’heure de fin est identique à l’heure de début.\n")
            continue
        if debut > fin:
            print("Attention ! le début de la location est après la fin ...\n")
            continue
        
        # Calcul du tarif
        calculer_location(debut, fin)
        break  # sortir de la boucle si tout est correct
    except ValueError:
        print("Veuillez entrer des nombres entiers valides.\n")