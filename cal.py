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