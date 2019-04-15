#This function looks at the first item in each players list to determine
#if they are BLEEDING OUT, PARALYZED, POISONED, INSANE, or DEAD

dicOfPlayers = {'Caleb':[['BLEEDING OUT', 'POISONED'], 100, 10, 5, 12], 'Josh':['DEAD', 100, 3, 14, 9], 'Charlie':['POISONED', 100, 3, 15, 10]}

def statEffects(dicOfPlayers):
    for player in dicOfPlayers:
        print(player)
        list1=dicOfPlayers[player]
        print(list1)
        if 'DEAD' in list1[0]:
            print(player, 'is dead')
        else:
            if 'BLEEDING OUT' in list1[0]:
                #remove 15 health points from player
                list1[1] = list1[1] - 15
                print(player,"is bleeding heavily")
                print(list1[1])
            if 'PARALYZED' in list1[0]:
                print(player, 'is paralyzed and cannot move.')
            if 'POISONED' in list1[0]:
                print(player, 'is poisoned.')
                list1[2] = list1[2] - 5
            if 'INSANE' in list1[0]:
                list1[3] = list1[3] - 3
        print(player + ' ' + str(list1))
        
statEffects(dicOfPlayers)
