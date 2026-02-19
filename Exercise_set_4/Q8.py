'''8. Write a function add square() that takes a 3-digit integer as its argument and finds the sum
of the squares of digits in the number.'''
def add_square(a):
    Sum = 0
    rem = 0
    while a > 0:
        rem = a % 10
        Sum += rem ** 2
        a = a // 10
    return Sum
num = int(input("Enter a 3-digit number: "))
if 100 <= num <= 999:
    print("The sum of the squares of the digits in %d is %d" % (num, add_square(num)))
else:
    print("Please enter a valid 3-digit number.")