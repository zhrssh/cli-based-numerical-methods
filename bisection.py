from sympy import *

x, y, z = symbols("x y z")
class Bisection:	
	def __init__(self, fox, a, b, DOF):
		# Conditions
		if a > b:
			raise Exception(f"a must be less than b")
		
		val = fox.evalf(subs={x: a},chop=True) * fox.evalf(subs={x: b},chop=True)
		if val > 0:
			raise Exception(f"f(a) * f(b) must be less than 0, got {val}")
		
		self.Compute(fox, a, b, DOF)
	def Compute(self, fox, a, b, DOF):
		print(f"\n\nComputing for Bisection of: {fox}\n")
		
		# test is fox = 2x^3 - 2x - 5 -> (2 * (x ** 3)) - (2 * x) - 5)
		# fox = "((2 * (x ** 3)) - (2 * x) - 5)"
		
		error = DOF
		c = (a + b) / 2.0
		iteration = 0
		while abs(fox.evalf(subs={x: c})) > error:
			# get c
			c = (a + b) / 2.0
		
			# substitute c to fox
			foc = fox.evalf(subs={x: c})
			
			# check if foc is < or > 0
			if foc < 0:
				a = c
			elif foc > 0:
				b = c
	
			# update
			iteration = iteration + 1
			
			# print
			print(f"\nc is {c:.12f} at iteration no: {iteration}")
			print(f"foc  = {foc:.12f}")
				
		print(f"Root is: {c:.12f}")
		print(f"No. of iterations: {iteration}")

def main():
	print("Bisection Method Calculator\n")

	formula = sympify(input("Input formula (for e, use exp(x)): "))
	a = float(input("Input a: "))
	b = float(input("Input b: "))
	DOF = float(input("Input DOF: "))
	
	myProgram = Bisection(formula, a, b, DOF)
	
if __name__ == "__main__":
	main()
