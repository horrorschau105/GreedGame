colors = {
	1: '\x1b[1;30;40m',
	2: '\x1b[1;31;40m',
	3: '\x1b[1;32;40m',
	4: '\x1b[1;33;40m',
	5: '\x1b[1;34;40m',
	6: '\x1b[1;35;40m',
	7: '\x1b[1;36;40m',
	8: '\x1b[1;37;40m',
	9: '\x1b[1;36;40m',
	"END" : '\x1b[0m'
}

moves = ["  Go up  " , "  Go down ", "Go right ", " Go left "]
empty = ["         " , "          ", "         ", "         "] # sorry for that
	
def color(col, txt=None):
	if txt is None: txt = col
	return colors[col]+str(txt)+ colors["END"]
	
def gameOverText():
	return color(2, "GAME OVER!")
	
def possibleMovesText(arr):
	return color(8 ,"Possible moves:\t") + "".join([color(i+2, moves[i]) if arr[i] else color(1,empty[i]) for i in range(4)])
	
	
