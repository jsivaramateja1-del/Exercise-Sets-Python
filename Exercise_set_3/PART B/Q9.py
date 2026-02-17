#Q9. Write a program to count the number of words in a string (words separated by spaces).
n = input("Enter an string : ")
i = 0
words = 0
while i < len(n):
    if n[i] != ' ' and (i == 0 or n[i-1] == ' '):
        words += 1
    i += 1
print("Numbers of words : ",words)