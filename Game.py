from Board import Board
from Player import Player


class Game:
    def __init__(self):
        self.board = Board()
        self.player1 = Player(1)
        self.player2 = Player(2)


   def play_game(self):
        while not self.board.has_winner():
            move = self.player1.get_move()
            while not self.board.add_move(move):
                move = self.player1.get_move()
            if not self.board.has_winner():
                self.player2.get_move()

            # choice = input(f"Player {'1' if self.player1 else '2'} Make your move (row,col): ")
            #
            # if is_within_bounds(choice):
            #
            #     print("input is correct")
            #     (row, column) = convert_user_input(choice)
            #
            # else:
            #
            #     print("input is incorrect skipping to top of loop")
            #     continue
