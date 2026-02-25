'''20. Write a program that takes a character as input and prints the alpha-numeric character (0 to 9,
A to Z, a to z are alpha-numeric characters) that is closest to this character.
Note: If the input character is equidistant from two alpha-numeric values, either one can
be printed.'''
a = input("Enter a character: ")
if len(a) != 1:
    print("Please enter a single character.")
else:
    ascii_val = ord(a)
    alphanumeric = []
    for i in range(48, 58):
        alphanumeric.append(i)
    for i in range(65, 91):
        alphanumeric.append(i)
    for i in range(97, 123):
        alphanumeric.append(i)
    closest_char = min(alphanumeric, key=lambda x: abs(x - ascii_val))
    print("Closest alpha-numeric character is:", chr(closest_char))
'''print("Process 2 :")
ch = input("Enter a character: ")

ascii_input = ord(ch)
closest = ''
min_diff = 1000

# digits 0 - 9
for i in range(ord('0'), ord('9')+1):
    diff = abs(ascii_input - i)
    if diff < min_diff:
        min_diff = diff
        closest = chr(i)

# uppercase A - Z
for i in range(ord('A'), ord('Z')+1):
    diff = abs(ascii_input - i)
    if diff < min_diff:
        min_diff = diff
        closest = chr(i)

# lowercase a - z
for i in range(ord('a'), ord('z')+1):
    diff = abs(ascii_input - i)
    if diff < min_diff:
        min_diff = diff
        closest = chr(i)

print("Closest alphanumeric character:", closest)'''