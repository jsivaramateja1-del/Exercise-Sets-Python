'''14.Write a program that takes as input:
• center of a circle (cx, cy),
• radius r,
• a point P(px, py),
and determines whether the point lies inside the circle, on the circle, or outside the circle.'''
cx = int(input("Enter center x-coordinate (cx): "))
cy = int(input("Enter center y-coordinate (cy): "))
r = int(input("Enter radius (r): "))
px = int(input("Enter point x-coordinate (px): "))
py = int(input("Enter point y-coordinate (py): "))
# Calculate the distance from the center to the point P
distance_squared = ((px - cx) ** 2) + ((py - cy) ** 2)
radius_squared = r ** 2
if distance_squared < radius_squared:
    print("The point lies inside the circle.")
elif distance_squared == radius_squared:
    print("The point lies on the circle.")
else:
    print("The point lies outside the circle.")