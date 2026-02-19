# 4. Write and test a function add square that returns the square of its parameter.
def add_square(x):
    return x**2
a = int(input("Enter a number: "))
print("The square of %d is %d" % (a, add_square(a)))