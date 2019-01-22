#YUHAN ZHANG(29400988) 14/08/2018 - 24/08/2018

#Uising time function to control the view of result output
import time

#create a user and join the game and decide how much coin that want to cost
#using while function to control the input number between 0 and 10, any others input are invalid
#leftCoinA: the coin that user buy the medics

userA = str(input('plz input your name\n'))
coinA = input('\n'+ userA + ' plz enter your coin,(0-10)\n')
while not (coinA.isdigit() and 0 <= int(coinA) <= 10):
    print('wrong input')
    coinA = input('plz insert coin,(0-10)\n')
else:
    print(userA + ' you have $', coinA)

leftCoinA = 10 - int(coinA)

#create a list for first user for store army
#determine what is the user input then add unit to list, valid input only 1,2,3,4,5
#user can purchase units only when have coin and cannot buy unit over the price
#every time add a unit, the coinA will -1
#playerAlist: userA's list that store the army

coinA = int(coinA)
playerAlist = []
while coinA > 0:
    x = input('select your unit 1 = Archer|$1, 2 = Soldier|$1, 3 = Knight|$2, 4 = Siege Equipment|$3, 5 = Wizard|$4\n')
    if x.isdigit() and int(x) == 1:
        playerAlist.append('Archer')
        coinA = int(coinA - 1)
        print(userA+' This is your army', playerAlist,'\nyou have $'+str(coinA)+' now')
    elif x.isdigit() and int(x) == 2:
        playerAlist.append('Soldier')
        coinA = int(coinA - 1)
        print(userA+' This is your army', playerAlist,'\nyou have $'+str(coinA)+' now')
    elif x.isdigit() and int(x) == 3 and coinA >=2:
        playerAlist.append('Knight')
        coinA = int(coinA - 2)
        print(userA+' This is your army', playerAlist,'\nyou have $'+str(coinA)+' now')
    elif x.isdigit() and int(x) == 4 and coinA >=3:
        playerAlist.append('Siege Equipment')
        coinA = int(coinA - 3)
        print(userA+' This is your army', playerAlist,'\nyou have $'+str(coinA)+' now')
    elif x.isdigit() and int(x) == 5 and coinA >=4:
        playerAlist.append('Wizard')
        coinA = int(coinA - 4)
        print(userA+' This is your army', playerAlist,'\nyou have $'+str(coinA)+' now')
    else:
        print('wrong,input again')

#create a user and join the game and decide how much coin that want to cost
#using while function to control the input number between 0 and 10, any others input are invalid
#leftCoinB: the coin that user buy the medics

userB = str(input('plz input your name\n'))
coinB = input('\n'+userB+' plz enter your coin,(0-10)\n')
while not (coinB.isdigit() and 0 <= int(coinB) <= 10):
    print('wrong input')
    coinB = input('plz insert coin,(0-10)\n')
else:
    print('you have $', coinB)

leftCoinB = 10 - int(coinB)

#create a list for first user for store army
#determine what is the user input then add unit to list, valid input only 1,2,3,4,5
#user can purchase units only when have coin and cannot buy unit over the price
#every time add a unit, the coinA will -1
#playerBlist: userB's list that store the army

coinB = int(coinB)
playerBlist = []
while coinB > 0:
    x = input('select your unit 1 = Archer|$1, 2 = Soldier|$1, 3 = Knight|$2, 4 = Siege Equipment|$3, 5 = Wizard|$4\n')
    if x.isdigit() and int(x) == 1:
        playerBlist.append('Archer')
        coinB = int(coinB - 1)
        print(userB+' ,This is your army', playerBlist,'\nyou have $'+str(coinB)+' now')
    elif x.isdigit() and int(x) == 2:
        playerBlist.append('Soldier')
        coinB = int(coinB - 1)
        print(userB+' ,This is your army', playerBlist,'\nyou have $'+str(coinB)+' now')
    elif x.isdigit() and int(x) == 3 and coinB >=2:
        playerBlist.append('Knight')
        coinB = int(coinB - 2)
        print(userB+' ,This is your army', playerBlist,'\nyou have $'+str(coinB)+' now')
    elif x.isdigit() and int(x) == 4 and coinB >=3:
        playerBlist.append('Siege Equipment')
        coinB = int(coinB - 3)
        print(userB+' ,This is your army', playerBlist,'\nyou have $'+str(coinB)+' now')
    elif x.isdigit() and int(x) == 5 and coinB >=4:
        playerBlist.append('Wizard')
        coinB = int(coinB - 4)
        print(userB+ ' ,This is your army', playerBlist,'\nyou have $'+str(coinB)+' now')
    else:
        print('wrong,input again')

#show the playerAlist and playerBlist after two user finish the unit purchased
print("\n"+userA+"'s army", playerAlist,'Medics =', leftCoinA, "\n"+ userB + "'s army", playerBlist,'Medics =', leftCoinB, "\n")

#using while function to run battle part
#if userA have units and userB have units, the while() keep going
#compare the first unit of two list, then decide which one could win
#i:using to show the round number
#before every time battle, i +1 and print i as the current round number
#every battle result will show to player
#tempA: store the first unit of playerAlist before battle
#tempB: store the first unit of playerBlist before battle
#lenAlist: the length of playerAlist
#lenBlist: the length of playerBlist

