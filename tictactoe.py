""" Note: Although the skeleton below is in Python, you may use any programming language you want so long as the language supports object-oriented programming,
          and you make use of relevant object-oriented design principles.
"""
import re


class Board(object):

    def __init__(self):
        """
        Initializes the Board of size 3x3
        """
        self.board = [['_', '_', '_'],
                      ['_', '_', '_'],
                      ['_', '_', '_']]
        self.player1 = True

        pass

    def mark_square(self, column, row, player):
        """
        Marks a square at coordinate (column, row) for player

        :param column: (int) the 0-indexed column of the Board to mark
        :param row: (int) the 0-indexed row of the Board to mark
        :param player: (str) the X or O representation of which player to mark in square

        :return: ????
        """

        pass

    def check_rows(self):
        # Check for three in a row in the rows
        for row in self.board:
            if row[0] == row[1] == row[2] and row[0] != '_':
                return 1 if row[0] == 'X' else 2
        return 0

    def check_columns(self):
        # Check for 3 in a row in a column
        for column in list(map(list, zip(*self.board))):
            if column[0] == column[1] == column[2] and column[0] != '_':
                return 1 if column[0] == 'X' else 2
        return 0

    def check_diagonals(self):
        # Check for 3 in a row in a diagonal
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != '_':
            return 1 if self.board[0][0] == 'X' else 2
        elif self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != '_':
            return 1 if self.board[0][2] == 'X' else 2
        else:
            return 0

    def has_three_in_a_row(self):
        """
                Checks to see if there is a current winner of the game

                :return: 1 if player 1 has won, 2 if player 2 has won or 0 if no one has won
        """
        results = [self.check_rows(), self.check_columns(), self.check_diagonals()]
        for result in results:
            if result != 0:
                return result
        return 0

    def board_full(self):
        for row in self.board:
            for i in row:
                if i != '_':
                    return False

        return True

    def has_winner(self):

        pass

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

    def play_game(self):
        """
        Takes moves from raw_input as comma-separated list in form (column, row, player)
            and makes a move. When a winner has been determined, the game ends
        
        :return: (str) the letter representing the player who won
        """
        while not self.has_winner():

            choice = input(f"Player {'1' if self.player1 else '2'} Make your move (row,col): ")

            if is_within_bounds(choice):

                print("input is correct")
                (row, column) = convert_user_input(choice)

            else:

                print("input is incorrect skipping to top of loop")
                continue

        pass


if __name__ == '__main__':
    board = Board()
    winner = board.play_game()
    print("{} has won!".format(winner))
