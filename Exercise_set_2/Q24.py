'''24. Write a program that takes a positive integer and prints the quotient and remainder when
divided by 2. Note: Do not use / or % operators.'''
num = int(input("Enter a positive integer: "))
if num < 0:
    print("Please enter a positive integer.")
else:
    quotient = num >> 1  # Equivalent to num // 2
    remainder = num & 1  # Equivalent to num % 2
    print(f"Quotient: {quotient}, Remainder: {remainder}")