from grid import Grid
import sys
if __name__ == "__main__":
	#data = []
	with open('grids.txt', 'r') as f:
		data = f.readlines()[1:]
	grids = []
	i=0
	while(i < len(data)):
		print(data[i][:-1])
		height, width, x, y = [int(k) for k in data[i][:-1].split(' ')]
		position = [x,y]
		print (height, width, position)
		i+=1
		values = []
		for j in range(height):
			values.append([int(k) for k in data[i+j][:-1]])
		i+=height
		g = Grid(2,2)
		g.importFrom(height, width, position, values)
		grids.append(g)
	#workplan:
	#
	#import all grids
	#import all ai-methods
		#greed
		#snail
		#!greed
		#greedAfterNsteps
		#random
		#tbd
	#run methods
	#print results

