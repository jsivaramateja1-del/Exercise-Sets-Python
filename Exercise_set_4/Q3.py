'''3. Write and test a function that takes a number as parameter and prints the multiplication table
of that number.'''
def multiplication_table(num,n):
    for i in range(1,n+1):
        print(f"{num} x {i} = {num*i}")
num = int(input("Enter a number: "))
n = int(input("Enter the range for multiplication table: "))
multiplication_table(num,n)