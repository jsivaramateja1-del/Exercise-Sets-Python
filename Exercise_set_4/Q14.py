'''14. Write a function that returns the non-negative square root of a number rounded to the nearest
integer.'''
def square_root(num):

    if num < 0:
        return None

    return round(num ** 0.5)


number = float(input("Enter a number: "))

ans = square_root(number)

if ans is None:
    print("Square root not defined for negative numbers.")
else:
    print("The square root of", number, "is", ans)


# without round off function
'''def square_root(num):

    if num < 0:
        return None

    root = num ** 0.5
    integer_part = int(root)

    if root - integer_part >= 0.5:
        return integer_part + 1
    else:
        return integer_part


number = float(input("Enter a number: "))

result = square_root(number)

if result is None:
    print("Square root not defined for negative numbers.")
else:
    print("The square root of", number, "rounded to nearest integer is", result)'''