# FizzBuzz
class FizzBuzz():

	# allow the user to choose which words to use, Fizz and Buzz as default
	def __init__(self, Fizz="Fizz", Buzz="Buzz"):
		self.Fizz = Fizz
		self.Buzz = Buzz

	# define the method that prints the output
	def fizz_buzz(self):
		zz_string = "" # the string has to be empty at the beginning

		for i in range(1, 100): # print the first 100 results

			if i % 3 == 0: # if dividing by 5 gives no remainder, the number is a multiple of 3
				zz_string += self.Fizz # adding "Fizz to the empty string"

			if i % 5 == 0:# if dividing by 5 gives no remainder, the number is a multiple of 5
				zz_string += self.Buzz # adding Buzz to the string

			if (i % 3 != 0) and (i % 5 != 0): #if the number is not a multiple of 3 and 5
			 	zz_string = str(i) # the string becomes the current number
			
			print(zz_string) # print the result
			zz_string = "" # reset the string for the next loop

if __name__=='__main__': # only execute the following code if this file is run directly
	fizzbuzz = FizzBuzz() # creating a FizzBuzz object
	fizzbuzz.fizz_buzz() # running the method