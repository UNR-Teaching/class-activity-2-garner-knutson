import sys


class Player:
	def __init__(self, player_number):
		self.player_number = player_number
		if player_number == 1:
			self.player_symbol = 'X'

		elif player_number == 2:
			self.player_symbol = 'O'

		else:
			print('Invalid player number')
			sys.exit(0)

	def is_within_bounds(choice):
		"""
		Returns true if the numeric input is within the bounds of the board
		"""
		pattern = "^[0-2]\,[0-2]$"
		return re.match(pattern, choice)

	def convert_user_input(choice):
		"""
		Takes in a string and returns column and row after validating
		"""
		# Split the choice by each element
		choice_l = choice.split(',')
		# print(f"CHOICE: {choice_l}")
		# Assign row and column and convert to integer
		########### Try to convert to integer
		row = int(choice_l[0])
		column = int(choice_l[1])

		# print(f"ROW: {row} COL: {column}")
		# return column and row as tuple
		return (row, column)

	def get_move(self):
		choice = input(f"Player {'1' if (self.player_number == 1) else '2'} Make your move (row,col): ")
		if self.is_within_bounds(choice):
			move = Move(convert_user_input(choice),self)
			return move
		else:
			return None
