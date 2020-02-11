from Board import Board
from Player import Player


class Game:
    def __init__(self):
        self.board = Board()
        self.player1 = Player(1)
        self.player2 = Player(2)