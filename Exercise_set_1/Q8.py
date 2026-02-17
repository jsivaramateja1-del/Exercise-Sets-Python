'''8. Write a program that takes a three-digit integer as input and prints the sum of its digits.'''
a = int(input("Enter an 3 - digit number : "))
if a >= 100 and a <= 999:
    sum = 0
    while(a!=0):
        rem = a%10
        sum = sum + rem
        a = a//10
    print(f"Sum of digits = {sum}")
else:
    print("Invalid input! Please Enter valid 3-digit number.")