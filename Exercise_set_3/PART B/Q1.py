#Q1. Write a program to count the number of vowels in a string using a while loop.
n = input("Enter a string : ")
i = 0
v_count = 0
while i < len(n):
    ch = n[i]
    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U':
        v_count += 1
    i += 1
print("Number of vowels = %d"%(v_count))