"""
This class is a representation of the Player. With functions to update the score and
update the win status.
Author: Stanley Ho
"""
class Player:
    playerScore = 0
    playerWin = False

    def updateScore(self, playerScore):
        self.playerScore = playerScore

    def updateWin(self, playerWin):
        self.playerWin = playerWin

    def __repr__(self):
        return str(self.playerScore) + " " + str(self.playerWin)