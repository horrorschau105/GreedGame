from random import randint
from colors import printc
from getch import getch
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
		self.grid = [[Square(randint(1,9)) for j in range(w) ] for i in range(h)]
		self.max = sum([sum([self.grid[i][j].value for j in range(w)]) for i in range(h)])
		self.position = [randint(0, h-1), randint(0, w-1)]
		self.result = self.grid[self.position[0]][self.position[1]].value
	def display(self):
		for i in range(self.height): # gonna be shorter
			for j in range(self.width):
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
		button = ord(getch())
		if button in [3, 24, 26, 113]: break # q, ^Z, ^X, ^C
		if button == 27: 
			button = ord(getch())
			if button == 91:
				button = ord(getch())
				if button == 65: 
					print("UP")
				if button == 66: 
					print("DW")
				if button == 67: 
					print("RT")	
				if button == 68: 
					print("LT")
				
