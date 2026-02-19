'''1. Write and test a function named check leap year that takes as parameter a year between 1600
and 9999. It should return True if the year is a leap year and False otherwise.'''
def check_leap_year(year):
        if(year%400==0)or(year%4==0 and year%100!=0):
            return True
        else:
            return False
year = int(input("Enter a year between 1600 and 9999: "))
if(1600 <= year <= 9999):
    print(check_leap_year(year))
else:
    print("Invalid input. Year must be between 1600 and 9999.")