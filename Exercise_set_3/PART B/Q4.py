#Q4. Given a string, print each character and check whether it is a digit or not.
n = input("Enter an string : ")
i=0
while i < len(n):
    ch =n[i]
    if ch >= '0' and ch <= '9':
        print(ch,'- digit')
    else :
        print(ch,"- not a digit")    
    i+=1