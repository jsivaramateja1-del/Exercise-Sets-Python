#Q2.Given a string, print all characters at even indices using a for loop.
n = input("Enter an string : ")
for i in range(0,len(n),2):
    print(n[i],end=" ")