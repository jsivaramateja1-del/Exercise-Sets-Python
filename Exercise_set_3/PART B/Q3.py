#Q3.Write a program to count the number of spaces in a given string.
n = input("Enter an string : ")
sp_count = 0
i = 0
while i < len(n):
    ch = n[i]
    if ch == ' ':
        sp_count += 1
    i += 1
print("Number of spaces = %d"%(sp_count))