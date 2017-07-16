from grid import Grid
from random import randint
#here you can put any ai method with additional classes 
def random(data):
	choices = [i for i in range(len(data[0])) if data[0][i]]
	return choices[randint(0,len(choices)-1)]
def greed(data):
	best = max(data[3])
	for i in range(len(data[3])):
		if data[3][i] == best: return i
def first(data):
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
			
	def snail(data):
		up, down, right, left = data[0]
		if snail.direction == 0:
			if down: return 1
			if right: return 2
			snail.direction = 1
			return first(data)
		if snail.direction == 1:
			if right: return 2
			if up: return 0
			snail.direction = 2
			return first(data)
		if snail.direction == 2:
			if up: return 0
			if left: return 3
			snail.direction = 3
			return first(data)
		if snail.direction == 3:
			if left: return 3
			if down: return 1
			snail.direction = 0
		return first(data)
#dfsNstep
#
#
