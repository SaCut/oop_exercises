# Base Scrabble word calculator instructions
# Given the below scoring create a Scrabble word calculator that will
# provide the correct scores dependent on the string provided.

# Letter Value
# A, E, I, O, U, L, N, R, S, T 1
# D, G 2
# B, C, M, P 3
# F, H, V, W, Y 4
# K 5
# J, X 8

class ScrabbleCalc():

	def __init__(self, word=""):
		self.word = word
		self.groups = {
			1: ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
			2: ["D", "G"],
			3: ["B", "C", "M", "P"],
			4: ["F", "H", "V", "W", "Y"],
			5: ["K"],
			8: ["J", "X"]
			}

	def result(self, word)
