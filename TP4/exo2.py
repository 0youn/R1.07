# Demande le nombre d'étudiants à l'utilisateur
nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))

# déclaration d’une liste vide qui va contenir les notes
notes = []

# variable pour la somme
somme = 0.0

# Remplissage de la liste
for i in range(nombreEtudiants):
    note = float(input(f"Note etudiant {i} : "))  # phrase contenant une variable

    # Vérification de la validité de la note
    while note < 0 or note > 20:
        print("Erreur : la note doit être comprise entre 0 et 20.")
        note = float(input(f"Note etudiant {i} : "))

    notes.append(note)
    somme += note  # on cumule la somme

# Calcul de la moyenne
moyenne = somme / nombreEtudiants

# Affichage de la moyenne
print(f"Moyenne de classe : {moyenne}")

# Affichage des écarts
print("Numéro de l’Etudiant | note | ecart a la moyenne")
for i in range(nombreEtudiants):
    ecart = notes[i] - moyenne
    print(f"{i} | {notes[i]} | {ecart}")