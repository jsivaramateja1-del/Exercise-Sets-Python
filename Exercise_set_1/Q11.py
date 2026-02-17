'''11. Write a program that takes an integer as input and displays if it is odd or even.'''
a = int(input("Enter an integer: "))
print("Process 1:")
if (a % 2) == 0:
    print("Even")
else:
    print("Odd")
print()
print("Process 2:")
if (a & 1) == 0:
    print("Even")
else:
    print("Odd")