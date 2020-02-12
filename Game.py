from Board import Board
from Player import Player


class Game:
	def __init__(self):
		self.board = Board()
		self.player1 = Player(1)
		self.player2 = Player(2)

	def play_game(self):
		while not self.board.has_three_in_a_row():
			self.get_player_move(self.player1.player_number)
			if not self.board.has_winner():
				self.get_player_move(self.player2.player_number)

	def get_player_move(self, player_number):
		if player_number == 1:
			move = self.player1.get_move()
			while not self.board.add_move(move):
				move = self.player1.get_move()
		else:
			move = self.player2.get_move()
			while not self.board.add_move(move):
				move = self.player2.get_move()


if __name__ == '__main__':
    Game().play_game()