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
#dfsNstep
#
#
