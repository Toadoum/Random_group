import random

def team_generator (my_list) :
    teams = []
    teams_number = 0
    if (len (my_list) / 5) % 5 == 0 :
        teams_number = int (len (my_list) / 5)
    else :
        teams_number = int (len (my_list) / 5) + 1
    for i in range (teams_number) :
        if len (my_list) < 5 :
            teams.append (my_list)
            break
        team = random.sample(my_list, 5)
        teams.append (team)
        for elem in team :
            my_list.remove (elem)
    for j in range (len (teams)) :
        print (f"Groupe N°: {j + 1} \n{teams [j]}\n")
        print ("_____________________________________________")

ma_list =["anne","aline","gros","eve","armand","yves","elv","allo","sonia","luc","marc","jules","kevin"]

team_generator (ma_list)