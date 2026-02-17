'''9. Write a program that takes the marks for 5 subjects as input and calculates the total and
average marks.'''
print("Process 1 : Using list")
print("Enter marks for 5 subjects : ")
marks = []
sum = 0
for i in range(5):
    mark = float(input(f"Enter marks for subject {i+1} : "))
    marks.append(mark)
    sum += mark
print("Total marks = %.2f."%(sum))
print("Average marks = %.2f."%(sum/5))

print("\nProcess 2 : Without using list")
sum = 0
for i in range(5):
    mark = float(input(f"Enter marks for subject {i+1} : "))
    sum += mark
print("Total marks = %.2f."%(sum))
print("Average marks = %.2f."%(sum/5))