'''28. Write a program that takes a 4-character binary number and prints its decimal equivalent.
Note: Do not use hex, bin, or int functions.'''
binary = input("Enter a 4-character binary number: ")
if len(binary) != 4 or any(ch not in '01' for ch in binary):
    print("Invalid input. Please enter a 4-character binary number.")
else:
    decimal = 0

    for ch in binary:
        decimal = decimal * 2 + (ord(ch) - ord('0'))

    print(decimal)
