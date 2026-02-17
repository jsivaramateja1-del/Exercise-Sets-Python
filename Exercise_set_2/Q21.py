#21.Write a program to swap two integers without using a third variable.
a = int(input("Enter an number : "))
b = int(input("Enter an number : "))
print("Before swapping: a =", a, ", b =", b)
a = a^b
b = a^b
a = a^b
print("After swapping: a =", a, ", b =", b)