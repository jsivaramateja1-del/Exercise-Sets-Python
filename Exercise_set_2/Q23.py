'''23.Write a program that takes three integers x, y, z and checks the divisibility of x by y and z,
printing appropriate messages.'''
x = int(input("Enter first integer (x): "))
y = int(input("Enter second integer (y): "))
z = int(input("Enter third integer (z): "))
if y == 0 or z == 0:
    print("Divisibility by zero is not allowed.")
else:
    if x % y == 0 and x % z == 0:
        print(f"{x} is divisible by both {y} and {z}.")
    elif x % y == 0:
        print(f"{x} is divisible by {y} but not by {z}.")
    elif x % z == 0:
        print(f"{x} is divisible by {z} but not by {y}.")
    else:
        print(f"{x} is not divisible by either {y} or {z}.")