'''7. Write a function named IIT() that takes a character as an argument and prints IIT in that
character. Example:
Input: ’.’
Output:
          .
          .
          .
          .
          .

          .
          .
          .
          .
          .

    ...............
          .
          .
          .
          .
          .
'''
def IIT(ch):

    # First I
    for i in range(5):
        print(" " * 4 + ch)

    print()

    # Second I
    for i in range(5):
        print(" " * 4 + ch)

    print()

    # Top bar of T (5 characters with spaces)
    for i in range(5):
        print(ch, end=" ")
    print()

    # Vertical line of T (centered)
    for i in range(5):
        print(" " * 4 + ch)

c = input("Enter a character: ")
print(f"The IIT pattern with '{c}' is:")
IIT(c)