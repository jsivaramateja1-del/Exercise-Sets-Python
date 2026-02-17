'''26. Write a program that takes a number between 0 and 31 and prints its binary representation.
Note: Do not use the bin function.'''
num = int(input("Enter a number between 0 and 31: "))

if num < 0 or num > 31:
    print("Number out of range.")
else:
    binary_representation = ""
    for i in range(4, -1, -1):
        binary_representation += str((num >> i) & 1)

    print(binary_representation)
