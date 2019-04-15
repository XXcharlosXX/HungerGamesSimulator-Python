import random
import time

E_EVENTLIST = [['is attacked by ridiculously large tracker jackers.',[0,8,5,5],["swiftly escapes.","is stung to death..."]],
               ["spots a wild boar.",[0,8,3,1],["kills it and cooks it for a snack.","is pierced by a tusk and slowly dies."]],
               ['is caught in a lightning storm.',[0,0,0,5], ["luckily isn't struck.", 'is struck and instantaeously combusts.']],
               ["runs into a tiger.",[0,10,5,3],["safely escapes.","gets mauled and dies."]],
               ["runs through a posion ivy bush.",[0,2,2,3],["begins to feel very uncomfortable but moves on.","is weakend and slowly dies."]],
               ['does not see a pit hidden in his path.', [0,12,4,0], ['sees the pit in time and avoids it.', 'falls into the pit and dies.']],
               ['is swept away by a flash flood.', [0,10,0,14], ['clings to a sturdy rock and survives.', 'gets sucked underneath and drowns.']],
               ['begins to give in to the voices in their head.', [0,0,14,0], ['silences the voices for another day.', 'slips into insanity and mindlessly lets themselves die.']],
               ['gets caught in a wildfire.', [0,9,9,9], ['narrowly escapes a fiery death.', 'is burned alive.']],
               ['stumbles on a rock on the path.', [0,5,0,0], ['expertly performs a barrel roll', 'falls and breaks their neck...dummy.']],
               ['sees a duck lying in front of them.', [0,0,0,12], ['lets the duck do his thing, ever suspicious...', 'stupidly picks up the duck and explodes. He should have known better.']],
               ['sees a rockslide hurtling toward them.', [0,14,0,12], ['jumps out of danger just in time.', 'is crushed underneath the rubble.']],
               ['becomes engulfed in the unspeakably awful, soul-scaring phenomenon.', [0,0,0,18], ['escapes, forever changed...', 'succumbs to the effects of the event. It has claimed another victim...']],
               ['is surrounded by mockingjays speaking in the voices of dead loved ones.', [0,0,15,0],['is not effected by the voices.', 'is overcome by madness and dies.']],
               ['is surprised when a tree comes to life and attacks.', [0,11,0,11], ["escapes the tree's clutches.", 'is eaten alive by a tree.']],
               ['becomes surrouned by poisonous gas.', [0,8,0,8], ['holds their breath just long enough to live.', 'inhales too much gas and dies.']],
               ['sees some tasty looking berries.', [0,0,12,0], ['eats the berries and they are delicious!', 'eats the berries, vomits, and dies.']],
               ["finds a Cracker Barell Buttered Buiscuit.",[0,0,10,1],["leaves it alone becuase it might be a trap.","eats it and quickly dies from an unknown poison"]],
               ["gets caught in quicksand.",[0,7,9,9],["recieves a package with rope, attaches it to a tree and climbs out unharmed.","is sucked to the bottom and dies."]],
               ["tries to escape the arena.",[0,0,8,2],["figures that's a bad idea, and searches for opponents.","attempts to escape and is attacked my massive hell hounds."]],
               ["is walking between a crevace as it begins to close in.",[0,7,6,5],["finds a sturdy log to buy time and escapes certain death.","tries to run to the opening, but isn't quick enough and is squashed."]],
               ['finds themselves in absolute darkness.', [0,0,7,7], ['waits it out until the light returns.', 'disappears within the inky void.']]]

P_EVENTLIST = [['charge at each other', 1, ['tries to kill','kills']],
               ['spot each other', 2, ['tries to trap','traps and kills']],
               ['attack each other', 1, ['tries to kill', 'kills']],
               ['spot each other', 2, ['attempts to surprise','catches by surprise and kills']],
               ['attack each other', 1, ['gains the advantage over','overpowers and kills']],
               ['hear each other', 2, ['spots', 'backstabs']],
               ['lunge at each other', 1, ['gets several blows into', 'mauls and mutilates']],
               ['stand off against each other', 1, ['strikes first for', 'breaks the neck of']],
               ['wrestle each other', 1, ['pins', 'bashes']],
               ['are unaware of one another', 2, ['hears','accidently kills']],
               ['track each other down', 2, ['catches', 'captures and kills']],
               ['are enraged at each other', 1, ['breaks the ribs of', 'smashes the skull of']],
               ['are hopelessly in love with each other', 2, ['steals a kiss from', 'very lovingly kills']]]



