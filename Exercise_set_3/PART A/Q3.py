#Q3.Write a program to count how many uppercase and lowercase letters are present in a string.
n = input("Enter an string : ")
up_count = dwn_count = 0
for i in n:
    if ord(i) >= 65 and ord(i) <= 90:
        up_count += 1
    if ord(i) >= 97 and ord(i) <= 122:
        dwn_count += 1
print("Uppercase Count = %d"%(up_count))
print("Lowercase Count = %d"%(dwn_count))