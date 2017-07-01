from random import randint
from colors import printc
import sys
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
		self.grid = [[Square(randint(1,5)) for j in range(w) ] for i in range(h)]
		self.max = sum([sum([self.grid[i][j].value for j in range(w)]) for i in range(h)])
		self.position = [randint(0, h-1), randint(0, w-1)]
		self.result = self.grid[self.position[0]][self.position[1]].value
	def display(self):
		for i in range(self.height): # gonna be shorter
			for j in range(self.width):
				printc(self.grid[i][j].value)
				if self.grid[i][j].visited: print(' ', end="")
				elif [i,j] == self.position: print('@', end="")
				else: printc(self.grid[i][j].value)
			print ('\n', end="")
		print()
		print(self.result, " / " , self.max, "\t", self.position)
if __name__ == "__main__":
	g = Grid(20,80)
	g.display()
	while(True):
		#button = sys.stdin.read(1)
		#if(button == 'q'): break
		
