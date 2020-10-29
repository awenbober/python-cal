import math

class Calculator:
	def add(self, firstNum, secondNum):
		return firstNum + secondNum
	def subtract(self, firstNum, secondNum):
		return firstNum - secondNum
	def divide(self, firstNum, secondNum):
		return firstNum / secondNum
	def multiplication(self, firstNum, secondNum):
		return firstNum * secondNum
	def power(self, firstNum, secondNum):
		return pow(firstNum, secondNum)
	def squareRoot(self,mul):
		return math.sqrt(mul)
	def logarithm1(self,firstNum):
	    return math.log(firstNum)
	def logarithm2(self,firstNum,secondNum):
		return math.log(firstNum,secondNum)

a = int(input("enter first number: "))
b = int(input("enter second number: "))

myCalculator = Calculator()
sum = myCalculator.add(a,b)
print("Result of addition: ",sum)

sub = myCalculator.subtract(a,b)
print("Result of subtraction: ",sub)

div = myCalculator.divide(a,b)
print("Result of division: ",div)

mul = myCalculator.multiplication(a,b)
print("Result of multiplication: ",mul)

power = myCalculator.power(a,b)
print("Result of power: ",power)

squareRoot=myCalculator.squareRoot(mul)
print("Result of squareRoot",squareRoot)

#Printing the log base e of input number
logarithm1=myCalculator.logarithm1(a)
print("Result of logarithm",logarithm1)

logarithm2=myCalculator.logarithm2(a,b)
print("Result of logarithm",logarithm2)