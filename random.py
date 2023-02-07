import random
ma_list =["anne","aline","gros","eve","armand","yves","elv","allo","sonia","luc","marc","jules","kevin"]
random_list = []
groupe = 1
for i in ma_list:
    if(len(ma_list)<=5):
        break
    random_list = random.sample(ma_list, 6)
    
    for element in random_list:
        ma_list.remove(element)
    print("Goupe N°:",groupe)
    print(random_list)
    print("-----------------------------------------------------")
    groupe += 1
