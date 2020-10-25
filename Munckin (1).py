""" munchkin.py
    basic card game framework
    keeps track of card locations for as many hands as needed
"""
import random
import time

DNUMCARDS = 10
TNUMCARDS = 10
DECK = 0
PLAYER = 1
COMPone = 2
end = 5
playerlevel = componelevel = 1
playerS = componeS = 0
changed1 = 0
changed2 = 0
hold = 0
hold2 = 0
stri = ""
valP = ""
valC1 = ""
val1 = ""
val2 = ""
chance = 0

pickList = [0] * 7
TcardLoc = [0] * TNUMCARDS
DcardLoc = [0] * DNUMCARDS
TDeckVal = (1, 1, 1, 2, 1, 2, 2, 1, 1, 3)
TDeck = ("Sword", "Mace", "Potion", "helmet", "rock", "shield", "armor", "kneepads", "lamp", "Guided missile")
DDeck = ("Nose", "Goblin", "Slime", "Leperchaun", "chicken", "harpies", "frogs", "gazebo", "rat", "Dragon")
DDeckVal = (2, 3, 5, 5, 3, 5, 2, 2, 4, 5)
playerName = ("player", "computerone")

def main():
    global valP
    global valC1
    global playerlevel
    global componelevel
    global componeS
    global playerS
    track = 0
    for i in range(2):
        assignCard(PLAYER)
        assignCard(COMPone)
    print(TcardLoc)
    print(DcardLoc)
    print("Your strength is {}".format(playerS + playerlevel))
    print("Computerone strength is {}".format(componeS + componelevel))
    while playerlevel < end and componelevel < end:
        valP = "false"
        while valP == "false": ##while not killed
            playeroneDcard = random.randint(0, 9)
            if DcardLoc[playeroneDcard] == 0: ##if the value hasnt been changed
                DcardLoc[changed1] = 69 ##assigning input value to location
                valP = "kill" ##kill
        time.sleep(2)
        print("You drew a {}".format(DDeck[playeroneDcard]))
        time.sleep(2)
        print("This monster has a power level of {}".format(DDeckVal[playeroneDcard]))
        time.sleep(2)
        userInput = input("Do you choose to (f)ight or (r)un or (b)ribe the computer to help you fight: ")
        if userInput == 'f':
            if playerlevel + playerS > DDeckVal[playeroneDcard]:
                time.sleep(2)
                print("You have won the fight and will move one level closer to victory")
                playerlevel += 1
                assignCard(PLAYER)
                print("Your strength is {}".format(playerS + playerlevel))
            else:
                time.sleep(2)
                print("WhY dId YoU tRy To Fight a monster you cant beat you headass your level has been moved back to one")
                playerlevel = 1
            time.sleep(2)
            print("Thank you for fighting the monster")
        if userInput == 'r':
            time.sleep(2)
            print("You have a 1 in 3 chance of escaping the monster")
            chance  = random.randint(0,2)
            if chance == 0:
                time.sleep(2)
                print("Congradulations you have escaped")
            else:
                time.sleep(2)
                print("I am sorry but your ass got snatched my guy your level was moved back to level 1")
                playerlevel = 1
        if userInput == 'b':
            time.sleep(2)
            print("Please pick a card from your deck to offer to the computer")
            x = 0
            while x < 9:
                if(TcardLoc[x] == PLAYER):
                    pickList[track] = x
                    track += 1
                    time.sleep(2)
                    print("You have a {}".format(TDeck[x]))
                    time.sleep(2)
                    print("This has a power level of {}".format(TDeckVal[x]))
                x += 1
            time.sleep(2)
            print("You have a choice of the numbers: ")
            y = 0
            while y < track:
                print(pickList[y])
                y += 1
            time.sleep(2)
            cardInput = input("Please pick one of those card numbers please: ")
            chance = random.randint(0,1)
            if chance == 0:
                if playerlevel + playerS + componeS> DDeckVal[playeroneDcard]:
                    time.sleep(2)
                    print("You have won the fight and will move one level closer to victory")
                    playerlevel += 1
                    assignCard(PLAYER)
                    time.sleep(2)
                    print("Your strength is {}".format(playerS + playerlevel))
                    time.sleep(2)
                    print("Your card will now be switched over to the computer")
                z = 0
                while z < track:
                    if cardInput == pickList[i]:
                        TcardLoc[pickList[i]] = COMPone
                        playerS = playerS - TDeckVal[pickList[i]]
                        componeS = componeS + TDeckVal[pickList[i]]
                    z += 1
            if chance == 1:
                time.sleep(2)
                print("Im sorry computer has denied your bribe and while you were begging him to help you have been eating rest in pieces")
                playerlevel = 1
        valC1 = "false"
        while valC1 == "false": ##while not killed
            componeDcard = random.randint(0, 9)
            if DcardLoc[componeDcard] == 0: ##if the value hasnt been changed
                DcardLoc[changed1] = 69 ##assigning input value to location
                valC1 = "kill" ##kill
        chance = random.randint(0,1)
        if playerlevel != end:
            time.sleep(2)
            print("Computer drew a {}".format(DDeck[componeDcard]))
            time.sleep(2)
            print("This monster has a power level of {}".format(DDeckVal[componeDcard]))
            if componelevel + componeS > DDeckVal[componeDcard]:
                if componelevel + componeS > DDeckVal[componeDcard]:
                    time.sleep(2)
                    print("The computer won the fight and will continue to move up another level")
                    componelevel += 1
                    time.sleep(2)
                    print("Computerone strength is {}".format(componeS + componelevel))
                    assignCard(COMPone)
                else:
                    time.sleep(2)
                    print("The computer picked the wrong answer yikes")
                    componelevel = 1
                time.sleep(2)
                print("Thank you, computer one for fighting the monster")
            elif componelevel + componeS + playerS > DDeckVal[componeDcard]:
                time.sleep(2)
                print("The computer would like to offer you a bribe to fight")
                x = 0
                while x < 9:
                    if(TcardLoc[x] == COMPone):
                        pickList[track] = x
                        track += 1
                    x += 1
                offering = random.randint(0, track - 1)
                time.sleep(2)
                print("The card the computer is offering is a {}".format(TDeck[pickList[offering]]))
                time.sleep(2)
                print("This card has a power level of {}".format(TDeckVal[pickList[offering]]))
                time.sleep(2)
                userTrade = input("Would you like the computers card in trade for you helping the fight (y)es or (n)o: ")
                if userTrade == 'y':
                    TcardLoc[pickList[offering]] = COMPone
                    playerS = playerS - TDeckVal[pickList[offering]]
                    componeS = componeS + TDeckVal[pickList[offering]]
                elif userTrade == 'n':
                    time.sleep(2)
                    print("You have denied the computers bribe and the computer will be given a 1 and three chance to escape")
                    bribeEscape = random.randint(0, 2)
                    if bribeEscape == 0:
                        time.sleep(2)
                        print("The computer has escaped and will continue with no repercussions")
                    else:
                        time.sleep(2)
                        print("The computer did not escape and will be moved back to level one")
                        componelevel = 1
                if playerlevel + playerS + componeS> DDeckVal[playeroneDcard]:
                    time.sleep(2)
                    print("The computer and user won the fight and the computer will move up another level")
                    componelevel += 1
                    assignCard(COMPone)
            else:
                time.sleep(2)
                print("The computer has a 1 in 3 chance of escaping the monster")
                chance  = random.randint(0,2)
                if chance == 0:
                    time.sleep(2)
                    print("The computer has escaped the monster and will continue without repercussions")
                else:
                    time.sleep(2)
                    print("The computer didnt escape and as a result it will return back to level one")
                    playerlevel = 1
    print("Thank you for playing")
    time.sleep(2)
    print("You finished the game at level {}".format(playerlevel))
    print("The computer one finished the game at level {}".format(componelevel))
  ##clearDeck()




def assignCard(inpu):
    global changed
    global val
    global playerlevel
    global componelevel
    global playerS
    global componeS

    val1 = "false" ##creating value to kill loop
##    val2 = "false" ##creating value to kill loop
    while val1 == "false": ##while not killed
        changed1 = random.randint(0, 9)
##        changed2 = random.randint(0, 9)
        if TcardLoc[changed1] == 0: ##if the value hasnt been changed
            TcardLoc[changed1] = inpu ##assigning input value to location
            if inpu == PLAYER:
               playerS += TDeckVal[changed1]
            elif inpu == COMPone:
                componeS += TDeckVal[changed1]
            val1 = "lk" ##kill
"""   while val2 == "false": ##while not killed
       changed1 = random.randint(0, 9)
        changed2 = random.randint(0, 9)
        if DcardLoc[changed2] == 0: ##if the value hasnt been changed
            DcardLoc[changed2] = inpu ##assigning input value to location
            val2 = "lk" ##kill """

main() ## runs this mf
