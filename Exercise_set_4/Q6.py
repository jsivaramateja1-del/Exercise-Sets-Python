'''6. Write a function called calcSeconds() which takes three arguments for hours, minutes, and
seconds and returns the total time in seconds. Example: calcSeconds(1, 3, 20) should
return 3800.'''
def calcSeconds(hours,minutes,seconds):
    return hours*3600 + minutes*60 + seconds
h = int(input("Enter hours: "))
m = int(input("Enter minutes: "))
s = int(input("Enter seconds: "))
print(f"The total time in seconds is {calcSeconds(h, m, s)}")