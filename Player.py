import sys


class Player:
    def __init__(self, player_number):
        if player_number == 1:
            self.player_symbol = 'X'

        elif player_number == 2:
            self.player_symbol = 'O'

        else:
            print('Invalid player number')
            sys.exit(0)