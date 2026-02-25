'''11.Write a program that takes a date in the format DDMMYYYY and prints the day of the week it
falls on. Given: 01-01-1990 was a Monday.'''
d = int(input("Enter day: "))
m = int(input("Enter month: "))
y = int(input("Enter year: "))

days = [31,28,31,30,31,30,31,31,30,31,30,31]
total = 0

# Count full years from 1990 to y-1
for year in range(1990, y):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        total += 366
    else:
        total += 365

# Adjust February for leap year
if (y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)):
    days[1] = 29

# Count months
for i in range(m - 1):
    total += days[i]

# Count days
total += d - 1

weekdays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
print(weekdays[total % 7])

'''print("Process 2 :")
d = int(input("Enter day: "))
m = int(input("Enter month: "))
y = int(input("Enter year: "))

# January and February adjustment
if m == 1 or m == 2:
    m = m + 12
    y = y - 1

K = y % 100
J = y // 100

h = (d + (13*(m+1))//5 + K + K//4 + J//4 + 5*J) % 7

# printing day without list
if h == 0:
    print("Saturday")
elif h == 1:
    print("Sunday")
elif h == 2:
    print("Monday")
elif h == 3:
    print("Tuesday")
elif h == 4:
    print("Wednesday")
elif h == 5:
    print("Thursday")
else:
    print("Friday")'''