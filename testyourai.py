import math
class TestYourAI:
	grids = []
	results = []
	def __init__(self, grids):
		self.grids = grids
		print("Imported!")
	def addToSummary(self, name, arr):
		fails = len([i for i in arr if i==-1])
		avg = sum([i  for i in arr if i>0]) / (len(arr)-fails)
		varr = sum([(i-avg)*(i-avg)  for i in arr if i>0]) / (len(arr)-fails)
		sd = math.sqrt(varr)
		minimum = min([i  for i in arr if i>0])
		maximum = max(arr)
		self.results.append([name, avg, minimum, maximum, sd, fails])
	def testWith(self, method):
		results = []
		for iter_grid in self.grids:
			grid = iter_grid
			while(True):
				possible = grid.chkMove()
				idx = method(grid.data())
				if(not possible[idx]): #illegal move or just gameover
					if(any(possible)): results.append(-1)
					break
				grid.move(idx)
			results.append(grid.result*100 / grid.max )
		self.addToSummary(method.__name__, results)
	def printResults(self):
		print("Name\tAvg(%)\tMin(%)\tMax(%)\tStDev\tFail")
		for line in self.results:
			print ("{}\t{:04.2f}\t{:04.2f}\t{:04.2f}\t{:04.2f}\t{}".format(line[0], line[1], line[2], line[3], line[4], line[5]))
		
	
