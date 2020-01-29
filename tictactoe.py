""" Note: Although the skeleton below is in Python, you may use any programming language you want so long as the language supports object-oriented programming, 
          and you make use of relevant object-oriented design principles.
"""

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

    def has_winner(self):
        """
        Checks to see if there is a current winner of the game

        :return: ????
        """

        pass

    def is_input_len_two(choice):
        """
        Returns true if split is lenth 2,
        else false
        """
        if (len(choice.split(',')) == 2):
            return True
        else:
            return False


    def validate_user_input(choice):
        """
        Takes in a string and returns column and row after validating
        """
        # Split the choice by each element
        choice_l = choice.split(',')
        #print(f"CHOICE: {choice_l}")
        # Assign row and column and convert to integer
        ########### Try to convert to integer
        row = int(choice_l[0])
        column = int(choice_l[1])

        #print(f"ROW: {row} COL: {column}")
        # return column and row as tuple
        return (column, row)

    def play_game(self):
        """
        Takes moves from raw_input as comma-separated list in form (column, row, player)
            and makes a move. When a winner has been determined, the game ends
        
        :return: (str) the letter representing the player who won
        """
        while not self.has_winner():
            choice = input(f"Player {'1' if self.player1 else '2'} Make your move (row,col): ")
            (column, row) = validate_user_input(choice)
            #self.mark_square(column, row, player)
         
        pass
        
if __name__ == '__main__':
    board = Board()
    winner = board.play_game()
    print("{} has won!".format(winner))
