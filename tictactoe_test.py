#!/usr/bin/env python3
import unittest
from tictactoe import Board

class TestValidInput(unittest.TestCase):

    def test_validate_user_input(self):
        self.assertEqual(Board.validate_user_input("1,1"), (1,1))

    def test_is_input_len_two(self):
        self.assertTrue(Board.is_input_len_two("1,3"))
        self.assertFalse(Board.is_input_len_two("1,3,1"))
        self.assertFalse(Board.is_input_len_two("1"))


if __name__ == '__main__':
    unittest.main()
