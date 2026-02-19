'''5. Write a function that takes three numbers as parameters and returns the median value of those
parameters.'''
def median(a, b, c):
    if (a <= b and b <= c) or (c <= b and b <= a):
        return b
    elif (b <= a and a <= c) or (c <= a and a <= b):
        return a
    else:
        return c
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))
print("The median of %d , %d and %d is %d" % (x, y, z, median(x, y, z)))