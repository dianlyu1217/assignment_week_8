import logging
import random

logger = logging.getLogger('tictactoe')


class Game:
	def __init__(self, single: bool):
		self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
		self.x = Human('X', self)
		if single:
			self.y = Robot('O', self)
		else:
			self.y = Human('O', self)
		self.turn = random.choice([self.x, self.y])
		self.show_board()
	
	def show_board(self):
		for row in self.board:
			print(row)
		print('---current board---')
	
	def change_turn(self):
		if self.turn is self.x:
			self.turn = self.y
		else:
			self.turn = self.x
	
	def judge_winner(self) -> bool:
		for i in range(0, 3):
			if self.board[i][0] != ' ' and self.board[i][0] == self.board[i][1] == self.board[i][2]:
				logger.info('{turn} won'.format(turn=self.board[i][0]))
				print(self.board[i][0], ' Won')
				return True
		for i in range(0, 3):
			if self.board[0][i] != ' ' and self.board[0][i] == self.board[1][i] == self.board[2][i]:
				logger.info('{turn} won'.format(turn=self.board[0][i]))
				print(self.board[0][i], ' Won')
				return True
		if self.board[1][1] != ' ' and (
				self.board[0][0] == self.board[1][1] == self.board[2][2] or self.board[2][0] == self.board[1][1] ==
				self.board[0][2]):
			logger.info('{turn} won'.format(turn=self.board[1][1]))
			print(self.board[1][1], ' Won')
			return True
		for row in self.board:
			for col in row:
				if col == ' ':
					return False
		logger.info('Draw')
		print('Draw')
		return True


class Gamer:
	def __init__(self, name: str, game: Game):
		self.name = name
		self.game = game


class Human(Gamer):
	def __init__(self, name: str, game: Game):
		super().__init__(name, game)
	
	def do_round(self):
		while True:
			r = input("[{turn} turn] input row index: ".format(turn=self.name))
			c = input("[{turn} turn] input col index: ".format(turn=self.name))
			if self.check_input(r, c):
				self.game.board[int(r)][int(c)] = self.name
				break
	
	def check_input(self, r: str, c: str) -> bool:
		if not r.isdigit() or not c.isdigit():
			logger.error('{turn} input invalid: {r},{c}'.format(turn=self.name, r=r, c=c))
			print('input invalid, not int')
			return False
		elif int(r) < 0 or int(r) > 2 or int(c) < 0 or int(c) > 2:
			logger.error('{turn} input invalid: {r},{c}'.format(turn=self.name, r=r, c=c))
			print('input invalid, should >=0 and <=2')
			return False
		elif self.game.board[int(r)][int(c)] != ' ':
			logger.error('{turn} input invalid: {r},{c}'.format(turn=self.name, r=r, c=c))
			print('input invalid, index already input')
			return False
		else:
			logger.info('received {turn} input: {r},{c}'.format(turn=self.name, r=r, c=c))
			return True


class Robot(Gamer):
	def __init__(self, name: str, game: Game):
		super().__init__(name, game)
	
	def do_round(self):
		empty_coordinates = [(row, col) for row in range(3) for col in range(3) if self.game.board[row][col] == ' ']
		r, c = random.choice(empty_coordinates)
		logger.info('{turn} random input: {r},{c}'.format(turn=self.name, r=r, c=c))
		self.game.board[r][c] = self.name
		print('[{turn} turn] robot automatic input index: {r},{c}'.format(turn=self.name, r=r, c=c))
