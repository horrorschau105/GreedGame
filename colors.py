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

def printc(col):
	print(colors[col]+str(col)+ colors["END"], end="")
	
