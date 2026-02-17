'''15.Write a program that takes a point P(px, py) and determines the quadrant it lies in. Explicitly
handle the cases when the point lies on the axes or at the origin.'''
px = int(input("Enter px: "))
py = int(input("Enter py: "))
if px == 0 and py == 0:
    print("The point lies at the origin.")
elif px == 0:
    print("The point lies on the Y-axis.")
elif py == 0:
    print("The point lies on the X-axis.")
elif px > 0 and py > 0:
    print("The point lies in the First Quadrant.")
elif px < 0 and py > 0:
    print("The point lies in the Second Quadrant.")
elif px < 0 and py < 0:
    print("The point lies in the Third Quadrant.")
else:
    print("The point lies in the Fourth Quadrant.")