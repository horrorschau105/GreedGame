from ai import *
from gridImport import parseGridsFrom
from testyourai import TestYourAI
import sys
if __name__ == "__main__":
	machine = TestYourAI(parseGridsFrom('grids.txt')) 
	#methods = [[None, greed], [None, gr1stp], [snail2.preSnail2, snail2.snail2], [None, random], [None, first],  [snail.preSnail, snail.snail]]
	# here put the name of function choosing move
	#methods = [[None, gr1stp], [snail2.preSnail2, snail2.snail2]]
	methods = [[None, greed], [None, gr1stp],  [deepgreed.preGreed, deepgreed.deepgrd]]
	for i in methods:
		machine.testWith(i)
		print("Finished: {}".format(i[1].__name__))
	machine.printResults()

