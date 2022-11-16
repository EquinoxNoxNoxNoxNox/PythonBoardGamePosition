import random
import time
################### CONSOLE TEXT COLORIZATION LIBRARY
import os
#Function to clear/reset console texts
clear = lambda: os.system('cls')
clear()

class Fore:
    RED = '\033[91m'
    YELLOW = '\033[93m'
    LIGHTBLUE_EX = '\033[94m'
    LIGHTCYAN_EX = '\033[96m'
    LIGHTBLACK_EX = ""
    RESET = ""
    WHITE = '\033[95m'
class Back(Fore):
    LIGHTRED_EX = '\033[91m'
    LIGHTWHITE_EX = '\033[0m'
###################

################### Programmer signature
print(Fore.RED +"#" * 29)
print(Fore.RED + "####",end="")
print(Fore.LIGHTBLUE_EX + "Coded by6 ",end="")
print(Fore.YELLOW + "$AE3D",end="")
print(Fore.RED + "####")
print(Fore.YELLOW + "GITHUB:",end="")
print(Fore.LIGHTBLUE_EX + "https://github.com/EquinoxNoxNoxNoxNox")
print(Fore.RED +"#" * 29 + '\n\n')
input("PRESS ENTER TO CONTINUE..")
###################
clear()
#The game deck
GameDeck = list(range(1,17))

#Boolean flag to see game is going on
IsGameGoingOn = True

#Boolean flag to determine players turn
IsUserTurn = random.choice([True,False])

#Dictinary for saving numbers that were choosed by players
Players = {
    "User" : [],
    "Computer" : []
}

#Function to print the board
def PrintDeck() -> None:
    print(Fore.RED+"COMPUTER : ",end="")
    print(Players["Computer"])
    print(Fore.LIGHTBLUE_EX+"YOU : ",end="")
    print(Players["User"])
    print(Fore.LIGHTCYAN_EX+" "+"-"*32+"\n")
    
    #A for loop from 1 to 4 (because each of our rows has 4 numbers in it)
    #EXAMPLE : | 6 | 7 | 8 | 9|
    for ForthIndex in range(1,5):
        #This variable holds 4 items by index selection
        #(ForthIndex - 1) * 4 >>>>> equals to 0 in first round of loop
        # ForthIndex*4 >>>>>> equals to 4 in first round of loop
        RowNumbers = GameDeck[(ForthIndex - 1) * 4 : ForthIndex*4]
        
        #X and O text stylization in game board is done with this for loop
        #it iterates through a row(RowNumbers variable)
        for _index in range(len(RowNumbers)):
            if RowNumbers[_index]=="x":
                RowNumbers[_index]=Fore.LIGHTBLUE_EX + "X" + Fore.RESET
            elif RowNumbers[_index]=="o":
                RowNumbers[_index]=Fore.RED + "O" + Fore.RESET
        
        #Adding coloumn spacing by using a "List Decorator"(single-line for-loop)
        #We add space in front and back of each element by using a single-line for-loop
        RowNumbers = ["   "+str(x)+Fore.LIGHTCYAN_EX+"\t|"+Fore.RESET for x in RowNumbers]
        
        #Print each row:
        print(Fore.LIGHTCYAN_EX+" |"+Fore.RESET+f"{RowNumbers[0]}{RowNumbers[1]}{RowNumbers[2]}{RowNumbers[3]}\n")
        print(Fore.LIGHTCYAN_EX+" "+"-"*32 + "\n")

# Function to check the winner
# parameter:Player >>>> key name in "Players" Dictionary
def IsWin(Player:str) -> bool:
    #List of all available win combinations
    Combinations = [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16],
        [1,5,9,13],
        [2,6,10,14],
        [3,7,11,15],
        [4,8,12,16],
        [1,6,11,16],
        [4,7,10,13],
        [2,7,12],
        [3,6,9],
        [5,10,15],
        [8,11,14]
    ]
    
    #This "if" says ignore the operation if player dont have atleast three numbers choosen
    if len(Players[Player]) < 3:
        return False
    
    for index in range(len(Players[Player])):
        #Checks every possible combination for each of items in Players[player]
        for Combination in Combinations:
            ListLength = len(Combination)
            if Players[Player][index:ListLength] == Combination:
                return True

#Function to validate user input
def UserInputValidation()->int:
    userInput = input("Enter number: ")
    try:
        #ERROR 1 : if userInput is not integer , program will error in this line
        userInput=int(userInput)
        
        if userInput not in GameDeck:
            #ERROR 2 : custom error to just get program to the "except" block
            raise Exception("Just to goto 'except'")
        return userInput
    except:#it catches those two possible errors
        clear()
        PrintDeck()
        print(Fore.RED+"!!!ENTER A NUMBER FROM THE DECK!!!")
        return UserInputValidation()

# Function to end the game
def EndGame(Winner:str) -> None:
    #Change game condition flag to False
    #While loop will stop working
    global IsGameGoingOn
    IsGameGoingOn = False

    #Style of text of the winner
    WinnerTextStyle = {
        "User" : Back.YELLOW + Fore.LIGHTBLUE_EX,
        "Computer" : Back.LIGHTRED_EX + Fore.WHITE,
        "Tie" : Back.WHITE + Fore.LIGHTBLUE_EX,
    }[Winner]
    clear()
    PrintDeck()
    print(Back.LIGHTWHITE_EX+Fore.LIGHTBLACK_EX + "GAME FINISHED" + Fore.RESET + Back.RESET)
    if(Winner != "Tie"):
        print(WinnerTextStyle + f"{Winner} WON THE GAME!" + Fore.RESET + Back.RESET)
    else:
        print(WinnerTextStyle + f"No one WON THE GAME!" + Fore.RESET + Back.RESET)

# Function computer to pick a random
def ComputerChoose():
    clear()
    PrintDeck()
    print(Fore.RED+"computer choosing..."+ Fore.RESET)

    time.sleep(1) # simulates choosing time

    Chosed=random.choice([x for x in GameDeck if type(x) != str]) # chooses randomly from the deck
    GameDeck[GameDeck.index(Chosed)] = "o" # replace the choosed number with an "o" character
    Players['Computer'].append(Chosed)
    if IsWin("Computer"): # Check if computer has a win combination
        EndGame("Computer")
    clear()
    PrintDeck()

    global IsUserTurn ## Passes the turn to user
    IsUserTurn = True


if __name__ == "__main__":
    PrintDeck()
    while IsGameGoingOn:
        if IsUserTurn:
            #checks if all the numbers turned into X and O
            if not [x for x in GameDeck if type(x) == int]:
                EndGame("Tie")
                break
            UserInput = UserInputValidation()
            Players["User"].append(UserInput)
            GameDeck[GameDeck.index(UserInput)] = "x"
            if IsWin("User"):
                EndGame("User")
                
            IsUserTurn=False
        else:
            ComputerChoose()