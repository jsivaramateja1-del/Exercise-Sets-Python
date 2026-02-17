'''10. Write a program that takes three integers as input and prints the minimum (of the three
values).'''
a = int(input("Enter first integer = "))
b = int(input("Enter second integer = "))
c = int(input("Enter third integer = "))
print("process 1 :")
if a <= b and a <= c:
    print(f"Minimum = {a}")
elif b <= a and b <= c:
    print(f"Minimum = {b}")
else:
    print(f"Minimum = {c}")
print()
print("process 2:")
print("Minimum = %d"%(min(a,b,c)))