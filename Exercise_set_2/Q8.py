'''8.Write a program that takes a 4-letter word as input and toggles the case of all its letters
using bitwise operations. Example: Input: HeLLo
Output: hEllO'''
n = input("Enter a 4-letter word : ")
if len(n) != 4:
    print("Please enter exactly 4 letters.")
else:
    if ord(n[0]) >= 65 and ord(n[0]) <= 90:
        c1 = chr(ord(n[0]) | 32)
    else:
        c1 = chr(ord(n[0]) & ~32)
    if ord(n[1]) >= 65 and ord(n[1]) <= 90:
        c2 = chr(ord(n[1]) | 32)
    else:
        c2 = chr(ord(n[1]) & ~32)
    if ord(n[2]) >= 65 and ord(n[2]) <= 90:
        c3 = chr(ord(n[2]) | 32)
    else:
        c3 = chr(ord(n[2]) & ~32)
    if ord(n[3]) >= 65 and ord(n[3]) <= 90:
        c4 = chr(ord(n[3]) | 32)
    else:
        c4 = chr(ord(n[3]) & ~32)
    print("Toggled case word is :",c1+c2+c3+c4)