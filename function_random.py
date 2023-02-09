from random import sample
ma_liste = ["Hamidé", "Nil", "Hassan", "Ezechiel", "Succès", "Elie", "Bray", "Innocent", "Hamza", "Bertrand", "Issa", "Julie", "Exaucé", "Yannick", "Sevrin", "Hyppolite", "Seraphin", "Sakayo"]
liste_randomise = []
groupe = 1
for i in ma_liste:
    if len(ma_liste) <= 5:
        break
    liste_randomise = sample(ma_liste, 6)
    
    for elem in liste_randomise:
        ma_liste.remove(elem)
    print("Groupe N° ", groupe)
    print(liste_randomise)
    print("----------------------------------------------------------")
    groupe+=1
if ma_liste:
    print(ma_liste)
        