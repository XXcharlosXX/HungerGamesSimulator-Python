import random
import time
#import event_List

E_EVENTLIST= ['is caught in a lightning storm.',[0,0,0,5], ['you win', 'lose'],["runs into a tiger.",[0,2,4,1],["safely escapes.","gets mauled and dies."],["runs through a posion ivy bush",[0,2,2,3],["",""]]
P_EVENTLIST = ['this is a mental event', 2, ['player1 stabs player 2', 'player 2 stabs player 1']]
dic1 = {'Caleb':[100,7,3,5,'','North']}
dic2 = {'Charlie':[100,5,5,12,'','North']}


def p_Event(cData1, cData2):
    eventSelect =random.randint(1,len(P_EVENTLIST))
    #getting the stats for each player...
    for key in cData1.keys():
        x1=key
    stats1=cData1[x1][P_EVENTLIST[1]]
    if cData2:
        for key in cData2.keys():
            x2=key
        stats2=cData2[x2][P_EVENTLIST[1]]

        #comparing the players' stats to each other...
        if stats1 == stats2:
            print('The two tributes are equal, and they retreat.')
        elif stats1<stats2:
            print(P_EVENTLIST[2][1])
            newData2 = cData2
            newData1 = cData1[x1][0]=0
        else:
            print(P_EVENTLIST[2][0])
            newData1 = cData1
            newData2 = cData2[x2][0]=0
    else:
        print(x, 'moves to a new region.')
        cData1[x][-1] = 'random'
        newData1 = cData1
        newData2 = False
    return newData1, newData2

#This event takes the data of two tributes given from main and gives them an event to complete
#If one of the players does not complete the event, they are either labeled as dead
def env_Event(cData1, cData2):
    eventSelect =random.randint(1,len(E_EVENTLIST))
    thevent=E EVENTLIST[eventSelect-1]

    #getting the stats for the first player...
    for key in cData1.keys():
        x=key
    stats1=cData1[x]

    count = 0
    for stat in stats1[1:4]:
        if stat >= thevent[1][count]: #CHANGE THIS WHEN EVENTSELECT GETS CHANGED
            print(x,thevent[0],thevent[2][0])
            newData1=cData1
        else:
            print(x,thevent[0],thevent[2][1])
            stats1[0] = 0
            print(stats1)
        count+=1
    newData1 = {x:stats1}

    #Checking to see if there is a second player...
    if cData2:
        #getting the stats for the second player...
        for key in cData2.keys():
            x=key
        stats2=cData2[x]

        count = 0
        for stat in stats2[1:4]:
            if stat >= E_EVENTLIST[1][count]: #CHANGE THIS WHEN EVENTSELECT GETS CHANGED
                print(E_EVENTLIST[2][0])
            else:
                print(E_EVENTLIST[2][1])
                stats2[0] = 0
                print(stats2)
            count+=1
        newData2 = {x:stats2}
        
    else:
        newData2 = False
        
    return newData1, newData2


def Event(cData1, cData2):
    c = random.randint(0,1)
    if c == 0: #run enveventx2
         result1, result2 = env_Event(cData1, cData2)
    else: #run player event
         result1, result2 = p_Event(cData1, cData2)
    print(result1, result2)
    return result1, result2

Event(dic1, dic2)
