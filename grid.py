from os import system
from random import randint
from colors import printc
class Square:
	visited = False
	value = -1
	def __init__(self, val):
		self.value = val
class Grid:
	grid = [[]]
	height = 0
	width = 0
	position = [-1,-1]
	result = 0
	max = 0
	end = False
	invalid = False
	def __init__(self, h, w, val=9):
		self.height = h
		self.width = w
		self.grid = [[Square(randint(1,val)) for j in range(w) ] for i in range(h)]
		self.max = sum([sum([self.grid[i][j].value for j in range(w)]) for i in range(h)])
		self.position = [randint(0, h-1), randint(0, w-1)]
		self.result = self.grid[self.position[0]][self.position[1]].value
		self.grid[self.position[0]][self.position[1]].visited = True
	### display
	def display(self):
		system('clear')
		for i in range(self.height): # gonna be shorter
			for j in range(self.width):
				if [i,j] == self.position: print('+' if self.end else '#', end="")
				elif self.grid[i][j].visited: print(' ', end="")
				else: printc(self.grid[i][j].value)
			print ('\n', end="")
		print()
		print("Result: {} / {},\t {:04.2f}% \t {} \t {} \t {}".format(self.result, 
			self.max, 100*self.result/self.max, self.position, "Invalid move" if self.invalid else "", "Game Over!" if self.end else ""))
	def importFrom(self, path):
		pass
	def show(self):
		print (self.height, self.width, self.position[0], self.position[1])
		for i in range(self.height): # gonna be shorter
			for j in range(self.width):
				print(self.grid[i][j].value, end="")
			print()
		
		pass
	def gameOver(self):
		self.end = True
		self.display()
	### moves
	def moveUp(self):
		step = self.grid[self.position[0] - 1][self.position[1]].value
		for i in range(1, step + 1):
			self.grid[self.position[0] - i][self.position[1]].visited = True
			self.result += self.grid[self.position[0] - i][self.position[1]].value
		self.position[0] -=	step
	def moveDown(self):
		step = self.grid[self.position[0] + 1][self.position[1]].value
		for i in range(1, step + 1):
			self.grid[self.position[0] + i][self.position[1]].visited = True
			self.result += self.grid[self.position[0] + i][self.position[1]].value 
		self.position[0] += step
	def moveLeft(self):
		step = self.grid[self.position[0]][self.position[1] - 1].value
		for i in range(1, step + 1):
			self.grid[self.position[0]][self.position[1] - i].visited = True
			self.result += self.grid[self.position[0]][self.position[1] - i].value
		self.position[1] -= step
	def moveRight(self):
		step = self.grid[self.position[0]][self.position[1] + 1].value
		for i in range(1, step + 1):
			self.grid[self.position[0]][self.position[1] + i].visited = True
			self.result += self.grid[self.position[0]][self.position[1] + i].value
		self.position[1] += step

	def move(self, num):
		moves = [self.moveUp, self.moveDown, self.moveRight, self.moveLeft]
		moves[num]()
	### moves check
	def chkUp(self):
		if self.position[0] == 0: 
			return False
		step = self.grid[self.position[0] - 1][self.position[1]].value # cell that we gonna step on
		if self.position[0] - step < 0:
			return False
		return not any([self.grid[self.position[0] - i][self.position[1]].visited for i in range(1, step + 1)])
	def chkDown(self):
		if self.position[0] == self.height - 1: 
			return False
		step = self.grid[self.position[0] + 1][self.position[1]].value # cell that we gonna step on
		if self.position[0] + step > self.height - 1:
			return False
		return not any([self.grid[self.position[0] + i][self.position[1]].visited for i in range(1, step + 1)])
	def chkLeft(self):
		if self.position[1] == 0:
			return False
		step = self.grid[self.position[0]][self.position[1] - 1].value
		if self.position[1] - step < 0:
			return False
		return not any([self.grid[self.position[0]][self.position[1] - i].visited for i in range(1, step + 1)])
	def chkRight(self):
		if self.position[1] == self.width - 1:
			return False
		step = self.grid[self.position[0]][self.position[1] + 1].value
		if self.position[1] + step > self.width - 1:
			return False
		return not any([self.grid[self.position[0]][self.position[1] + i].visited for i in range(1, step + 1)])
