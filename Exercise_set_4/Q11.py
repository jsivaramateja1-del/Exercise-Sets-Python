'''11. Write a Python function called quadratic roots that takes three arguments (a, b, c) representing
the coefficients of a quadratic equation ax2 + bx + c = 0. The function should return the
positive real root if one exists; otherwise, return None.'''
def quadratic_roots(a, b, c):

    discriminant = b**2 - 4*a*c

    if discriminant < 0:
        return None

    sqrt_d = discriminant ** 0.5

    root1 = (-b + sqrt_d) / (2*a)
    root2 = (-b - sqrt_d) / (2*a)

    # Check for positive roots
    if root1 > 0 and root2 > 0:
        return max(root1, root2)
    elif root1 > 0:
        return root1
    elif root2 > 0:
        return root2
    else:
        return None
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
result = quadratic_roots(a, b, c)
if result is not None:
    print(f"The positive real root is: {result}")
else:
    print("No positive real root exists.")
