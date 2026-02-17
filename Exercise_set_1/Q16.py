'''16. Write a program that takes as input the coefficients of the quadratic equation

ax2 + bx + c = 0
and prints whether the roots are real or complex.'''
a = int(input("Enter coefficient a: "))
b = int(input("Enter coefficient b: "))
c = int(input("Enter coefficient c: "))
if a == 0: 
    print("Not a quadratic equation.")
else:
    D = b**2 - 4*a*c
    if D >= 0:
        print("Roots are real.")
    else:
        print("Roots are complex.")