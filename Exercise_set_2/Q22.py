'''22. Write a program to convert percentage marks into grades:
• 91–100: S
• 81–90: A
• 71–80: B
• 61–70: C
• Below 60: D'''
marks = int(input("Enter percentage marks: "))
if 91 <= marks <= 100:
    grade = 'S'
elif 81 <= marks <= 90:
    grade = 'A'
elif 71 <= marks <= 80:
    grade = 'B'
elif 61 <= marks <= 70:
    grade = 'C'
else:
    grade = 'D'
print(f"The grade is: {grade}")