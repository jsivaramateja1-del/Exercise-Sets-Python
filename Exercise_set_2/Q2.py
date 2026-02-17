#2.Write a program to check whether a number has 0 as its last digit.
n = int(input("Enter an number : "))
if n%10!=0:
    print("Last digit is not 0")
else:
    print("Last digit is 0")