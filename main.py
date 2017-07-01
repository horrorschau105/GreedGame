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
	def __init__(self, h, w):
		self.height = h
		self.width = w
		self.grid = [[Square(randint(1,5)) for i in range(w) ] for j in range(h)]
		self.max = sum([sum([self.grid[i][j].value for i in range(w)]) for j in range(h)])
		self.position = [randint(0, w-1), randint(0, h-1)]
		#self.grid[self.position[0]][self.position[1]].visited = True
		self.result = self.grid[self.position[0]][self.position[1]].value
	def display(self):
		for i in range(self.width): # gonna be shorter
			for j in range(self.height):
				if self.grid[i][j].visited: print(' ', end="")
				elif [i,j] == self.position: print('@', end="")
				else: print (self.grid[i][j].value, end="")
			print ('\n', end="")
		print()
		print(self.result, " / " , self.max)
if __name__ == "__main__":
	
	g = Grid(4,4)
	g.display()
	#print (g.grid)
	#g.kupa()
	#print (g.map)