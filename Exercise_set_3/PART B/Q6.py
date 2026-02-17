#Q6. Given a string, count how many characters are not alphabets.
n = input("Enter an string : ")
nc_count = 0
i = 0
while i < len(n):
    ch = ord(n[i])
    if not ((ch >= 65 and ch <= 90) or (ch >= 97 and ch <= 122)):
        nc_count += 1
    i += 1
print("Number of not alphabets count = %d"%(nc_count))