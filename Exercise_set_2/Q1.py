#1.Write a program to swap the contents of two variables using only bitwise operations
a = int(input("Enter an number : "))
b = int(input("Enter an number : "))
a = a ^ b
b = a ^ b
a = a ^ b
print("After swapping a =",a)
print("After swapping b =",b)