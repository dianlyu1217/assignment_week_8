import unittest
from unittest.mock import patch
from logic import Game, Human, Robot


class TestTicTacToeGame(unittest.TestCase):
	def setUp(self):
		# Set up a game with two human players for testing
		self.game = Game(single=False)
	
	def test_game_initialized_with_empty_board(self):
		self.assertEqual(self.game.board, [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']])
	
	def test_game_initialized_with_players(self):
		self.assertIsInstance(self.game.x, Human)
		self.assertIsInstance(self.game.y, Human)
	
	def test_players_assigned_unique_symbols(self):
		self.assertNotEqual(self.game.x.name, self.game.y.name)
	
	def test_players_alternate_turns(self):
		if self.game.turn is self.game.x:
			self.game.change_turn()
			self.assertEqual(self.game.turn, self.game.y)
		else:
			self.game.change_turn()
			self.assertEqual(self.game.turn, self.game.x)
	
	def test_valid_moves(self):
		# Mock user input for a valid move
		with patch('builtins.input', side_effect=['0', '0']):
			self.game.turn.do_round()
			self.assertEqual(self.game.board[0][0], self.game.turn.name)
	
	def test_invalid_moves(self):
		# Mock user input for an invalid move (out of bounds)
		with patch('builtins.input', side_effect=['-1', '0']):
			self.assertEqual(False, self.game.x.check_input('-1', '0'))
			# with self.assertRaises(ValueError):
			#     self.game.turn.do_round()
	
	def test_detect_winner(self):
		# Manually set up a winning condition
		self.game.board = [['X', 'O', ' '], ['X', 'O', ' '], ['X', ' ', 'O']]
		self.assertTrue(self.game.judge_winner())
	
	def test_detect_draw(self):
		# Manually set up a draw condition
		self.game.board = [['X', 'O', 'X'], ['X', 'O', 'O'], ['O', 'X', 'X']]
		self.assertTrue(self.game.judge_winner())


if __name__ == '__main__':
	unittest.main()
