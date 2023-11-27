def ajouter_mangue():
    fruits = ["pomme", "cerise", "orange", "Melon"]
    index = 2
    fruits.insert(index, "Mangue")
    return fruits

resultat_attendu = ajouter_mangue()
print(resultat_attendu)