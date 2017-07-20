from grid import Grid
from examples import first
#here you can put any ai method with additional classes 
class goodsnail:
#         <- 2
#      3 XXXXXX ^
#      I XXXXXX I
#      v XXXXXX 1
#         -> 0
	direction, mostup, mostdown, mostright, mostleft = 0,0,0,0,0
	def setDirection(grid):
		goodsnail.mostup, goodsnail.mostdown, goodsnail.mostright, goodsnail.mostleft = -1, grid.height+1, grid.width+1, -1
		if grid.position[0] > grid.height/2 and grid.position[1] > grid.width/2:
			goodsnail.direction = 0
		if grid.position[0] < grid.height/2 and grid.position[1] < grid.width/2:
			goodsnail.direction = 2
		if grid.position[0] < grid.height/2 and grid.position[1] > grid.width/2:
			goodsnail.direction = 1
		if grid.position[0] > grid.height/2 and grid.position[1] < grid.width/2:
			goodsnail.direction = 3
	def snail2(grid):
		up, down, right, left = grid.chkMove()
		if goodsnail.direction == 0:
			if grid.position[0] > goodsnail.mostdown and up: return 0 
			if down: return 1
			if right: return 2
			goodsnail.direction = 1
			goodsnail.mostdown = grid.position[0]
		elif goodsnail.direction == 1:
			if grid.position[1] > goodsnail.mostright and left: return 3
			if right: return 2
			if up: return 0
			goodsnail.direction = 2
			goodsnail.mostright = grid.position[1]
		elif goodsnail.direction == 2:
			if grid.position[0] < goodsnail.mostup and down: return 1
			if up: return 0
			if left: return 3
			goodsnail.direction = 3
			goodsnail.mostup = grid.position[0]
		elif goodsnail.direction == 3:
			if grid.position[1] < goodsnail.mostleft and right: return 2
			if left: return 3
			if down: return 1
			goodsnail.direction = 0
			goodsnail.mostleft = grid.position[0]
		return first(grid)
class wiseBFS: # same as deepgreed, but with deep manipulation
	deep = 1
	steps = []
	def setN(grid):
		wiseBFS.deep = 3
	def moveN(grid):
		if len(wiseBFS.steps) == 0:
			wiseBFS.steps = wiseBFS.bfsPath(grid, wiseBFS.deep)[0]
		move = wiseBFS.steps[0]
		wiseBFS.steps = wiseBFS.steps[1:] 
		score = grid.score()
		if score > 20:
			wiseBFS.deep = 9
		elif score > 17:
			wiseBFS.deep = 7
		elif score > 12:
			wiseBFS.deep = 5
		elif score > 5:
			wiseBFS.deep = 4
		return move
	def bfsPath(grid, deep):
		if deep == 0:
			return [[], grid.result]
		else:
			up, down, right, left = [[[],0],[[],0],[[],0],[[],0]]
			if grid.chkUp():
				grid.moveUp()
				up = wiseBFS.bfsPath(grid, deep - 1)
				up[0]    = [0] + up[0]
				grid.undoUp()
			if grid.chkDown():
				grid.moveDown()
				down = wiseBFS.bfsPath(grid, deep - 1)
				down[0]  = [1] + down[0]
				grid.undoDown()
			if grid.chkRight():
				grid.moveRight()
				right = wiseBFS.bfsPath(grid, deep - 1)
				right[0] = [2] + right[0]
				grid.undoRight()
			if grid.chkLeft():
				grid.moveLeft()
				left = wiseBFS.bfsPath(grid, deep - 1)
				left[0]  = [3] + left[0]
				grid.undoLeft()
			#print ([up, down, right, left], grid.position)
			return [[mv, res + grid.result] for mv, res in [up, down, right, left] if 	res == max([tup[1] for tup in [up, down, right	, left]])][0]