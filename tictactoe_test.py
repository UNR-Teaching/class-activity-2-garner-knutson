#!/usr/bin/env python3
import unittest
from tictactoe import Board

class TestIsWithinBounds(unittest.TestCase):

    def test_correct_input(self):
        self.assertTrue(Board.is_within_bounds("0,2"))
        self.assertTrue(Board.is_within_bounds("1,2"))
        self.assertTrue(Board.is_within_bounds("2,1"))
        self.assertTrue(Board.is_within_bounds("0,0"))

    def test_three_tuple_input(self):
        self.assertFalse(Board.is_within_bounds("0,2,1"))
        self.assertFalse(Board.is_within_bounds("1,3,1"))

    def test_single_integer_input(self):
        self.assertFalse(Board.is_within_bounds("1"))
        self.assertFalse(Board.is_within_bounds("20"))
        self.assertFalse(Board.is_within_bounds("100"))

    def test_incorrect_char_input(self):
        self.assertFalse(Board.is_within_bounds("a"))
        self.assertFalse(Board.is_within_bounds(",,,"))
        self.assertFalse(Board.is_within_bounds("$"))
        self.assertFalse(Board.is_within_bounds("\fkenvkd"))

    def test_empty_string_input(self):
        self.assertFalse(Board.is_within_bounds(""))

    def test_very_large_user_input(self):
        self.assertFalse(Board.is_within_bounds("al;dkfjafiowjh;aosfna;oifjawo;fkas;ahjoaiwjfal;skdjfoawiejf;aldkfja;lsdkfja;weijfa;slkdfjaowiejf;alsdkfjawoiejf;asldfkja;weoifja;ldsfkjawe;oifjasdl;fkajwoe;ifja;lfkjawoe;ifjas;lfkjaweo;ifjasl;fkjawoefija;dfawleifja;faiwejf;oaijdf;lakjfo;aijwef;askdfj;aliwefja;oiefja;lsdkfja;oeijfa;lskfjao;wiefja;lskdfja;wiejfa;kfja;owiefja;slkdfja;woiefja;lskdfja;woiefj;alskdfja;owiefja;ldkfja;woeifja;lsdkfja;owiefja;lsdkfja;owiefj;aldkfja;lfewi;awejf;lawe;fj;fjoi69"*10000))

class TestConvertUserInput(unittest.TestCase):

    def test_valid_input(self):
        self.assertEqual(Board.convert_user_input("0,2"), (0,2))
        self.assertEqual(Board.convert_user_input("1,2"), (1,2))
        self.assertEqual(Board.convert_user_input("2,1"), (2,1))
        self.assertEqual(Board.convert_user_input("0,0"), (0,0))


class TestRows(unittest.TestCase):
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

    def test_empty(self):
        self.game.board = [['_', '_', '_'],
                           ['_', '_', '_'],
                           ['_', '_', '_']]
        self.assertEqual(self.game.check_rows(), 0)

    def test_no_rows(self):
        self.game.board = [['X', '_', 'O'],
                           ['_', 'X', 'O'],
                           ['_', 'X', 'O']]
        self.assertEqual(self.game.check_rows(), 0)

class TestColumns(unittest.TestCase):
    def setUp(self):
        self.game = Board()

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
        self.assertEqual(self.game.check_columns(), 0)

    def test_no_cols(self):
        self.game.board = [['X', 'X', 'X'],
                           ['_', 'O', 'O'],
                           ['_', 'X', 'O']]
        self.assertEqual(self.game.check_columns(), 0)

class TestDiagonal(unittest.TestCase):
    def setUp(self):
        self.game = Board()

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

    def test_empty(self):
        self.game.board = [['_', '_', '_'],
                           ['_', '_', '_'],
                           ['_', '_', '_']]
        self.assertEqual(self.game.check_diagonals(), 0)

    def test_no_cols(self):
        self.game.board = [['X', 'X', 'X'],
                           ['_', 'O', 'O'],
                           ['_', 'X', 'O']]
        self.assertEqual(self.game.check_diagonals(), 0)

class TestHasThreeInARow(unittest.TestCase):
    def setUp(self):
        self.game = Board()

    def test_player1_threeInARow(self):
        self.game.board = [['X', '_', 'O'],
                           ['X', 'O', '_'],
                           ['X', '_', '_']]
        self.assertEqual(self.game.has_three_in_a_row(), 1)

    def test_player2_threeInARow(self):
        self.game.board = [['X', '_', 'O'],
                           ['O', 'O', 'O'],
                           ['X', 'X', '_']]
        self.assertEqual(self.game.has_three_in_a_row(), 2)


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


class TestBoardFull(unittest.TestCase):
    def setUp(self):
        self.game = Board()

    def test_board_full(self):
        self.game.board = [['X', 'O', 'X'],
                           ['X', 'O', 'O'],
                           ['O', 'X', 'O']]
        self.assertTrue(self.game.board_full())

    def test_board_not_empty(self):
        self.game.board = [['X', 'O', 'X'],
                           ['X', 'O', 'O'],
                           ['O', 'X', '_']]
        self.assertFalse(self.game.board_full())


if __name__ == '__main__':
    unittest.main()
