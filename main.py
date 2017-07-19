from ai import *
from gridImport import parseGridsFrom
from testyourai import TestYourAI
import time
import sys
if __name__ == "__main__":
	machine = TestYourAI(parseGridsFrom('grids.txt')) 
	#methods = [[None, greed], [None, gr1stp], [snail2.preSnail2, snail2.snail2], [None, random], [None, first],  [snail.preSnail, snail.snail]]
	# here put the name of function choosing move
	methods = [[None, first], [snail2.preSnail2, snail2.snail2], [deepgreed.preGreed, deepgreed.deepgrd]]
	#methods = [[None, greed], [None, gr1stp]]
	start, end = 0,0
	for i in methods:
		start = time.time()
		machine.testWith(i)
		end = time.time()
		print("Finished: {} \t Used time: {:05.3f}".format(i[1].__name__, end - start))
	machine.printResults()

