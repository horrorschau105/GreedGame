from termios import tcgetattr, tcsetattr, TCSADRAIN
from tty import setraw
import sys
class Getch:
	def __call__(self):
		fd = sys.stdin.fileno()
		old_settings = tcgetattr(fd)
		try:
			setraw(sys.stdin.fileno())
			ch = sys.stdin.read(1)
		finally:
			tcsetattr(fd, TCSADRAIN, old_settings)
		return ch

getch = Getch()
