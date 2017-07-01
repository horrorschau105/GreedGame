from random import randint
class Square:
	visited = 0
	value = -1
	def __init__(self, val):
		self.value = val

class Grid:
	grid = [[]]
	height = 0
	width = 0
	position = [-1,-1]
	def __init__(self, h, w):
		self.height = h
		self.width = w
		self.grid = [[Square(randint(1,5)) for i in range(w) ] for j in range(h)]
		self.position = [randint(0, w-1), randint(0, h-1)]
	def display(self):
		print (self.grid)
if __name__ == "__main__":
	g = Grid(4,4)
	g.display()
	#print (g.grid)
	#g.kupa()
	#print (g.map)