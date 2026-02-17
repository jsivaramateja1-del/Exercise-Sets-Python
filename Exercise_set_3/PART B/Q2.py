#Q2. Given a string, print all characters until a vowel is encountered using a while loop.
n = input("Enter a string : ")
i = 0
while i < len(n):
    ch = n[i]
    if ch in 'aeiouAEIOU':
        break
    print(ch,end='')
    i += 1