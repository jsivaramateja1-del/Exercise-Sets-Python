'''12. Write a function cubesum that accepts a 3-digit integer and returns the sum of the cubes of
individual digits of that number. Use this function in another function isArmstrong to check
if its 3-digit parameter is an Armstrong number. Example: 371 is an Armstrong number since
33 + 73 + 13 = 371.'''
def cubesum(num):
    temp = num
    total = 0
    while temp > 0:
        digit = temp % 10
        total += digit ** 3
        temp //= 10
    return total
def isArmstrong(num):
    return num == cubesum(num)
number = int(input("Enter a 3-digit number: "))
if 100 <= number <= 999:
    if isArmstrong(number):
        print(f"{number} is an Armstrong number.")
    else:
        print(f"{number} is not an Armstrong number.")
else:
    print("Please enter a valid 3-digit number.")