from grid import Grid
from random import randint
from copy import deepcopy
#here you can put any ai method with additional classes 
def random(grid):
	data = [[], []]
	data[0] = grid.chkMove() #temporal patch
	choices = [i for i in range(len(data[0])) if data[0][i]]
	return choices[randint(0,len(choices)-1)]
def greed(grid):
	data = [[], [], [], []]
	data[3] = grid.potScore()
	best = max(data[3])
	for i in range(len(data[3])):
		if data[3][i] == best: return i
def first(grid):
	data = [[], []]
	data[0] = grid.chkMove()
	choices = [i for i in range(len(data[0])) if data[0][i]]
	return choices[0]

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
#dfsNstep
#
#
