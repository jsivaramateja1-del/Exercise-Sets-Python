'''13. Write a function prodDigits that takes a 5-digit number as its parameter and returns the
product of the digits of the number.'''
def prodDigits(num):
    product = 1
    while num > 0:
        digits = num % 10
        product *= digits
        num //= 10
    return product
number = int(input("Enter an number : "))
if number >= 10000 and number <= 99999:
    print(f"Product of the digits of the {number} = {prodDigits(number)}.")
else:
    print('Number should be between 10000 and 99999')