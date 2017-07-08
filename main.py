from grid import Grid
import sys
if __name__ == "__main__":
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
	if(len(sys.argv) != 5):
		print("Usage: python3 main.py (count of grids) (width) (height) (max value in simgle cell) > (output file)")
		sys.exit()
	count, width, height, maxvalue = [int(i) for i in sys.argv[1:]]
	for i in range(count):
		g = Grid(height, width, maxvalue)
		g.show()

