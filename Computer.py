from random import randint
"""
This class is a representation of the computer. With functions to update the score,
update the win status and generate it's move. 
Author: Stanley Ho
"""
class Computer:
    computerScore = 0
    computerWin = False

    def updateScore(self, computerScore):
        self.computerScore = computerScore

    def updateWin(self, computerWin):
        self.computerScore = computerWin

    def move(self):
        moves = ["Scissors", "Rock", "Paper"]
        compMove = moves[randint(0, 2)]
        return compMove

    def __repr__(self):
        return str(self.computerScore) + " " + str(self.computerWin)