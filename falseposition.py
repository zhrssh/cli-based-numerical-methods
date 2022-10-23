import cmath
import math

class FalsePosition:
	def __init__(self, fox, a, b, DOF):
		
		# Conditions
		if a > b:
			print("A must be less than B")
			return
		
		if self.Evaluate(fox, a) * self.Evaluate(fox, b) > 0:
			print("f(a) and f(b) must be opposite signs")
			return
		
		self.Compute(fox, a, b, DOF)
	
	def Compute(self, fox, a, b, DOF):
		 
		# While f(x) > DOF
		c = 1
		
		iteration = 0
		while abs(self.Evaluate(fox, c)) > DOF:
				
			# update iteration
			iteration = iteration + 1
				
			
			# x1 = (af(b) - bf(a)) / f(b) - f(a)
			c = ((a * self.Evaluate(fox, b)) - (b * self.Evaluate(fox, a))) / (self.Evaluate(fox, b) - self.Evaluate(fox, a))
			
			# check conditions
			if self.Evaluate(fox,c) != 0 and self.Evaluate(fox, c) < 0:
				a = c
				
			# print values
			print(f"c is {c:.12f} at iteration no. {iteration}")
			print(f"foc = {self.Evaluate(fox, c):.12f}")
			
		print(f"Root is: {c:.12f}")
		print(f"Number of iterations: {iteration}")
		
	
	def Evaluate(self, formula, value):
		formula = formula.replace("x", f"{value}")
		formula = eval(formula)
		return formula

def e(x):
	return math.exp(x)

def main():
	# Start of program
	print("False Position Method Calculator\n")

	formula = input("Input formula (for e, use e(x)): ")
	a = float(input("Input a: "))
	b = float(input("Input b: "))
	DOF = float(input("Input DOF: "))
	
	myProgram = FalsePosition(formula, a, b, DOF)

if __name__ == "__main__":
	main()
