'''3. Write a simple calculator program. It should be able to add, subtract, multiply, and divide
any two numbers input by the user.
Note: The user will also specify the operation to perform.'''
a = int(input("Enter an integer : "))
b = int(input("Enter an integer : "))
op = input("Enter any one of the following (+,-,*,/) : ")
if op == '+':
    print("Sum = %d."%(a+b))
elif op == '-':
    print("Difference = %d."%(a-b))
elif op == '*':
    print("Product = %d."%(a*b))
elif op == '/':
    if b != 0:
        print("Division = %f."%(a/b))
    else : 
        print("Division = Not Defined.")
else:
    print("Invalid input! Please select anyone of the following (+,-,*,/)")