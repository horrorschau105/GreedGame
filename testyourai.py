import math
from copy import deepcopy
class TestYourAI:
	grids = []
	results = []
	def __init__(self, grids):
		self.grids = grids
		print("Grids imported!")
	def addToSummary(self, name, array):
		arr = [i[0] for i in array]
		fails = len([i for i in arr if i==-1])
		avg_steps = sum([i[1] for i in array if i[0] > 0]) / (len(arr)-fails)
		avg = sum([i for i in arr if i>0]) / (len(arr)-fails)
		varr = sum([(i-avg)*(i-avg) for i in arr if i>0]) / (len(arr)-fails)
		sd = math.sqrt(varr)
		minimum = min([i  for i in arr if i>0])
		maximum = max(arr)
		self.results.append([name, avg, minimum, maximum, sd, fails, avg_steps])
	def testWith(self, method):
		results = []
		grids = deepcopy(self.grids)
		for grid in grids:
			steps = 0
			while(True):
				steps +=1
				possible = grid.chkMove()
				if(not any(possible)): #gameover
					break
				idx = method(grid.data())
				if(not possible[idx]): #illegal move 
					results.append([-1, -1]) #mark it
					break
				grid.move(idx)
			results.append([grid.result*100 / grid.max, steps])
		self.addToSummary(method.__name__, results)
	def printResults(self):
		print("Name\tAvg(%)\tMin(%)\tMax(%)\tStDev\tFail\tAvgSteps")
		#print(self.results)
		for line in self.results:
			print ("{}\t{:05.3f}\t{:05.3f}\t{:05.3f}\t{:05.3f}\t{}\t{:05.3f}".format(line[0], line[1], line[2], line[3], line[4], line[5], line[6]))
		
	
