#3.Write a program that takes an integer as input and checks, using bitwise operations, if it is divisible by 4.
n = int(input("Enter an number : "))
if n & 3 == 0:
    print(f"{n} is divisible by 4")
else:
    print(f"{n} is not divisible by 4")