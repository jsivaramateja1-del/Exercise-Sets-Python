#Q5. Write a program to find the first uppercase letter in a string using a while loop.
n = input("Enter an string : ")
i = 0
while i < len(n):
    ch = n[i]
    if  65 <= ord(ch) <= 90:
        print(ch)
        break
    i += 1