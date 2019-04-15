import random
import time
import p_Questions

#Ask the player how many are playing and returns that number.
def howMany():
    a = False
    while not a:
        try:
            number = int(input("How many players are playing? (1-24) Please enter an integer: "))
            if 0<number<=24:
                a = True
                return number
            else:
                if number == 0:
                    time.sleep(1)
                    print('\nThen why are you playing this game, dummy!?\n')
                a = False
                time.sleep(1)
                print('Enter a number between 1 and 24')
                time.sleep(1)
        except ValueError:
            time.sleep(1)
            print("Please enter a number.")


#grabs 3 random {questions:[[answers, score values]]} and sends in to questions()
def getQuestions():
    questList = p_Questions.q()
    listList = []
    
    for x in range(3):
        selectDic = random.randint(0, len(questList))
        listList.append(questList[selectDic-1])
        questList.remove(questList[selectDic-1])
    return(listList)


#Ask the player the 3 questions from getQuestions() and returns a dictionary of attributes
def questions(getQuestions):
    print("During Training Days...")
    print("")
    time.sleep(.5)
    count=0
    result = [100,5,5,5]
    for x in getQuestions:
        time.sleep(1)
        print(getQuestions[count][0])
        otherCount = 0
        for a in getQuestions[count][1]:
            time.sleep(.1)
            print(a[0])
            otherCount+=1
        q = input('')
        print("")
        #Also make sure the number they type isn't too large or too small
        while q == str(q):
            try:
                if int(q) in range(otherCount+1):
                    q = int(q)
                else:
                    time.sleep(.2)
                    print("Enter one of the numbers above.\n")
                    q = input('')
            except:
                time.sleep(.2)
                print('Enter a number\n')
                q = input('')
                
        result[1] = result[1] + getQuestions[count][1][q-1][1]
        result[2] = result[2] + getQuestions[count][1][q-1][2]
        result[3] = result[3] + getQuestions[count][1][q-1][3]
        count+=1
    result.append('')
    result.append('location')
        #print(result)
    return(result)


#Ask each player their name and sends them to take a 3 question personality test.
#Returns a dictionary with the name as a key and dictionary of stats as a value.
def getStats():
    dic ={}
    times = howMany()
    try:
        f=open('NPCs.txt', 'r')
        for NPC in range(24-times):
            name = f.readline().rstrip()
            stats = f.readline().rstrip().split(',')
            for num in range(4):
                stats[num] = int(stats[num])
            time.sleep(.1)
            print(name,'has been reaped.')
            dic[name.rstrip()] = stats
    except Exception as err:
        print(err)
    
    for player in range(times):
        print('')
        name=input('Player '+ str(player+1) + ", What is your name? ")
        stats = questions(getQuestions())
        time.sleep(.5)
        print(name, 'is ready for battle!')
        dic[name.rstrip()] = stats
    return dic

        

#getStats()
