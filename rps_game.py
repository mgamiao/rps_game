import random
import time
import sys
import os
clear = lambda: os.system('cls')
clear()

power = ["R", "P", "S"] #, "r", "p", "s"
YourScore = 0
SBScore = 0
rounds = 1

def End():
    global power
    global you
    global battle
    global rounds
    global YourScore
    global SBScore
    global Scores
    global Name
    print("\n" + "     END OF ALL ROUNDS!" + "\n")
    Points()
    if YourScore > SBScore:
        print("     " + Name + " is the WINNER!!!" + "\n\n")
        Rematch()
    elif YourScore < SBScore:
        print("     StarkBoy WINS!!!" + "\n\n")
        Rematch()
    elif YourScore == SBScore:
        print("     ITS A TIE!!!" + "\n\n")
        Rematch()

def Round():
    print("\n" + "                         Round " + str(rounds) + "\n")

def Text():
    print("\n" + "     Your Opponent will be the SUPER AI - STARKBOY!!!")
    print("\n" + "     Choose your power!")
    print("     R = Rock" + "\n" + "     P = Paper" + "\n" + "     S = Scissor" + "\n")

def Front():
    print("___________                                                       __  ._._._.")
    print("\__    ___/___  __ _________  ____  _____    _____   ____   _____/  |_| | | |")
    print("  |    | /  _ \|  |  \_  __ \/    \ \__  \  /     \_/ __ \ /    \   __\ | | |")
    print("  |    |(  <_> )  |  /|  | \/   |  \ / __ \|  Y Y  \  ___/|   |  \  |  \|\|\|")
    print("  |____| \____/|____/ |__|  |___|   (____  /__|_|  /\___  >___|  /__|  ______")
    print("                                  \/     \/      \/     \/     \/      \/\/\/")

def Back():
    print("___________.__                    __     _____.___.              ___________            __________.__                 .__              ._._._.")
    print("\__    ___/|  |__  _____    ____ |  | __ \__  |   | ____  __ __  \_   _____/__________  \______   \  | _____   ___.__.|__| ____    ____| | | |")
    print("  |    |   |  |  \ \__  \  /    \|  |/ /  /   |   |/  _ \|  |  \  |    __)/  _ \_  __ \  |     ___/  | \__  \ <   |  ||  |/    \  / ___\ | | |")
    print("  |    |   |   Y  \ / __ \|   |  \    <   \____   (  <_> )  |  /  |     \(  <_> )  | \/  |    |   |  |__/ __ \ \___  ||  |   |  \/ /_/  >|\|\|")
    print("  |____|   |___|   (____  /___|  /__|_ \  / ______|\____/|____/   \___  / \____/|__|     |____|   |____(____   / ____||__|___|  /\___  /______")
    print("                \/      \/     \/     \/  \/                          \/                                    \/ \/             \//_____/ \/\/\/")

def Points():
    global power
    global you
    global battle
    global rounds
    global YourScore
    global SBScore
    global Scores
    global Name

    Scores = print("     StarkBoy's Score is: " + str(SBScore) + "     " + Name + "'s Score is: " + str(YourScore) +   "\n")

def Rematch():
    global power
    global you
    global battle
    global rounds
    global YourScore
    global SBScore
    global Scores
    global Name

    Banse = str(input("     Do You Want To Play Again? Y/N: "))
    if (Banse == "Y" or Banse == "y"):
        YourScore = 0
        SBScore = 0
        rounds = 1
        clear()
        Opening()
    if (Banse == "N" or Banse == "n"):
        clear()
        Back()
        time.sleep(3)
        clear()
        sys.exit()
    else:
        print("     Invalid Choice... Try Again")
        time.sleep(2)
        clear()
        Front()
        End()
        Rematch()

def LABAN():
    global power
    global you
    global battle
    global rounds
    global YourScore
    global SBScore
    global Scores
    global Name

    if (you == "R" or you == "r") and battle == "R":
        print("\n" + "     It's a TIE!")
        rounds = rounds + 1
        time.sleep(2)
        clear()
        Opening()
    elif (you == "P" or you == "p") and battle == "P":
        print("\n" + "     It's a TIE!")
        rounds = rounds + 1
        time.sleep(2)
        clear()
        Opening()
    elif (you == "S" or you == "s") and battle == "S":
        print("\n" + "     It's a TIE!")
        rounds = rounds + 1
        time.sleep(2)
        clear()
        Opening()
    elif (you == "R" or you == "r") and battle == "P":
        print("\n" + "     StarkBoy WINS!")
        SBScore = SBScore + 1
        rounds = rounds + 1
        time.sleep(2)
        clear()
        Opening()
    elif (you == "R" or you == "r") and battle == "S":
        print("\n" + "     " + Name + " WINS!")
        YourScore = YourScore + 1
        rounds = rounds + 1
        time.sleep(2)
        clear()
        Opening()
    elif (you == "P" or you == "p") and battle == "R":
        print("\n" + "     " + Name + " WINS!")
        YourScore = YourScore + 1
        rounds = rounds + 1
        time.sleep(2)
        clear()
        Opening()
    elif (you == "P" or you == "p") and battle == "S":
        print("\n" + "     StarkBoy WINS!")
        SBScore = SBScore + 1
        rounds = rounds + 1
        time.sleep(2)
        clear()
        Opening()
    elif (you == "S" or you == "s") and battle == "R":
        print("\n" + "     StarkBoy WINS!")
        SBScore = SBScore + 1
        rounds = rounds + 1
        time.sleep(2)
        clear()
        Opening()
    elif (you == "S" or you == "s") and battle == "P":
        print("\n" + "     " + Name + " WINS!")
        YourScore = YourScore + 1
        rounds = rounds + 1
        time.sleep(2)
        clear()
        Opening()

def Start():
    global power
    global you
    global battle
    global rounds
    global YourScore
    global SBScore
    global Scores
    global Name

    while rounds != 6:
        Round()
        you = str(input("     StarkBoy chooses: ???" + "     Choose your power!: "))

        if (you == "R" or you == "r"):
            battle = random.choice(power)
            clear()
            Front()
            Text()
            Points()
            Round()
            print("     StarkBoy chooses: " + battle + "     Choose your power!: " + (you))
            LABAN()
        elif (you == "P" or you == "p"):
            battle = random.choice(power)
            clear()
            Front()
            Text()
            Points()
            Round()
            print("     StarkBoy chooses: " + battle + "     Choose your power!: " + (you))
            LABAN()
        elif (you == "S" or you == "s"):
            battle = random.choice(power)
            clear()
            Front()
            Text()
            Points()
            Round()
            print("     StarkBoy chooses: " + battle + "     Choose your power!: " + (you))
            LABAN()
        else:
            print("\n" + "     Invalid Power...Try Again")
            time.sleep(2)
            clear()
            Opening()

        if rounds == 6:
            clear()
            Front()
            End()
             
def Opening():
    global power
    global you
    global battle
    global rounds
    global YourScore
    global SBScore
    global Scores
    global Name
    
    Front()
    Text()
    Points()
    Start()

def Player():
    global power
    global you
    global battle
    global rounds
    global YourScore
    global SBScore
    global Scores
    global Name

    Front()
    print("\n\n" + "     WELCOME TO THE MOST INTENSE ROCK-PAPER-SCISSORS TOURNAMENT OF ALL TIME!!!")
    Name = str(input("\n\n" + "     WHAT IS YOUR NAME CHALLENGER? "))
    clear()
    Opening()

Player()