from ai import *
from gridImport import parseGridsFrom
from testyourai import TestYourAI
import sys
if __name__ == "__main__":
	machine = TestYourAI(parseGridsFrom('grids.txt'))
	methods = [random] # put here whatever you want
	for i in methods:
		machine.testWith(i)
		print("Finished: {}".format(i.__name__))
	machine.printResults()

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

