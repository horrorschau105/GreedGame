# some simple implemented tactics
from grid import Grid
from random import randint
def random(grid):
	data = [[]]
	data[0] = grid.chkMove() #temporal patch
	choices = [i for i, val in enumerate(data[0]) if val]
	return choices[randint(0,len(choices)-1)]
def greed(grid):
	data = [[], [], [], []]
	data[3] = grid.potScore()
	best = max(data[3])
	return [i for i, val in enumerate(data[3]) if val == best][0]
def first(grid):
	data = [[], []]
	data[0] = grid.chkMove()
	return [i for i,val in enumerate(data[0]) if val][0]
class snail:
# classic snail 
#         <- 2
#      3 XXXXXX ^
#      I XXXXXX I
#      v XXXXXX 1
#         -> 0
	direction = 0
	def preSnail(grid):
		if grid.position[0] > grid.height/2 and grid.position[1] > grid.width/2:
			snail.direction = 0
		if grid.position[0] < grid.height/2 and grid.position[1] < grid.width/2:
			snail.direction = 2
		if grid.position[0] < grid.height/2 and grid.position[1] > grid.width/2:
			snail.direction = 1
		if grid.position[0] > grid.height/2 and grid.position[1] < grid.width/2:
			snail.direction = 3
	def snail(grid):
		up, down, right, left = grid.chkMove()
		if snail.direction == 0:
			if down: return 1
			if right: return 2
			snail.direction = 1
		elif snail.direction == 1:
			if right: return 2
			if up: return 0
			snail.direction = 2
		elif snail.direction == 2:
			if up: return 0
			if left: return 3
			snail.direction = 3
		elif snail.direction == 3:
			if left: return 3
			if down: return 1
			snail.direction = 0
		return greed(grid)
class greedNstep: # go N step forward, take best way
	deep = 1
	steps = []
	def setN(grid):
		greedNstep.deep = 3 # arbitrary
	def greedN(grid):
		if len(greedNstep.steps) == 0:
			greedNstep.steps = greedNstep.search(grid, greedNstep.deep)[0]
		move = greedNstep.steps[0]
		greedNstep.steps = greedNstep.steps[1:] 
		return move
	def search(grid, deep):
		if deep == 0:
			return [[], grid.result]
		else:
			up, down, right, left = [[[],0],[[],0],[[],0],[[],0]]
			if grid.chkUp():
				grid.moveUp()
				up = greedNstep.search(grid, deep - 1)
				up[0]    = [0] + up[0]
				grid.undoUp()
			if grid.chkDown():
				grid.moveDown()
				down = greedNstep.search(grid, deep - 1)
				down[0]  = [1] + down[0]
				grid.undoDown()
			if grid.chkRight():
				grid.moveRight()
				right = greedNstep.search(grid, deep - 1)
				right[0] = [2] + right[0]
				grid.undoRight()
			if grid.chkLeft():
				grid.moveLeft()
				left = greedNstep.search(grid, deep - 1)
				left[0]  = [3] + left[0]
				grid.undoLeft()
			return [[mv, res + grid.result] for mv, res in [up, down, right, left] if 	res == max([tup[1] for tup in [up, down, right, left]])][0]
			# just take best move from four above and remember the way