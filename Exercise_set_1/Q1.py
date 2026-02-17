'''Write a program that takes the radius of a circle as input and computes its area.
Note: If the radius is non-negative, display an appropriate message.'''
r = float(input("Enter the radius of the circle : "))
pi = 3.14159
if r < 0:
    print("Please give valid input.")
else:
    area = pi*r**2
    print("Area of the circle = %f."%(area))