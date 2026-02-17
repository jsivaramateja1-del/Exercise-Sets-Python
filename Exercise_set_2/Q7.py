#7.Write a program that takes as input two integers and checks if their LCM is equal to at least one of the given integers.
n1 = int(input("Enter first integer: "))
n2 = int(input("Enter second integer: "))
if n1 == 0 or n2 == 0:
    print("LCM is not defined for zero.")
elif n1%n2 == 0 or n2%n1 == 0:
    print("The LCM of", n1, "and", n2, "is equal to at least one of the given integers.")
else:
    print("The LCM of", n1, "and", n2, "is not equal to either of the given integers.")