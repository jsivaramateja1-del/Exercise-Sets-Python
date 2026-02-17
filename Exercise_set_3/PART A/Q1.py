#Q1. Write a program to count the number of vowels in a given string.
'''
ch = input("Enter an string : ")
count = 0
for i in range(len(ch)):
    if ch[i] == 'a' or ch[i] == 'e' or ch[i] == 'i' or ch[i] == 'o' or ch[i] == 'u' or ch[i] == 'A' or ch[i] == 'E' or ch[i] == 'I' or ch[i] == 'O' or ch[i] == 'U':
        count += 1
print("Count of vowels in given string : %d"%(count))
'''
'''
ch = input("Enter a string: ")
count = 0
vowels = "aeiouAEIOU"

for c in ch:
    if c in vowels:
        count += 1

print("Count of vowels in given string:", count)
'''

ch = input("Enter a string: ")
print("Count of vowels in given string:", sum(1 for c in ch if c in "aeiouAEIOU"))
