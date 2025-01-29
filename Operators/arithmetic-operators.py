# Arithmetic Operators:-
# - used to perform arithmetic operations on two or more operands.
# Below are arithmetic operators:
# 1) + addition
# 2) - subtraction
# 3) * multiplication
# 4) / division
# 5) % Remainder
# 6) // floor division
# 7) ** exponetiation

#addition, subtraction, multiplication, division

print(2 + 3)
print(2.0 + 3)   #if any one of the two operands is float then the result will also be float
print(2 - 3)
print(2.1 - 3)   #if any one of the two operands is float then the result will also be float
print(2 * 3)
print(2 * 3.0)   #if any one of the two operands is float then the result will also be float
print(2 / 3)    #always returns float value only

print("\t")
print("\t")
print("\t")
print("\t")

# using variables
num1 = 2
num2 = 3
print(num1 + num2)

print("\t")
print("\t")
print("\t")
print("\t")

# Remainder
num1 = 10
num2 = 10.0
num3 = 3

print(num1 % num3)
print(num2 % num3)      #because one the operand is float so the output will float

print("\t")
print("\t")
print("\t")
print("\t")

# floor division
num1 = 10
num2 = 10.0
num3 = -10
num4 = 3

print(num1 / num4)      #this is a normal division
print(num1 // num4)     #this is a floor division(floor division is like greatest integer function)
print(num2 // num4)     #most of the people thing floor division returns int value but that's wrong because it can return float values also
print(num3 // num4)

print("\t")
print("\t")
print("\t")
print("\t")

# exponentiation

num1 = 2
num2 = 2.0
num3 = 3
num4 = 3.0

print(num1**num3)     #2^3=8
print(num1**num4)
print(num2**num4)