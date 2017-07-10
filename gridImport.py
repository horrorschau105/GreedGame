from grid import Grid
def parseGridsFrom(path):
	with open(path, 'r') as f:
		data = f.readlines()[1:]
	grids = []
	i=0
	while(i < len(data)):
		height, width, x, y = [int(k) for k in data[i][:-1].split(' ')]
		position = [x,y]
		i+=1
		values = []
		for j in range(height):
			values.append([int(k) for k in data[i+j][:-1]])
		i+=height
		g = Grid(2,2)
		g.importFrom(height, width, position, values)
		grids.append(g)
	return grids
