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