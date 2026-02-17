'''19. Worker efficiency is determined by time taken to complete a job. Write a program that takes
the time taken as input and prints the efficiency category.'''
time_taken = float(input("Enter time taken to complete the job (in hours): "))
if time_taken < 2:
    category = "Highly Efficient"
elif 2 <= time_taken <= 4:
    category = "Efficient"
else:
    category = "Less Efficient"
print(f"The worker's efficiency category is: {category}")