i = 0
while len(playerAlist) != 0 and len(playerBlist) != 0:
    tempA = playerAlist[0]
    tempB = playerBlist[0]
    lenAlist = len(playerAlist)
    lenBlist = len(playerBlist)
    i += 1

    if (playerAlist[0] == 'Archer' and playerBlist[0] == 'Archer') or (playerAlist[0] == 'Soldier' and playerBlist[0] == 'Soldier') or (playerAlist[0] == 'Knight' and playerBlist[0] == 'Knight') or (playerAlist[0] == 'Wizard' and playerBlist[0] == 'Wizard') or (playerAlist[0] == 'Siege Equipment' and playerBlist[0] == 'Siege Equipment'):
        playerAlist.pop(0)
        playerBlist.pop(0)
        print("Round",i,"This round is Tie\n","\n"+userA+"'s army", playerAlist, "\n"+ userB +"'s army", playerBlist)
    elif (playerAlist[0] == 'Archer' and playerBlist[0] == 'Soldier') or (playerAlist[0] == 'Archer' and playerBlist[0] == 'Wizard'):
        playerBlist.pop(0)
        print("Round",i,"This round " + userA + " win\n","\n"+userA+"'s army", playerAlist, "\n"+ userB +"'s army", playerBlist)
    elif (playerAlist[0] == 'Archer' and playerBlist[0] == 'Knight') or (playerAlist[0] == 'Siege Equipment' and playerBlist[0] == 'Knight'):
        playerAlist.pop(0)
        print("Round",i,"This round " + userB + " win\n","\n"+userA+"'s army", playerAlist, "\n"+ userB +"'s army", playerBlist)
    elif (playerAlist[0] == 'Soldier' and playerBlist[0] == 'Archer') or (playerAlist[0] == 'Wizard' and playerBlist[0] == 'Archer'):
        playerAlist.pop(0)
        print("Round",i,"This round " + userB + " win\n","\n"+userA+"'s army", playerAlist, "\n"+ userB +"'s army", playerBlist)
    elif playerAlist[0] == 'Soldier' and playerBlist[0] == 'Knight':
        playerBlist.pop(0)
        print("Round",i,"This round " + userA + " win\n","\n"+userA+"'s army", playerAlist, "\n"+ userB +"'s army", playerBlist)
    elif (playerAlist[0] == 'Soldier' and playerBlist[0] == 'Wizard') or (playerAlist[0] == 'Knight' and playerBlist[0] == 'Wizard') or (playerAlist[0] == 'Siege Equipment' and playerBlist[0] == 'Wizard'):
        playerAlist.pop(0)
        print("Round",i,"This round " + userA + " win\n","\n"+userA+"'s army", playerAlist, "\n"+ userB +"'s army", playerBlist)
    elif (playerAlist[0] == 'Knight' and playerBlist[0] == 'Archer') or (playerAlist[0] == 'Knight' and playerBlist[0] == 'Siege Equipment'):
        playerBlist.pop(0)
        print("Round",i,"This round " + userA + " win\n","\n"+userA+"'s army", playerAlist, "\n"+ userB +"'s army", playerBlist)
    elif playerAlist[0] == 'Archer' and playerBlist[0] == 'Soldier':
        playerAlist.pop(0)
        print("Round",i,"This round " + userB + " win\n","\n"+ userA +"'s army", playerAlist, "\n"+ userB +"'s army", playerBlist)
    elif (playerAlist[0] == 'Archer' and playerBlist[0] == 'Siege Equipment') or (playerAlist[0] == 'Soldier' and playerBlist[0] == 'Siege Equipment'):
        playerAlist.pop(0)
        print("Round",i,"This round " + userB + " win\n","\n"+userA+"'s army", playerAlist, "\n"+ userB +"'s army", playerBlist)
    elif (playerAlist[0] == 'Siege Equipment' and playerBlist[0] == 'Archer') or (playerAlist[0] == 'Siege Equipment' and playerBlist[0] == 'Soldier'):
        playerBlist.pop(0)
        print("Round",i,"This round " + userB + " win\n","\n"+userA+"'s army", playerAlist, "\n"+ userB +"'s army", playerBlist)
    elif (playerAlist[0] == 'Wizard' and playerBlist[0] == 'Soldier') or (playerAlist[0] == 'Wizard' and playerBlist[0] == 'Siege Equipment') or (playerAlist[0] == 'Wizard' and playerBlist[0] == 'Knight'):
        playerBlist.pop(0)
        print("Round",i,"This round " + userB + " win\n","\n"+userA+"'s army", playerAlist, "\n"+ userB +"'s army", playerBlist)
    else:
        pass

# the medics situation shows at every battle
#if any list lose unit the length will -1, so len(playerAlist) == lenAlist - 1 means playerAlist lose a unit
#The leftcoinA > 0 means userA still have medics.
#only list lose unit and user have medics, unit store in tempA could add to tail of list
#if add a unit the leftCoinA -1

    print(userA + ' have', leftCoinA, 'Medics now')
    if len(playerAlist) == lenAlist - 1 and leftCoinA > 0:
        playerAlist.append(tempA)
        leftCoinA -= 1
    else:
        pass

# the medics situation shows at every battle
# if any list lose unit the length will -1, so len(playerBlist) == lenBlist - 1 means playerBlist lose a unit
# The leftcoinB > 0 means userB still have medics.
# only list lose unit and user have medics, unit store in tempB could add to tail of list
# if add a unit the leftCoinB -1

    print(userB + ' have', leftCoinB, 'Medics now\n')
    if len(playerBlist) == lenBlist - 1 and leftCoinB > 0:
        playerBlist.append(tempB)
        leftCoinB -= 1
    else:
        pass

#time.sleep(1): every one second output one of battle result

    time.sleep(1)

#any list is null means battle finished
#the situation of both lists are null must be the top of jujument if not, the result can not output correct
#only 3 result will be released


if len(playerAlist) == 0 and len(playerBlist) == 0:
    print('Tie!')
elif len(playerBlist) == 0:
    print('winner is ' + userA + '\n',playerAlist)
elif len(playerAlist) == 0:
    print('winner is ' + userB + '\n', playerBlist)
else:
    pass
