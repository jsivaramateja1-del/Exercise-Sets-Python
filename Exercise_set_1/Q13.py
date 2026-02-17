'''13. Write a program that takes an integer as input and checks if it is divisible by 17.'''
a = int(input("Enter an integer: "))
if a % 17 == 0:
    print(f"{a} is divisible by 17")
else:
    print(f"{a} is not divisible by 17")