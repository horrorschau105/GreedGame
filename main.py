from getch import getch
from grid import Grid
from score import Score
if __name__ == "__main__":
	sc = Score()
	g = Grid(20,80)
	g.display()
	while(True):
		chkmove = [g.chkUp(), g.chkDown(), g.chkRight(), g.chkLeft()]
		if not any(chkmove): 
			g.gameOver()
			sc.update(g.result, g.max)
			print("Press any key...")
			getch()
			break
		button = ord(getch())
		if button in [3, 24, 26, 113]: break # q, ^Z, ^X, ^C
		if button == 27: 
			button = ord(getch())
			if button == 91:
				button = ord(getch())-65
				g.invalid = not chkmove[button] #flag for info about moves
				if chkmove[button]: 
					g.move(button)
		g.display()

