'''12.Write a program that takes the length and breadth of a rectangle as input and prints its area
and perimeter. Also print whether the area is greater than the perimeter.'''
length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))
area = length * breadth
perimeter = 2 * (length + breadth)
print(f"Area of the rectangle: {area}")
print(f"Perimeter of the rectangle: {perimeter}")
if area > perimeter:
    print("The area is greater than the perimeter.")
elif area == perimeter:
    print("The area is equal to the perimeter.")
else:
    print("The area is not greater than the perimeter.")