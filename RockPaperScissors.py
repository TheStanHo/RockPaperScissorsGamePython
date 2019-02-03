import Player
import Computer

"""
This is a simple Rock, Paper, Scissors game. This class runs the game 
Author: Stanley Ho
"""


def playerValidChoice(choice):
    if choice == "scissors" or choice == "rock" or choice =="paper":
        return True
    else:
        return False

myPlayer = Player.Player()
myComp = Computer.Computer()
print(myPlayer)
myPlayer.updateWin(True)
print("Welcome to rock paper scissors. The first player to get to 3 wins. Good Luck!")
while True:
    print("Player Score: " + str(myPlayer.playerScore) + " Vs Computer Score " + str(myComp.computerScore))
    if myPlayer.playerScore == 3:
        print("You Won")
        break
    elif myComp.computerScore == 3:
        print("You Lost")
        break
    else:
        playerChoice = input("What do you want Rock, Paper or Scissors? ")
        computerChoice = myComp.move()
        if playerValidChoice(playerChoice.lower()) is False:
            print("Please Enter a valid choice or check the spelling")

        else:
            if playerChoice.lower() == "scissors" and computerChoice == "Paper":
                print("You Won the computer chose " + str(computerChoice))
                myPlayer.updateScore(myPlayer.playerScore + 1)
            elif playerChoice.lower() == "paper" and computerChoice == "Rock":
                print("You Won the computer chose " + str(computerChoice))
                myPlayer.updateScore(myPlayer.playerScore + 1)
            elif playerChoice.lower() == "rock" and computerChoice == "Scissors":
                print("You Won the computer chose " + str(computerChoice))
                myPlayer.updateScore(myPlayer.playerScore + 1)
            elif playerChoice.lower() == "rock" and computerChoice == "Rock":
                print("Draw! The computer chose " + str(computerChoice))

            elif playerChoice.lower() == "scissors" and computerChoice == "Scissors":
                print("Draw! The computer chose " + str(computerChoice))

            elif playerChoice.lower() == "paper" and computerChoice == "Paper":
                print("Draw! The computer chose " + str(computerChoice))

            else:
                print("You Lose!" + str(computerChoice))
                myComp.updateScore(myComp.computerScore + 1)