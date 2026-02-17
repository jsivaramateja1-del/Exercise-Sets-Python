#Q10. Given a string, count the number of special characters (characters other than alphabets and digits).
n = input("Enter a string : ")
sp_chowdary_aslam = 0
for i in n:
    x = ord(i)
    if not ((x >= 65 and x <= 90) or (x >= 97 and x <= 122) or (x >= 48 and x <= 57)):
        sp_chowdary_aslam += 1
print("Number of special characters = %d"%(sp_chowdary_aslam))