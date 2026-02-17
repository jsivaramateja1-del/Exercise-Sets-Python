#Q5.Write a program to count the number of digits in a given string.
n = input("Enter an string : ")
dt_count = 0
for i in n:
    if ord(i) >= 48 and ord(i) <= 57:
        dt_count += 1
print("Number of digits in the given string = %d"%(dt_count))