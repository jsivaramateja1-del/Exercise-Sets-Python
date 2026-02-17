'''19. Write a program that takes a 2-letter word as input and prints it in small letters.
Note: Each letter of the input word can be in capital or small letters.'''
a = input("Enter a 2-letter word: ")
print("Process 1 :")
if len(a) != 2 or not a.isalpha():
    print("Invalid input! Please enter a 2-letter word.")
else:
    print("Word in small letters =", a.lower())
print()
print("Process 2:")
if len(a) != 2 or not a.isalpha():
    print("Invalid input! Please enter a 2-letter word.")
else:
    small_word = ''
    for char in a:
        if 'A' <= char <= 'Z':
            small_word += chr(ord(char) + 32)
        else:
            small_word += char
    print("Word in small letters =", small_word)