'''13.Write a program that takes three points (x1, y1), (x2, y2), and (x3, y3) and checks if they lie
on a straight line.'''
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))
x3 = int(input("Enter x3: "))
y3 = int(input("Enter y3: "))
# Check if the area of the triangle formed by the three points is zero
area = x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)
if area == 0:
    print("The points lie on a straight line.")
else:
    print("The points do not lie on a straight line.")