'''25. Write a program that takes a number between 0 and 65535 and prints its hexadecimal
representation. Note: Do not use the hex function.'''
num = int(input("Enter a number between 0 and 65535: "))
if num < 0 or num > 65535:
    print("Number out of range.")
else:
    hex_digits = "0123456789ABCDEF"
    hex_representation = ""
    temp_num = num
    while temp_num > 0:
        remainder = temp_num % 16
        hex_representation = hex_digits[remainder] + hex_representation
        temp_num //= 16
    if hex_representation == "":
        hex_representation = "0"
    print(f"The hexadecimal representation of {num} is: {hex_representation}")