from os import system

class Score:
	scores = []
	def __init__(self):
		try:
			with open('highscores.xd', 'r') as f:
				self.scores = [[int(j[0]), int(j[1])] for j in [i.split(' ') for i in f.read().split('\n')[:-1:1]]]
		except Exception:
			self.scores = []
			print("Cannot load highscores")
	def update(self, result, ofall):
		self.scores.append([result, ofall])
		self.scores.sort(key = lambda x: x[1]/x[0])
		system('clear')
		print("No.\tResult\tMax\tPercentage")
		with open('highscores.xd', 'w') as f:
			for i in range(min(len(self.scores), 10)):
				print("{}\t{}\t{}\t{:04.2f}%\t{}".format(i+1, self.scores[i][0], self.scores[i][1], self.scores[i][0] * 100/ self.scores[i][1], "NEW!" if self.scores[i] == [result, ofall] else ""))
				f.write("{} {}\n".format(self.scores[i][0], self.scores[i][1]))  
