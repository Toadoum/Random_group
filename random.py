import random
ma_list =["lagré","julie","yacoub","hypolite","succes","yassine",
         "francis","Elie","seraphin","severin","issa","hamza",
         "bray","exaucé","yannick","innocent","arsène","payang",
         "hassane","Hamidé","Ezékiel","Nil","Narcisse"]
#this will contain an occurence of our list
maListOc = ma_list
#this list will contain our random list
random_list = None
groupe = 1
#for each element in ma_list, we randome and put into our variable
print("########################### Composition de groupe de travail #########################")
for i in ma_list:
#This condition will avoid errors when n is greater than 4
    if(len(ma_list)<=5):
        break
    random_list = random.sample(ma_list, 5)
    #then we remove data already randomize in our list, but the complexity is high for this little program
    for element in random_list:
        ma_list.remove(element)
    
    print("Goupe N°:",groupe)
    #and we finally print our randomized list
    print(random_list)
    print("______________________________")
    groupe += 1
x=groupe
print("Goupe N°:",x)
print(maListOc)


