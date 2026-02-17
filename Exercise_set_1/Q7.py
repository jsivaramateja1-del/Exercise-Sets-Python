'''7. Write a program that takes three integers as input and prints their maximum value.'''
a = int(input("Enter first integer = "))
b = int(input("Enter second integer = "))
c = int(input("Enter third integer = "))
print("process 1 :")
if a >= b and a >=c:
    print(f"Maximum = {a}")
elif b >= a and b >= c:
    print(f"Maximum = {b}")
else:
    print(f"Maximum = {c}")
print("process 2:")
print("Maximum = %d"%(max(a,b,c)))