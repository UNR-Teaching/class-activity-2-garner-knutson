#!/usr/bin/env python3
import unittest
from tictactoe import Board


class TestValidInput(unittest.TestCase):

    def test_validate_user_input(self):
        self.assertEqual(Board.validate_user_input("1,1"), (1, 1))

    def test_is_input_len_two(self):
        self.assertTrue(Board.is_input_len_two("1,3"))
        self.assertFalse(Board.is_input_len_two("1,3,1"))
        self.assertFalse(Board.is_input_len_two("1"))


class TestHasThreeInARow(unittest.TestCase):
    def setUp(self):
        self.game = Board()

    def test_row1_player1(self):
        self.game.board = [['X', 'X', 'X'],
                           ['_', '_', '_'],
                           ['_', '_', '_']]

        self.assertEqual(self.game.check_rows(), 1)

    def test_row1_player2(self):
        self.game.board = [['O', 'O', 'O'],
                           ['_', '_', '_'],
                           ['_', '_', '_']]

        self.assertEqual(self.game.check_rows(), 2)

    def test_row2_player1(self):
        self.game.board = [['_', '_', '_'],
                           ['X', 'X', 'X'],
                           ['_', '_', '_']]

        self.assertEqual(self.game.check_rows(), 1)

    def test_row2_player2(self):
        self.game.board = [['_', '_', '_'],
                           ['O', 'O', 'O'],
                           ['_', '_', '_']]

        self.assertEqual(self.game.check_rows(), 2)

    def test_row3_player1(self):
        self.game.board = [['_', '_', '_'],
                           ['_', '_', '_'],
                           ['X', 'X', 'X']]

        self.assertEqual(self.game.check_rows(), 1)

    def test_row3_player2(self):
        self.game.board = [['_', '_', '_'],
                           ['_', '_', '_'],
                           ['O', 'O', 'O']]

        self.assertEqual(self.game.check_rows(), 2)

    def test_diagonal1_player1(self):
        self.game.board = [['X', '_', '_'],
                           ['_', 'X', '_'],
                           ['_', '_', 'X']]

        self.assertEqual(self.game.check_diagonals(), 1)

    def test_diagonal1_player2(self):
        self.game.board = [['O', '_', '_'],
                           ['_', 'O', '_'],
                           ['_', '_', 'O']]

        self.assertEqual(self.game.check_diagonals(), 2)

    def test_diagonal2_player1(self):
        self.game.board = [['_', '_', 'X'],
                           ['_', 'X', '_'],
                           ['X', '_', '_']]

        self.assertEqual(self.game.check_diagonals(), 1)

    def test_column1_player1(self):
        self.game.board = [['X', '_', '_'],
                           ['X', '_', '_'],
                           ['X', '_', '_']]

        self.assertEqual(self.game.check_columns(), 1)

    def test_column1_player2(self):
        self.game.board = [['O', '_', '_'],
                           ['O', '_', '_'],
                           ['O', '_', '_']]

        self.assertEqual(self.game.check_columns(), 2)

    def test_column2_player1(self):
        self.game.board = [['_', 'X', '_'],
                           ['_', 'X', '_'],
                           ['_', 'X', '_']]

        self.assertEqual(self.game.check_columns(), 1)

    def test_column2_player2(self):
        self.game.board = [['_', 'O', '_'],
                           ['_', 'O', '_'],
                           ['_', 'O', '_']]

        self.assertEqual(self.game.check_columns(), 2)

    def test_column3_player1(self):
        self.game.board = [['_', '_', 'X'],
                           ['_', '_', 'X'],
                           ['_', '_', 'X']]

        self.assertEqual(self.game.check_columns(), 1)

    def test_column3_player2(self):
        self.game.board = [['_', '_', 'O'],
                           ['_', '_', 'O'],
                           ['_', '_', 'O']]

        self.assertEqual(self.game.check_columns(), 2)

    def test_empty(self):
        self.game.board = [['_', '_', '_'],
                           ['_', '_', '_'],
                           ['_', '_', '_']]
        self.assertEqual(self.game.has_three_in_a_row(), 0)

    def test_cats_game(self):
        self.game.board = [['X', 'O', 'X'],
                           ['X', 'O', 'O'],
                           ['O', 'X', 'O']]
        self.assertEqual(self.game.has_three_in_a_row(), 0)




if __name__ == '__main__':
    unittest.main()
