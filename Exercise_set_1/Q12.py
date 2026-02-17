'''12. Write a program that takes a floating-point value as input and prints its absolute value.'''
a = float(input("Enter a floating-point value: "))
print("Process 1:")
if a < 0:
    a = -a
print(f"Absolute value = {a}")
print()
print("Process 2:")
print(f"Absolute value = {abs(a)}")