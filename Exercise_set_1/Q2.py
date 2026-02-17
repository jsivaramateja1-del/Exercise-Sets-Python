'''2. Write a program that takes two integers a and b as input and prints their sum, difference,
product, quotient, and remainder.'''
a = int(input("Enter an integer : "))
b = int(input("Enter an integer : "))
print("Sum = %d."%(a+b))
print("Difference = %d."%(a-b))
print("Product = %d."%(a*b))
if b != 0:
    print("Quotient = %d."%(a//b))
    print("Remainder = %d."%(a%b))
else : 
    print("Quotient = Not Defined.")
    print("Remainder = Not Defined.")