'''4. Write a program that takes the length and breadth of a rectangle as input and prints its area
and perimeter.
Note: If the inputs are invalid, display an appropriate message.'''
l = float(input("Enter the length of the rectangle = "))
b = float(input("Enter the breadth of the rectangle = "))
if (l <= 0 or b <= 0):
    print("Invalid Input!")
else :
    print("Area of the rectangle = %.3f"%(l*b))
    print("Perimeter of the rectangle = %.3f"%(2*(l+b)))