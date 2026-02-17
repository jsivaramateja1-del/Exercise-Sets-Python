#6.Write a program that takes as input two integers and prints appropriate messages if at least one or both are positive, negative, or zero.
n1 = int(input("Enter first integer: "))
n2 = int(input("Enter second integer: "))
if n1 > 0 and n2 > 0:
    print("Both numbers are positive.")
elif n1 < 0 and n2 < 0:
    print("Both numbers are negative.")
elif n1 == 0 and n2 == 0:
    print("Both numbers are zero.")
elif (n1 > 0 and n2 < 0) or (n1 < 0 and n2 > 0):
    print("One number is positive and the other is negative.")
else:
    if n1 == 0 and n2 != 0:
        print("First number is zero and second is non-zero.")
    else:
        print("Second number is zero and first is non-zero.")