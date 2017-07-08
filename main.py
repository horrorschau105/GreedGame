from grid import Grid
import sys
if __name__ == "__main__":
	if(len(sys.argv) != 5):
		print("Usage: python3 main.py (count of grids) (width) (height) (max value in simgle cell) > (output file)")
		sys.exit()
	print(count)
	count, width, height, maxvalue = [int(i) for i in sys.argv[1:]]
	for i in range(count):
		g = Grid(height, width, maxvalue)
		g.show()

