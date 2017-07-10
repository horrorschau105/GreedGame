from grid import Grid
from random import randint
def random(data):
	choices = [i for i in range(len(data[0])) if data[0][i]]
	return choices[randint(0,len(choices)-1)]
def last(data):
	choices = [i for i in range(len(data[0])) if data[0][i]]
	return choices[-1]
def first(data):
	choices = [i for i in range(len(data[0])) if data[0][i]]
	return choices[0]
#greed
#dfsNstep
#
#
