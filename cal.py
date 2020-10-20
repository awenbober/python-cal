class Calculator:
	def add(self, firstNum, secondNum):
		return firstNum + secondNum
	

a = int(input("enter first number: "))
b = int(input("enter second number: "))

myCalculator = Calculator()
sum = myCalculator.add(a,b)
print("Sum is: ",sum)