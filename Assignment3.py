'''
Task 1: Using the Math Module for Calculations
Problem Statement: Write a Python program
Asks the user for a number as input.
Uses the math module to calculate the:
Square root of the number
Natural logarithm (log base e) of the number
Sine of the number (in radians)
'''


'''
from math import *
num2=int(input('Enter a number: '))
result= log(num2)
print(f"Logarithm base of {num2} is:", result)
result= (sqrt(num2))
print(f"Square root of {num2} is:", result)
result= sin(num2)
print(f"Sine of {num2} is:", result)
'''




'''
Task 2: Calculate Factorial Using a Function
Problem Statement: Write a Python program that:
Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
Returns the calculated factorial.
Calls the function with a sample number and prints the output.
'''


'''
def factorial (n):
if n<2:
    return 1
else:
    return n* (factorial(n-1))

num=int(input('Enter a number: '))
result = factorial(num)
print(f"factorial of {num} is:", result)
'''

