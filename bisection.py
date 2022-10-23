class Bisection:	
	def __init__(self, fox, a, b, DOF):
		
		# Conditions
		if a > b:
			print("a must be less than b")
			return
		
		if self.Evaluate(fox, a) * self.Evaluate(fox, b) > 0:
			print("f(a) * f(b) must be less than 0")
			return
		
		self.Compute(fox, a, b, DOF)
	def Compute(self, fox, a, b, DOF):
		print(f"Computing for Bisection of: {fox}")
		
		# test is fox = 2x^3 - 2x - 5 -> (2 * (x ** 3)) - (2 * x) - 5)
		# fox = "((2 * (x ** 3)) - (2 * x) - 5)"
		
		error = DOF
		c = (a + b) / 2.0
		iteration = 0
		while abs(self.Evaluate(fox, c)) > error:
			# get c
			c = (a + b) / 2.0
		
			# substitute c to fox
			foc = self.Evaluate(fox, c)
			
			# check if foc is < or > 0
			if foc < 0:
				a = c
			elif foc > 0:
				b = c
	
			# update
			iteration = iteration + 1
			
			# print
			print(f"c is {c:.12f} at iteration no: {iteration}")
			print(f"foc  = {foc:.12f}")
				
		print(f"Root is: {c:.12f}")
		print(f"No. of iterations: {iteration}")

	
	def Evaluate(self, formula, value):
		formula = formula.replace("x", f"{value}")
		formula = eval(formula)
		return formula

def e(x):
	return math.exp(x)		

def main():
	print("Bisection Method Calculator\n")

	formula = input("Input formula (for e, use e(x)): ")
	a = float(input("Input a: "))
	b = float(input("Input b: "))
	DOF = float(input("Input DOF: "))
	
	myProgram = Bisection(formula, a, b, DOF)
	
	
if __name__ == "__main__":
	main()
