from ai import *
from gridImport import parseGridsFrom
from testyourai import TestYourAI
import sys
if __name__ == "__main__":
	machine = TestYourAI(parseGridsFrom('grids.txt')) 
	#methods = [[None, random], [None, first], [None, greed], [snail.preSnail, snail.snail]]
	# here put the name of function choosing move
	methods = [[None, first], [snail.preSnail, snail.snail]]
	for i in methods:
		machine.testWith(i)
		print("Finished: {}".format(i[1].__name__))
	machine.printResults()

