import random
list =["Francis","Succès","Bray","Innocent","Hyppolite","Yassine","Severin","Ezechiel","Elie","Exocé","Honoré","Amédé","Nil","Julie","Bertrand","Saleh","Issa","Séraphin","Hamza","Hassan","Fourissou","Arsène","Narcisse",]
#cela contiendra une occurrence de notre liste
maListOc = list
#cette liste contiendra notre liste aléatoire
randomlist = None
groupe = 1
fin=5
#pour chaque élément de ma_list, nous randome et mettons dans notre variable
for i in list:
#Cette condition évitera les erreurs lorsque n est supérieur à 4
    if(len(list)<=fin):
        break
    randomlist = random.sample(list, 5)
    #ensuite on supprime les données déjà randomisées dans notre liste, mais la complexité est élevée pour ce petit programme
    for element in randomlist:
        list.remove(element)
    print("Groupe N°:",groupe)
    #et nous imprimons enfin notre liste randomisée
    print(randomlist)
    print("_________________________________________")
    groupe += 1
print(maListOc)