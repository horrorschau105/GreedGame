from os import system
from random import randint
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
	steps = []
	def __init__(self, h, w, val=9):
		self.height = h
		self.width = w
		self.grid = [[Square(randint(1,val)) for j in range(w) ] for i in range(h)]
		self.max = sum([sum([self.grid[i][j].value for j in range(w)]) for i in range(h)])
		self.position = [randint(0, h-1), randint(0, w-1)]
		self.result = self.grid[self.position[0]][self.position[1]].value
		self.grid[self.position[0]][self.position[1]].visited = True

	def score(self): # result in percentage
		return self.result* 100 / self.max
	def importFrom(self, height, width, position, values):
		self.height, self.width, self.position = height, width, position
		self.grid = [[Square(values[i][j]) for j in range(self.width) ] for i in range(self.height)]
		self.result = self.grid[self.position[0]][self.position[1]].value
		self.grid[self.position[0]][self.position[1]].visited = True
		self.max = sum([sum([self.grid[i][j].value for j in range(self.width)]) for i in range(self.height)])

	def gameOver(self):
		self.end = True
		
	### moves
	def moveUp(self):
		step = self.grid[self.position[0] - 1][self.position[1]].value
		self.steps.append(step)
		for i in range(1, step + 1):
			self.grid[self.position[0] - i][self.position[1]].visited = True
			self.result += self.grid[self.position[0] - i][self.position[1]].value
		self.position[0] -=	step
	def moveDown(self):
		step = self.grid[self.position[0] + 1][self.position[1]].value
		self.steps.append(step)
		for i in range(1, step + 1):
			self.grid[self.position[0] + i][self.position[1]].visited = True
			self.result += self.grid[self.position[0] + i][self.position[1]].value 
		self.position[0] += step
	def moveRight(self):
		step = self.grid[self.position[0]][self.position[1] + 1].value
		self.steps.append(step)
		for i in range(1, step + 1):
			self.grid[self.position[0]][self.position[1] + i].visited = True
			self.result += self.grid[self.position[0]][self.position[1] + i].value
		self.position[1] += step
	def moveLeft(self):
		step = self.grid[self.position[0]][self.position[1] - 1].value
		self.steps.append(step)
		for i in range(1, step + 1):
			self.grid[self.position[0]][self.position[1] - i].visited = True
			self.result += self.grid[self.position[0]][self.position[1] - i].value
		self.position[1] -= step
	
	def undoUp(self):
		step = self.steps[-1]
		self.steps = self.steps[:-1]
		for i in range(step):
			self.grid[self.position[0] + i][self.position[1]].visited = False
			self.result -= self.grid[self.position[0] + i][self.position[1]].value
		self.position[0] +=	step
		
	def undoDown(self):
		step = self.steps[-1]
		self.steps = self.steps[:-1]
		for i in range(step):
			self.grid[self.position[0] - i][self.position[1]].visited = False
			self.result -= self.grid[self.position[0] - i][self.position[1]].value 
		self.position[0] -= step
		
	def undoRight(self):
		step = self.steps[-1]
		self.steps = self.steps[:-1]
		for i in range(step):
			self.grid[self.position[0]][self.position[1] - i].visited = False
			self.result -= self.grid[self.position[0]][self.position[1] - i].value
		self.position[1] -= step
		
	def undoLeft(self):
		step = self.steps[-1]
		self.steps = self.steps[:-1]
		for i in range(step):
			self.grid[self.position[0]][self.position[1] + i].visited = False
			self.result -= self.grid[self.position[0]][self.position[1] + i].value
		self.position[1] += step
		
	def potScore(self):
		possible = self.chkMove()
		up, down, left, right = -1, -1, -1, -1
		if possible[0]: 
			step = self.grid[self.position[0] - 1][self.position[1]].value
			up = sum([self.grid[self.position[0] - i][self.position[1]].value for i in range(1,step+1)])
		if possible[1]: 
			step = self.grid[self.position[0] + 1][self.position[1]].value
			down = sum([self.grid[self.position[0] + i][self.position[1]].value for i in range(1,step+1)])
		if possible[2]:
			step = self.grid[self.position[0]][self.position[1] + 1].value
			right = sum([self.grid[self.position[0]][self.position[1] + i].value for i in range(1,step+1)])
		if possible[3]:
			step = self.grid[self.position[0]][self.position[1] - 1].value
			left = sum([self.grid[self.position[0]][self.position[1] - i].value for i in range(1,step+1)])
		
		return [up, down, right, left]
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
	def chkRight(self):
		if self.position[1] == self.width - 1:
			return False
		step = self.grid[self.position[0]][self.position[1] + 1].value
		if self.position[1] + step > self.width - 1:
			return False
		return not any([self.grid[self.position[0]][self.position[1] + i].visited for i in range(1, step + 1)])
	def chkLeft(self):
		if self.position[1] == 0:
			return False
		step = self.grid[self.position[0]][self.position[1] - 1].value
		if self.position[1] - step < 0:
			return False
		return not any([self.grid[self.position[0]][self.position[1] - i].visited for i in range(1, step + 1)])
	
	def chkMove(self):
		return [self.chkUp(), self.chkDown(), self.chkRight(), self.chkLeft()]
	def potStep(step):
		up, down, right, left = -1, -1, -1, -1
		if self.chkUp(): up = self.grid[self.position[0] - 1][self.position[1]].value
		if self.chkDown(): down = self.grid[self.position[0] + 1][self.position[1]].value
		if self.chkRight(): right = self.grid[self.position[0]][self.position[1] + 1].value
		if self.chkLeft(): left = self.grid[self.position[0]][self.position[1] - 1].value
		return [up, down, right, left]
		
	
		