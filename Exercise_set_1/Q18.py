'''18. Write a program that takes a 2-letter word as input and prints it in capital letters.
Note: Each letter of the input word can be in capital or small letters.'''
a = input("Enter a 2-letter word : ")
print("Process 1:")
if len(a) != 2 or not a.isalpha():
    print("Invalid input! Please enter a 2-letter word.")
else:
    print("Word in capital letters =", a.upper())
print()
print("Process 2:")
if len(a) != 2 or not a.isalpha():
    print("Invalid input! Please enter a 2-letter word.")
else:
    capital_word = ''
    for char in a:
        if 'a' <= char <= 'z':
            capital_word += chr(ord(char) - 32 )
        else:
            capital_word += char
    print("Word in capital letters =", capital_word)