def p_Event(cData1, cData2,char_data):
    eventSelect =random.randint(1,len(P_EVENTLIST))
    thevent = P_EVENTLIST[eventSelect-1]
    time.sleep(1)
    print (cData1,'and',cData2,thevent[0])
    #getting the stats for each player...
    stats1=char_data[cData1]#[P_EVENTLIST[1]]
    if cData2:
        stats2=char_data[cData2]#[P_EVENTLIST[1]]
        #comparing the players' stats to each other...
        if stats1[thevent[1]] == stats2[thevent[1]]:
            print('The two tributes are equally matched, and they retreat.')
        elif stats1[thevent[1]]<stats2[thevent[1]]:
            factor = random.randint(1,45)
            if stats1[3] >= factor:
                print (cData2,thevent[2][0],cData1,'but',cData1,'gets lucky and escapes.')
            else:
                print(cData2,thevent[2][1],cData1,'with',stats2[6])
                if stats2[6] == "Bare Hands" and stats1[6] != "Bare Hands":
                    print (cData2,' picks up ',cData1,"'s ",stats1[6],'.')
                    char_data[cData2][6] = stats1[6]
                    index = 0
                    for boost in char_data[cData2][4]:
                        char_data[cData2][index] = char_data[cData2][index] + boost
                        #increasing "index" by 1 to cycle through the character's stats
                        index += 1
                char_data[cData1][0] = 0
        else:
            factor = random.randint(1,45)
            if stats2[3] >= factor:
                print (cData1,thevent[2][0],cData2,'but',cData2,'gets lucky and escapes.')
            else:
                print(cData1,thevent[2][1],cData2,'with',stats1[6])
                if stats1[6] == "Bare Hands" and stats2[6] != "Bare Hands":
                    print (cData1,' picks up ',cData2,"'s ",stats2[6],'.')
                    char_data[cData1][6] = stats2[6]
                    index = 0
                    for boost in char_data[cData1][4]:
                        char_data[cData1][index] = char_data[cData1][index] + boost
                        #increasing "index" by 1 to cycle through the character's stats
                        index += 1
                char_data[cData2][0] = 0
    else:
        print("You shouldn't be reading this...\n")
    print('')
    #return newData1, newData2

#This event takes the data of two tributes given from main and gives them an event to complete
#If one of the players does not complete the event, they are either labeled as dead
def env_Event(cData1, cData2,char_data):
    time.sleep(1)
    eventSelect =random.randint(1,len(E_EVENTLIST))
    thevent=E_EVENTLIST[eventSelect-1]

    #getting the stats for the first player...
    stats1=char_data[cData1]

    #count = 0
    if stats1[1] >= thevent[1][1] and stats1[2] >= thevent[1][2] and stats1[3] >= thevent[1][3]:
        print(cData1,thevent[0],cData1,thevent[2][0])
    else:
        print(cData1,thevent[0],cData1,thevent[2][1])
        char_data[cData1][0] = 0
        
    eventSelect =random.randint(1,len(E_EVENTLIST))
    thevent=E_EVENTLIST[eventSelect-1]
    
    #Checking to see if there is a second player...
    if cData2:
        print('')
        #getting the stats for the second player...
        stats2=char_data[cData2]
        #count = 0
        if stats2[1] >= thevent[1][1] and stats2[2] >= thevent[1][2] and stats2[3] >= thevent[1][3]:
            print(cData2,thevent[0],cData2,thevent[2][0])
        else:
            print(cData2,thevent[0],cData2,thevent[2][1])
            char_data[cData2][0] = 0
    else:
        newData2 = False
    print('')


def Event(cData1, cData2,char_data):
    c = random.randint(0,1)
    if c == 0: #run enveventx2
         #result1, result2 =
         env_Event(cData1, cData2,char_data)
    else: #run player event
         #result1, result2 =
         p_Event(cData1, cData2,char_data)
    #print(result1, result2)
    return char_data
