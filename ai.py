from grid import Grid
from examples import first
#here you can put any ai method with additional classes 
class snailbfs: # snail at the beginning, bfs ends
	moves = []
	def pre(grid):
		snailbfs.moves = []
		boostedsnail.setDirection(grid)
		wiseBFS.setN(grid)
		while(any(grid.chkMove())):
			m = boostedsnail.Bsnail(grid)
			snailbfs.moves.append(m)
			[grid.moveUp, grid.moveDown, grid.moveRight, grid.moveLeft][m]()
		for i in snailbfs.moves[::-1]:
			[grid.undoUp, grid.undoDown, grid.undoRight, grid.undoLeft][i]()
		snailbfs.moves = snailbfs.moves[:-5] # arbitrary
	def Gsnail(grid):
		if len(snailbfs.moves) > 0:
			move, snailbfs.moves = snailbfs.moves[0], snailbfs.moves[1:]
			return move
		return wiseBFS.moveN(grid)
			
class combo:
#        <-2
#      3 XX ^
#      v XX 1
#        0->
	direction, mostup, mostdown, mostright, mostleft = 0,0,0,0,0
	def setDirection(grid):
		combo.mostup, combo.mostdown, combo.mostright, combo.mostleft = -1, grid.height+1, grid.width+1, -1
		if grid.position[0] > grid.height/2 and grid.position[1] > grid.width/2:
			combo.direction = 0
		if grid.position[0] < grid.height/2 and grid.position[1] < grid.width/2:
			combo.direction = 2
		if grid.position[0] < grid.height/2 and grid.position[1] > grid.width/2:
			combo.direction = 1
		if grid.position[0] > grid.height/2 and grid.position[1] < grid.width/2:
			combo.direction = 3
		wiseBFS.setN(grid)
	def combo(grid):
		if grid.score() > 20:
			return wiseBFS.moveN(grid)
		up, down, right, left = grid.chkMove()
		if combo.direction == 0:
			if grid.position[0] > combo.mostdown and up: return 0 
			if down: return 1
			if right: return 2
			combo.direction = 1
			combo.mostdown = grid.position[0]
		elif combo.direction == 1:
			if grid.position[1] > combo.mostright and left: return 3
			if right: return 2
			if up: return 0
			combo.direction = 2
			combo.mostright = grid.position[1]
		elif combo.direction == 2:
			if grid.position[0] < combo.mostup and down: return 1
			if up: return 0
			if left: return 3
			combo.direction = 3
			combo.mostup = grid.position[0]
		elif combo.direction == 3:
			if grid.position[1] < combo.mostleft and right: return 2
			if left: return 3
			if down: return 1
			combo.direction = 0
			combo.mostleft = grid.position[0]
		return first(grid)
class wiseBFS: # same as deepgreed, but with deep manipulation
	deep = 1
	steps = []
	def setN(grid):
		wiseBFS.deep = 10
	def moveN(grid):
		if len(wiseBFS.steps) == 0:
			wiseBFS.steps = wiseBFS.bfsPath(grid, wiseBFS.deep)[0]
		move = wiseBFS.steps[0]
		wiseBFS.steps = wiseBFS.steps[1:] 
		if grid.score() > 20:
			wiseBFS.deep = 15
		return move
	def bfsPath(grid, deep):
		if deep == 0:
			return [[], grid.result]
		else:
			up, down, right, left = [[[],-1000],[[],-1000],[[],-1000],[[],-1000]]
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
			return [[mv, res + grid.result] for mv, res in [up, down, right, left] if 	res == max([tup[1] for tup in [up, down, right	, left]])][0]
class boostedsnail:
#        <-2
#      3 XX ^
#      v XX 1
#        0->
	direction, mostup, mostdown, mostright, mostleft = 0,0,0,0,0
	def setDirection(grid):
		boostedsnail.mostup, boostedsnail.mostdown, boostedsnail.mostright, boostedsnail.mostleft = -1, grid.height+1, grid.width+1, -1
		distup, distdown, distright, distleft = grid.position[0], grid.height - grid.position[0], grid.width - grid.position[1], grid.position[1]
		distances = [distup, distdown, distright, distleft]
		if distup == min(distances):
			boostedsnail.direction = 2
		if distdown == min(distances):
			boostedsnail.direction = 0
		if distright == min(distances):
			boostedsnail.direction = 1
		if distleft == min(distances):
			boostedsnail.direction = 3
		#wiseBFS.setN(grid)
	def Bsnail(grid):
		#if grid.score() > 10:
		#	return wiseBFS.moveN(grid)
		up, down, right, left = grid.chkMove()
		if boostedsnail.direction == 0:
			if grid.position[0] > boostedsnail.mostdown and up: return 0 
			if right: return 2
			boostedsnail.direction = 1
			boostedsnail.mostdown = grid.position[0]
			if up: return 0
		elif boostedsnail.direction == 1:
			if grid.position[1] > boostedsnail.mostright and left: return 3
			if up: return 0
			boostedsnail.direction = 2
			boostedsnail.mostright = grid.position[1]
			if left: return 3
		elif boostedsnail.direction == 2:
			if grid.position[0] < boostedsnail.mostup and down: return 1
			if left: return 3
			boostedsnail.direction = 3
			boostedsnail.mostup = grid.position[0]
			if down: return 1
		elif boostedsnail.direction == 3:
			if grid.position[1] < boostedsnail.mostleft and right: return 2
			if down: return 1
			boostedsnail.direction = 0
			boostedsnail.mostleft = grid.position[0]
			if right: 2
		return first(grid)