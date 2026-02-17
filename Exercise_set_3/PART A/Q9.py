#Q9. Write a program to reverse a string using a for loop.
n = input("Enter a string : ")
for i in range(len(n)-1,-1,-1):
    print(n[i],end='')