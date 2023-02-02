import random
ma_list =["Asène","Bray","Elie","Ezechiel","Hamidé","Hassane","Hypolite","Issa","Innocent","Julie","Lagré","Mahamat","Narcisse","Nil","Payang","Seraphin","Severin","jules","kevin"]
#this will contain an occurence of our list
maListOc = ma_list
#this list will contain our random list
random_list = []
groupe = 1
#for each element in ma_list, we randome and put into our variable
for i in ma_list:
#This condition will avoid errors when n is greater than 4
    if len(ma_list)<= 5 :
        break
    random_list = random.sample(ma_list, 5)
    #then we remove data already randomize in our list, but the complexity is high for this little program
    for element in random_list:
            ma_list.remove(element)
    print("Goupe N°:",groupe)
#and we finally print our randomized list
    print(random_list)
    print("______________________________")
#if ma_list :
    groupe+=1
d=groupe
print("Goupe N°:",d)
print(maListOc)
