'''14. Write a program that takes a valid letter grade (S/A/B/C/D/E) as input and prints its
respective grade point (10/9/8/7/6/4).
Note: If an invalid letter grade is entered, the program should display an appropriate
message.'''
a = input("Enter a valid letter grade (S/A/B/C/D/E): ")
print("Process 1:")
if a == 'S':
    print("Grade Point = 10")
elif a == 'A':
    print("Grade Point = 9")
elif a == 'B':
    print("Grade Point = 8")
elif a == 'C':
    print("Grade Point = 7")
elif a == 'D':
    print("Grade Point = 6")
elif a == 'E':
    print("Grade Point = 4")
else:
    print("Invalid input! Please Enter a valid letter grade.")
print()
print("Process 2:")
grade_points = {'S': 10, 'A': 9, 'B': 8, 'C': 7, 'D': 6, 'E': 4}
if a in grade_points:
    print(f"Grade Point = {grade_points[a]}")
else:
    print("Invalid input! Please Enter a valid letter grade.")
print()