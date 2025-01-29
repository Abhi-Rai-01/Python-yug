# Comparision Operators:-
# - compares values on either side of the operator and decide the relation among them.
# - return boolean value (True/False)
# Below are comparison operators:-
# 1) greater than (>)
# 2) less than (<)
# 3) equal to (==)
# 4) not equal to (!=)
# 5) greater than or equal (>=)
# 6) less than or equal (<=)

num1 = 10
num2 = 20
num3 = 10
print(num1>num2)   #10>20
print(num2>num1)   #20>10

print("\t",num3>num1)

print(num1<num2)   #20>10
print(num2<num1)   #20>10

print("\t",num1<num3)

print(num1==num3)
print(num1==num2)

print("\t")

print(num1!=num2)
print(num1!=num3)

print("\t")

print(num1>=num2)
print(num2>=num1)
print(num1>=num3)

print("\t")

print(num1<=num2)
print(num2<=num1)
print(num3<=num1)