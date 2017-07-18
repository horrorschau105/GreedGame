from grid import Grid
from random import randint
from copy import deepcopy
#here you can put any ai method with additional classes 
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
		
class snail2:
#         <- 2
#      3 XXXXXX ^
#      I XXXXXX I
#      v XXXXXX 1
#         -> 0
	direction, mostup, mostdown, mostright, mostleft = 0,0,0,0,0
	def preSnail2(grid):
		snail2.mostup, snail2.mostdown, snail2.mostright, snail2.mostleft = -1, grid.height+1, grid.width+1, -1
		if grid.position[0] > grid.height/2 and grid.position[1] > grid.width/2:
			snail2.direction = 0
		if grid.position[0] < grid.height/2 and grid.position[1] < grid.width/2:
			snail2.direction = 2
		if grid.position[0] < grid.height/2 and grid.position[1] > grid.width/2:
			snail2.direction = 1
		if grid.position[0] > grid.height/2 and grid.position[1] < grid.width/2:
			snail2.direction = 3
			
	def snail2(grid):
		up, down, right, left = grid.chkMove()
		if snail2.direction == 0:
			if grid.position[0] > snail2.mostdown and up: return 0 
			if down: return 1
			if right: return 2
			snail2.direction = 1
			snail2.mostdown = grid.position[0]
		elif snail2.direction == 1:
			if grid.position[1] > snail2.mostright and left: return 3
			if right: return 2
			if up: return 0
			snail2.direction = 2
			snail2.mostright = grid.position[1]
		elif snail2.direction == 2:
			if grid.position[0] < snail2.mostup and down: return 1
			if up: return 0
			if left: return 3
			snail2.direction = 3
			snail2.mostup = grid.position[0]
		elif snail2.direction == 3:
			if grid.position[1] < snail2.mostleft and right: return 2
			if left: return 3
			if down: return 1
			snail2.direction = 0
			snail2.mostleft = grid.position[0]
		return greed(grid)

def gr1stp(grid):
	up, down, right, left = grid.chkMove()
	potScore = [-1, -1, -1, -1]
	if up:
		grid.moveUp()
		potScore[0] = grid.result
		grid.undoUp()
	if down: 
		grid.moveDown()
		potScore[1] = grid.result
		grid.undoDown()
	if right:
		grid.moveRight()
		potScore[2] = grid.result
		grid.undoRight()
	if left:
		grid.moveLeft()
		potScore[3] = grid.result
		grid.undoLeft()
	for i, val in enumerate(potScore):
		if potScore[i]>0:
			potScore[i] -= grid.result
	best = max(potScore)
	return [i for i, val in enumerate(potScore) if val == best][0]
		
class deepgreed:
	deep = 1
	steps = []
	def preGreed(grid):
		deepgreed.deep = 4
	def deepgrd(grid):
		if len(deepgreed.steps) == 0:
			deepgreed.steps = deepgreed.bfsPath(grid, deepgreed.deep)
		move =  deepgreed.steps[0]
		deepgreed.steps = deepgreed.steps[1:] 
	def bfsPath(grid, deep):
		
		"""up, down, right, left = -1,-1,-1,-1
		bestmove = {}
		if deep == 1: # classic greed
			if grid.chkUp():
				grid.moveUp()
				up = grid.result
				grid.undoUp()
			if grid.chkDown():
				grid.moveDown()
				down = grid.result
				grid.undoDown()
			if grid.chkRight():
				grid.moveRight()
				right = grid.result
				grid.undoRight()
			if grid.chkLeft():
				grid.moveLeft()
				left = grid.result
				grid.undoLeft()
			mv = [up, down, right, left]
			best = max(mv)
			for i, val in enumerate(mv):
				if val == best:
					return {best+grid.result: [i]}
		if deep > 1:  
			if grid.chkUp():
				grid.moveUp()
				up = bfsPath(grid, deep - 1)
				grid.undoUp()
			if grid.chkDown():
				grid.moveDown()
				down = bfsPath(grid, deep - 1)
				grid.undoDown()
			if grid.chkRight():
				grid.moveRight()
				right = bfsPath(grid, deep - 1)
				grid.undoRight()
			if grid.chkLeft():
				grid.moveLeft()
				left = bfsPath(grid, deep - 1)
				grid.undoLeft()
			bestmove = {0: up, 1: down, 2: right, 3: left}
		"""
		
