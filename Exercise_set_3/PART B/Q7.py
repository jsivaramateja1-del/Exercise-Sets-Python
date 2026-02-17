#Q7.Write a program to print characters of a string in reverse order using a while loop
n = input("Enter an string : ")
i = len(n) - 1
while i >= 0:
    print(n[i],end = '')
    i -= 1