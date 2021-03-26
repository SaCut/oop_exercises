# OOP Exercises

#### FizzBuzz class
- First we define the class
```python
class FizzBuzz():
```
- and initialise it
```python
	
	# the parameters allow the user to choose which words to use, Fizz and Buzz as default
	def __init__(self, Fizz="Fizz", Buzz="Buzz"):
		self.Fizz = Fizz
		self.Buzz = Buzz
```


- then we define the method that prints the output
```python
	def fizz_buzz(self):
		zz_string = "" # the string is empty

		for i in range(1, 100): # print 100 results

			if i % 3 == 0: # if dividing by 3 gives no remainder, the number is a multiple of 3
				zz_string += self.Fizz # add "Fizz" to the empty string

			if i % 5 == 0:# if dividing by 5 gives no remainder, the number is a multiple of 5
				zz_string += self.Buzz # add "Buzz" to the string

			if (i % 3 != 0) and (i % 5 != 0):	# if the number is not a multiple of 3 or 5, 
			 	zz_string = str(i) 				# the string becomes the current number
			
			print(zz_string) # print the result
			zz_string = "" # reset the string for the next loop
```

- finally, we create an onject from the function, then call the method
```python
if __name__=='__main__': # only execute the following code if this file is run directly
	
	fizzbuzz = FizzBuzz() 	# create object. If we wanted to use other words instead of Fizz and
							# Buzz, we would specify it here

	fizzbuzz.fizz_buzz() # call method
```

#### Scrabble calculator
- We define the class
```python
class ScrabbleCalc():
```
- in the init method, we create a dictionary of points and letters
```python
	def __init__(self):
		self.groups = {
			1: ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
			2: ["D", "G"],
			3: ["B", "C", "M", "P"],
			4: ["F", "H", "V", "W", "Y"],
			5: ["K"],
			8: ["J", "X"]
			}
```

- we define a method for calculating the result
```python
	def result(self, word=""): # taking use input

		total = 0 # starting with zero points

		for letter in word: # we check each letter
			for points, group in self.groups.items(): # we iterate over the dictionary
				if letter.upper() in group: 	# if the (upper-case) letter is found in the group
					total += points				# we add its worth to the total
```
- then we return the total score
```python
		return total # then we return the total
```
- finally, we create an object for the class and execute the method, passing a string to be checked
```python
if __name__=='__main__':
	calculator = ScrabbleCalc() # we assign the class to an object
	print(calculator.result("this_should_be_worth_32")) # then we check it the method works
```