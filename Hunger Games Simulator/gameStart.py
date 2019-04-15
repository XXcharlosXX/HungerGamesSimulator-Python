
import charInfo
import eventInfo
import random

#This program takes in the names of participants and randomly generates events
#in a Hunger-Games style deathmatch.

#Declaring dictionary to hold player names, stats, and equipment
corn_stash = [['Dagger',1,0,0], ['Short Sword',2,0,0], ['War Axe',3,0,0],
              ['Mace',4,0,0], ['Claymore',5,0,0], ['Battle Axe',6,0,0],
              ['War Hammer',7,0,0], ['Sling Shot',0,1,0], ['Long Bow',0,2,0],
              ['Traps',0,3,0], ['Whip',0,4,0], ['Throwing Knives',0,5,0],
              ['Nunchucks',0,6,0], ['Chakrams',0,7,0], ['Pot of Gold',0,0,1],
              ['First Aid Kit',0,0,2], ['Magic Konch',0,0,3],
              ['Horseshoe',0,0,4], ['8 Ball',0,0,5],
              ['Cracker Barrel Buttered Biscuit',0,0,6], ['Time Bomb',0,0,7]]
#Declaring dictionary to hold possible settings
setting = {}

#Declaring main function
def main ():

    #Introducing Simulator
    print ('Welcome to the Arena!\nYou are the lucky winners of our',
           '"Opportunity of a Lifetime" contest!\nTo begin your participation',
           'in this greatest of opportunities, please take turns entering your',
           'names and receiving your personalized care package!\nThank you and',
           'enjoy your time at the Arena!\n')

    #Function that will take in player names, use a personality quiz to
    #allocate stats,select and randomly determine stats for NPCs, and then
    #assigning that information to the "char_data" dictionary
    char_data = charInfo.getStats()
    
    #Pausing the program til the user wishes to continue
    input ('\nPress enter when you would like to continue.') 

    #Prepping dictionaries for simulator by importing contents from other files
    files('scenery.txt',setting)

    #Introducing the names of all contestants and their districts of origin and
    #declaring the list of keys for the "char_data" dictionary
    print ("\nLet's welcome this year's contestants!")
    char_keys = char_announce(char_data.keys())

    #Pausing the program til the user wishes to continue
    input ('\nPress enter when you would like to return to the Arena.')
    
    #Setting the scenery for the Arena
    print ('\nWelcome back, dear contestants!\nNow that you are prepared to take',
           'part in this "Opportunity of a Lifetime," we will introduce you to',
           "this year's Arena!\n")

    #Calling the "scene()" function and assigning the chosen setting to "arena"
    arena = scene()

    #Pausing the program til the user wishes to continue
    input ('Press enter when you are ready to begin the Games.\n')

    #Calling the "bloodbath()" function and assigning the dead characters to
    #"char_dead"
    char_dead = bloodbath(char_data,char_keys)

    #Calling the "cornucopia()" function and assigning the living characters to
    #"char_keys"
    char_keys = cornucopia(char_data,char_keys,arena)

    #"day" keeps track of the current day inside the Arena
    day = 1
    #Declaring that the day's events have ended with multiple casualties
    print ('Day',day,'has ended.\nThe cannons fire',len (char_dead),
           'times, announcing those who have died today.')
    #Calling the "char_announce()" function to announce the dead characters
    char_announce(char_dead)
    #Clearing the "char_dead" list of the previous day's casualties
    char_dead = list ()
    #Giving the player time to review the day's events and continue when ready
    input ('\nPress enter when you would like to progress to the next day.\n')
    #Moving to the next day in the Arena
    day += 1

    #Running the event generator until there is only one character left alive
    while len (char_keys) > 1:
        #Establishing how many events will happen in a day
        for count in range (len (char_keys)//2):
            #Calling the char_select function and assigning the first character
            #participating in a random event in "char1", the second character
            #participating in a random event in "char2", and the characters that
            #are still alive in "char_keys"
            char1,char2,char_keys = char_select(char_data,char_keys,arena)
            #Function that will randomly generate the environmental and PVP
            #events that happen to the players as they participate in the Arena
            char_data = eventInfo.Event(char1,char2,char_data)
            print('')
            #Determining whether "char1" has died by analyzing the HP stat
            if char_data[char1][0] == 0:
                #Appending the dead character to the "char_dead" list
                char_dead.append(char1)
                #Removing the dead character from the "char_keys" list
                char_keys.remove(char1)
            #Determining whether "char2" has died by analyzing the HP stat
            if char_data[char2][0] == 0:
                #Appending the dead character to the "char_dead" list
                char_dead.append(char2)
                #Removing the dead character from the "char_keys" list
                char_keys.remove(char2)
        #Determining whether the number of tributes that died this day is equal
        #to 1 or greater than 1.
        if len (char_dead) == 1:
            #Declaring that the day's events have ended with 1 casualty
            print ('Day',day,'has ended.\nThe cannons fire a single time,',
                   'announcing those who have died today.')
        else:
            #Declaring that the day's events have ended with multiple casualties
            print ('Day',day,'has ended.\nThe cannons fire',len (char_dead),
                   'times, announcing those who have died today.')
        #Calling the "char_announce()" function to announce the dead characters
        char_announce(char_dead)
        #Clearing the "char_dead" list of the previous day's casualties
        char_dead = list ()
        #Giving the player time to review the day's events and continue when
        #ready
        input ('\nPress enter when you would like to progress to the next day.\n')
        #Moving to the next day in the Arena
        day += 1
    #Determining whether there is a winner of the Hunger Games
    if len (char_keys) == 0:
        #Declaring that there are no survivors
        print ('We regret to inform our viewers that there are no winners in',
               "this year's Hunger Games.")
    else:
        #Declaring the winner of the Hunger Games
        print (char_keys[0],'has won the Hunger Games!')

#Function that prints out contestant names from a list
#"group" is the parameter for the keys of "char_data"
def char_announce(group):
    #"char_name" holds the keys from the "char_data" dictionary
    char_name = list()
    #Announcing name of each character and their home district and appending the
    #keys to the "char_keys" list
    for item in group:
        print (item)
        #Appending the key to "char_name"
        char_name.append(item)
    #Returning contents of "char_name" to the "char_keys" list
    return (char_name)

#Function that reads in files and puts their contents in dictionaries
#"file_x" is the parameter for the name of the file being used
#"dic1" is the parameter for the dictionary for storing the contents of "file_x" 
def files(file_x,dic1):
    #Testing whether "file_x" is able to be opened
    try:
        #Opening file_x for reading and assigning to "f"
        f = open (file_x, 'r')
        #Putting contents of file_x into the corresponding dictionary
        for line in f:
            #Putting values in the "temp" list
            temp = f.readline().rstrip().split(',')
            #Establishing the key associated with the list of values
            dic1[line.rstrip()] = temp
        #Closing "file_x"
        f.close()
    except:
        #Stating that "file_x" is not available
        print ('No file, "',file_x,'", exists in this location.')

#Function that establishes the scenery of the Arena
def scene():
    #"arena" receives a tuple of the selected setting for the Arena from the
    #"setting" dictionary
    arena = setting.popitem()
    print ("This year's Arena features a(n)",arena[0],'with a(n)',arena[1][0],'in',
           'the North, a(n)',arena[1][1],'in the East, a(n)',arena[1][2],'in the',
           'South, and a(n)',arena[1][3],'in the West!\n\nPlease proceed to your',
           'prep rooms!\nThere an associate will prepare you to enter the',
           'Arena.\nThank you and may the odds be ever in your favor!\n')
    #Returning the contents of "arena" (local to "scene()") to "arena" (local to
    #"main()")
    return (arena)

#Function that sets up the Cornucopia and counts down to the start of the games
#"dic1" is the paramater for the "char_data" dictionary
#"list1" is the parameter for the "char_keys" list
#"tuple1" is the parameter for the "arena" tuple
def cornucopia(dic1,list1,tuple1):
    #"list2" catches the character names removed from "list1"
    list2 = list ()
    #Establishing which players receive weapons and which don't and establishes
    #starting location for players
    for x in range (len(dic1)):
        #"index1" is the randomly selected index for "list1"
        index1 = random.randint(0, (len(list1)- 1))
        #"index2" is the randomly selected index for "corn_stash"
        index2 = random.randint(0, (len(corn_stash) - 1))
        #"index3" is the index for each stat position for the selected character
        index3 = 1
        #"loc" holds the selected location that the player runs towards
        loc = tuple1[1][random.randint(0,3)]
        #"factor" acts as an I/O switch to randomly determine whether players
        #run away or take a weapon from the Cornucopia
        factor = random.randint(0, 1)
        #Making player run from the Cornucopia with no weapon and run towards a
        #landmark
        if factor == 0:
            print (list1[index1],' runs away from the Cornucopia towards the ',
                   loc,'.\n')
            #Establishing the player's designated weapon as "Bare Hands"
            dic1[list1[index1]].append('Bare Hands')
        #Making player take a weapon from the Cornucopia and run towards a
        #landmark
        else:
            print (list1[index1],' reaches the Cornucopia and grabs ',
                   corn_stash[index2][0],' before leaving in the direction of ',
                   'the ',loc,'.\n')
            #Establishing the player's designated weapon as the randomly
            #selected weapon from "corn_stash"
            dic1[list1[index1]].append(corn_stash[index2][0])
            #Establishing the values for the stat boost slot
            dic1[list1[index1]][4] = corn_stash[index2][1:]
            #Adding the stat boosts from the weapon onto the player's stats
            for boost in corn_stash[index2][1:]:
                dic1[list1[index1]][index3] = dic1[list1[index1]][index3] + boost
                #increasing "index3" by 1 to cycle through the character's stats
                index3 += 1
            #Removing used weapon from "corn_stash"
            corn_stash.remove(corn_stash[index2])
        #Establishing the player's new location
        dic1[list1[index1]][5] = loc
        #Appending character from "list1" that is about to be removed
        list2.append(list1[index1])
        #Removing used character from "list1"
        list1.remove(list1[index1])
    #Returning "list2" contents to the "char_keys" list
    return (list2)

#Function that determines who dies in the initial bloodbath
#"dic1" is the paramater for the "char_data" dictionary
#"list1" is the parameter for the "char_keys" list
def bloodbath(dic1,list1):
    #"list2" catches the character names removed from "list1"
    list2 = list ()
    #"casualties" holds the random number of casualties in the bloodbath
    casualties = random.randint(4, 12)
    #Determining who and how many players die in the bloodbath using random
    #number generation
    for x in range (casualties):
        #"index" is the randomly selected index for "dic1"
        index = random.randint(0, (len(dic1)- 1))
        #Removing the dead character from "dic1"
        dic1.pop(list1[index])
        #Appending character from "list1" that is about to be removed
        list2.append(list1[index])
        #Removing dead character from "list1"
        list1.remove(list1[index])
    #Stating the number of casualties in the initial bloodbath
    print ('There are',casualties,'casualties in the bloodbath.\n')
    #Returning contents of "list2" to the "char_dead" list
    return (list2)

#Function that selects characters to participate in a randomly generated event
#"dic1" is the paramater for the "char_data" dictionary
#"list1" is the parameter for the "char_keys" list
#"tuple1" is the parameter for the "arena" tuple
def char_select(dic1,list1,tuple1):
    #"vicinity" holds whether there is a character in the player's vicinity
    vicinity = ''
    #"list2" catches the character names removed from "list1"
    list2 = list ()
    #"index1" is the first randomly selected index for "list1"
    index1 = random.randint(0, (len(list1)- 1))
    #"base" holds the first character selected for location comparison
    base = list1[index1]
    #Appending character from "list1" that is about to be removed
    list2.append(base)
    #Removing first character from "list1"
    list1.remove(base)
    #Comparing location of characters with "base" while "vicinity" is unknown
    while vicinity == '':
        #Looking for a character in the same location as "base" until the list
        #runs out of characters
        try:
            #"index2" is the second randomly selected index for "list1"
            index2 = random.randint(0, (len(list1)- 1))
            #Testing if the selected character is in the same location as the
            #first character
            if dic1[base][5] == dic1[list1[index2]][5]:
                #"char1" holds the first character in the location
                char1 = base
                #"char2" holds the second character in the location
                char2 = list1[index2]
                #Setting "vicinity" to true because there is a character nearby
                vicinity = True
            #Removing tested character from "list1" if not in the same location
            else:
                #Appending character from "list1" that is about to be removed
                list2.append(list1[index2])
                #Removing tested character from "list1"
                list1.remove(list1[index2])
        #Moving the first character to a new location
        except:
            #Selecting a random location 
            loc = tuple1[1][random.randint(0,3)]
            #Ensuring the first character moves to a new location
            while loc == dic1[base][5]:
                loc = tuple1[1][random.randint(0,3)]
            #Stating the first character's new location
            print (base,'moves to the',loc)
            #Changing the character's location to the new location
            dic1[base][5] = loc
            #Restoring tested characters to "list1" for location comparison
            for item in list2:
                list1.append(item)
            #Clearing the contents of "list2" to prevent character duplication
            list2 = list ()
            #Appending character from "list1" that is about to be removed
            list2.append(base)
            #Removing first character from "list1"
            list1.remove(base)
    #Restoring tested characters to "list1"
    for item in list2:
        list1.append(item)
    #Returning contents of "char1", "char2", and "list1" to "char1", "char2",
    #and "char_keys"
    return (char1,char2,list1)

#Calling the main function
main()
