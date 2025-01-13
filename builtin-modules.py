# 1) math module:- basic mathematical operations and constants such as trignometry functions, logarithmic functions, etc...
# example:-
import math
print(math.sqrt(25))  #sqaure root
print(math.sin(math.pi / 2)) #Sine


# 2) cmath module:- The cmath module is used for complex number arithmetic.
# example
import cmath
z = complex(2, 3)
print(cmath.sqrt(z))  #complex square root


# 3) statistics module:-
# example
import sympy
x = sympy.symbol('x')
equation = x**2-4
solutions = sympy.solve(equation, x)
print(solutions)


# 4)  sympy:- sympy is a python library for symbolic mathematics. ex. solving equations and expressions.
# example
import sympy
x = sympy.symbols('x')
equation = x**2-4
solutions = sympy.solve(equation, x)
print(solutions)