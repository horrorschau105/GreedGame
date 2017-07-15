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
	def __init__(self, h, w, val=9):
		self.height = h
		self.width = w
		self.grid = [[Square(randint(1,val)) for j in range(w) ] for i in range(h)]
		self.max = sum([sum([self.grid[i][j].value for j in range(w)]) for i in range(h)])
		self.position = [randint(0, h-1), randint(0, w-1)]
		self.result = self.grid[self.position[0]][self.position[1]].value
		self.grid[self.position[0]][self.position[1]].visited = True
	### display
	def show(self):
		print (self.height, self.width, self.position[0], self.position[1])
		for i in range(self.height):
			for j in range(self.width):
				print(self.grid[i][j].value, end="")
			print()