from ai import *
from gridImport import parseGridsFrom
from testyourai import TestYourAI
import sys
if __name__ == "__main__":
	machine = TestYourAI(parseGridsFrom('grids.txt')) 
	methods = [random, first, greed] # here put the name of function choosing move
	for i in methods:
		machine.testWith(i)
		print("Finished: {}".format(i.__name__))
	machine.printResults()

