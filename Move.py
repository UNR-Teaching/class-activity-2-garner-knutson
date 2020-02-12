from Player import Player

class Move():

    def __init__(self, row, col, player):
        self.location = (row,col)
        self.player = player