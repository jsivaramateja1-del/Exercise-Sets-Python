'''27. Write a program that takes a 4-character hexadecimal number and prints its decimal equivalent.
Note: Do not use hex, bin, or int functions.'''
hex_num = input("Enter a 4-character hexadecimal number: ")
decimal_value = 0

for ch in hex_num:
    if '0' <= ch <= '9':
        digit = ord(ch) - ord('0')
    else:
        digit = ord(ch) - ord('A') + 10

    decimal_value = decimal_value * 16 + digit

print(decimal_value)
