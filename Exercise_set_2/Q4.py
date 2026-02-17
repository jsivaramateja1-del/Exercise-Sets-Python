#4. Write a program that takes a natural number as input and prints the remainder when it is divided by 3.
n = int(input("Enter a natural number: "))
print("Method 1 :")
remainder = n % 3
print(f"The remainder when {n} is divided by 3 is: {remainder}")
print("Method 2 :")
rem = n - (n//3)*3
print(f"The remainder when {n} is divided by 3 is: {rem}")