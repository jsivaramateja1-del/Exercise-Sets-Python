'''9. Write a function that takes a 3-digit positive integer as its argument and reverses it. Example:
Input: 123, Output: 321 Input: 120, Output: 21'''
def reverse_number(num):
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num = num // 10
    return reversed_num
number = int(input("Enter a 3-digit positive integer: "))
if 100 <= number <= 999:
    print("The reverse of %d is %d" % (number, reverse_number(number)))
else:
    print("Please enter a valid 3-digit positive integer.")