from ai import boostedsnail, snailbfs
from examples import random, greed, snail, first,greedNstep
from gridImport import parseGridsFrom
from testyourai import TestYourAI
import sys
if __name__ == "__main__":
	machine = TestYourAI(parseGridsFrom('grids.txt')) 
	methods = [[None, first], [None, greed], [None, random], [snail.preSnail, snail.snail],[boostedsnail.setDirection, boostedsnail.Bsnail], [greedNstep.setN, greedNstep.greedN],[snailbfs.pre, snailbfs.Gsnail]]
	for i in methods:
		timeSpent = machine.testWith(i)
		print("Finished: {} \t Used time: {:05.3f}".format(i[1].__name__, timeSpent))
	machine.printResults()

