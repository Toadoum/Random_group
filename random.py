import random

nil = input("entrer les noms separer d'espace : ").split(" ")
ma_list = nil
print(ma_list)
nombre = int(input("entrer le nombre de personne par groupe : "))
# nombre=int(nombre)
# this will contain an occurence of our list
maListOc = ma_list
# this list will contain our random list
random_list = None
groupe = 1
# for each element in ma_list, we randome and put into our variable
for i in ma_list:
    # This condition will avoid errors when n is greater than 4
    if (len(ma_list) <= nombre):
        random_list = ma_list
        #             print("groupe N° :", groupe)
        #             print(ma_list)
        break
    random_list = random.sample(ma_list, nombre)
    print("Goupe N°:",groupe)
         #and we finally print our randomized list
    print(random_list)
    print("______________________________")
    groupe += 1
    # then we remove data already randomize in our list, but the complexity is high for this little program
    for element in random_list:
        ma_list.remove(element)
    if len(maListOc) <= 2:
        random_list.append("".join(maListOc))
    elif len(maListOc) > 2 and len(maListOc) < nombre:
        random_list = maListOc
print("Goupe N°:", groupe)
    # and we finally print our randomized list
print(maListOc)
print("______________________________")


