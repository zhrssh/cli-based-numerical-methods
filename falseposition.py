from sympy import *

x, y, z = symbols("x y z")
class FalsePosition:
	def __init__(self, fox, a, b, DOF):
		
		# Conditions
		if a > b:
			raise Exception("A must be less than B")
		
		val = fox.evalf(subs={x: a}, chop=True) * fox.evalf(subs={x: b}, chop=True)
		if val > 0:
			raise Exception(f"f(a) and f(b) must be opposite signs: got {val}")
		
		self.Compute(fox, a, b, DOF)
	
	def Compute(self, fox, a, b, DOF):
		print(f"\n\nComputing for False Position of: {fox}\n")

		# While f(x) > DOF
		c = 1
		
		iteration = 0
		while abs(fox.evalf(subs={x: c})) > DOF:
				
			# update iteration
			iteration = iteration + 1
				
			# x1 = (af(b) - bf(a)) / f(b) - f(a)
			c = ((a * fox.evalf(subs={x: b})) - (b * fox.evalf(subs={x: a}))) / (fox.evalf(subs={x: b}) - fox.evalf(subs={x: a}))
			
			# check conditions
			if fox.evalf(subs={x: c}) != 0 and fox.evalf(subs={x: c}) < 0:
				a = c
				
			# print values
			print(f"\nc is {c:.12f} at iteration no. {iteration}")
			print(f"foc = {fox.evalf(subs={x: c}):.12f}")
			
		print(f"Root is: {c:.12f}")
		print(f"Number of iterations: {iteration}")

def main():
	# Start of program
	print("False Position Method Calculator\n")

	formula = sympify(input("Input formula (for e, use exp(x)): "))
	a = float(input("Input a: "))
	b = float(input("Input b: "))
	DOF = float(input("Input DOF: "))
	
	myProgram = FalsePosition(formula, a, b, DOF)

if __name__ == "__main__":
	main()
