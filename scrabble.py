# Base Scrabble word calculator
class ScrabbleCalc():

	def __init__(self):

		# we create a dictionary of points and letters
		self.groups = {
			1: ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
			2: ["D", "G"],
			3: ["B", "C", "M", "P"],
			4: ["F", "H", "V", "W", "Y"],
			5: ["K"],
			8: ["J", "X"]
			}

	# we define a method for calculating the result
	def result(self, word=""): # taking use input

		total = 0 # starting with zero points

		for letter in word: # we check each letter
			for points, group in self.groups.items(): # we iterate over the dictionary
				if letter.upper() in group: 	# if the (upper-case) letter is found in the group
					total += points				# we add its worth to the total

		return total # then we return the total

if __name__=='__main__':
	calculator = ScrabbleCalc() # we assign the class to an object
	print(calculator.result("this_should_be_worth_32")) # then we check it the method works