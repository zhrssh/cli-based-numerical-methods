from sympy import *

class FixedPointIteration:
    def __init__(self):
        pass

    def fpi(self, eq, gx, a, b, dof, isradian=False):
        # Initialize symbols
        x, y, z = symbols('x'), symbols('y'), symbols('z')

        # From string to numbers
        eq = sympify(eq)
        gx = sympify(gx)
        a = float(a)
        b = float(b)
        dof = float(dof)

        self.x0 = 0

        # Check if the equations satisfies the FPI conditions
        if eq.evalf(subs={x: a}) > 0:
            raise Exception("f(a) must be less than 0, try another value of `a`")
        
        elif eq.evalf(subs={x: b}) < 0:
            raise Exception("f(b) must be greater than 0, try another value of `b`")

        else:
            self.x0 = (a + b) / 2.0
            print(f"X0 is {self.x0}")

        diff_gx = diff(gx, x)
        val = diff_gx.evalf(subs={x: self.x0})
        assert {
            val < 1,
            f"G'(X0) must be < 1, got: {val}"
        }

        # Solve

        print(f"\n\nComputing for Fixed Point Iteration of: {fox}\n")

        iterations = 0
        prev_x0 = 0
        while abs(gx.evalf(subs={x: self.x0}) - prev_x0) > dof:
            iterations = iterations + 1
            self.x0 = gx.evalf(subs={x: self.x0})
            prev_x0 = self.x0

            # Print what's happening
            print(f"Iteration: {iterations} | X: {self.x0:.12f}")
        
        # Print final root
        if isradian == False:
            print(f"No. of iterations: {iterations} | Root: {self.x0:.12f} or {self.x0:.4f}")
        else:
            print(f"No. of iterations: {iterations} | Root: {math.radians(self.x0):.12f} or {math.radians(self.x0):.4f}")


def main():
    myProgram = FixedPointIteration()
    init_printing()   

    eq = input("f(x): ")
    gx = input("g(x): ")
    a = input("a: ")
    b = input("b: ")
    dof = input("dof: ")
    isradian = input("in radians? y/n: ")
    isradian = True if isradian == 'y' else False

    myProgram.fpi(eq, gx, a, b, dof, isradian)


if __name__ == "__main__":
    main()
