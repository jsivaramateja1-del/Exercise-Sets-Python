#Q8. Given a string, print only those characters which are alphabets.
n = input("Enter an string : ")
for i in n:
    x = ord(i)
    if (x >= 65 and x <= 90) or (x >= 97 and x <= 122) :
        print(i,end = "")