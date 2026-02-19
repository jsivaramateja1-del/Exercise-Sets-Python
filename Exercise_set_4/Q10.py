'''10. Write a function that takes as an argument a parameter of type Point and returns True if it
lies within the square connecting the points (0, 0), (1, 0), (0, 1), (1, 1); and False otherwise.'''
def is_within_square(x, y):
    if 0 <= x <= 1 and 0 <= y <= 1:
        return True
    else:
        return False


x = float(input("Enter x-coordinate: "))
y = float(input("Enter y-coordinate: "))

if is_within_square(x, y):
    print(f"The point ({x}, {y}) lies within the square.")
else:
    print(f"The point ({x}, {y}) does not lie within the square.")
