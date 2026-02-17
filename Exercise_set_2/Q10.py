'''10.Write a program that takes a year as input and prints whether it is a leap year or not. Note:
The year can be any year in the past or up to 100 years into the future.'''
year = int(input("Enter a year: "))
if (year%4==0 and year%100!=0) or (year%400==0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")