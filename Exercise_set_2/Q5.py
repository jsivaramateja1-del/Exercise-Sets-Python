#5.Write a program that takes as input n1 o1 n2 o2 n3, where n1, n2, n3 are natural numbers and o1, o2 ∈ {+,−, ∗}. Use nested if--else--if statements to evaluate the expression.
n1 = int(input("Enter first natural number (n1): "))
o1 = input("Enter first operator (o1) [+,-,*]: ")
n2 = int(input("Enter second natural number (n2): "))
o2 = input("Enter second operator (o2) [+,-,*]: ")
n3 = int(input("Enter third natural number (n3): "))
if o1 == '+':
    if o2 == '+':
        result = n1 + n2 + n3
    elif o2 == '-':
        result = n1 + n2 - n3
    elif o2 == '*':
        result = n1 + n2 * n3
    else:
        result = "Invalid operator o2"
elif o1 == '-':
    if o2 == '+':
        result = n1 - n2 + n3
    elif o2 == '-':
        result = n1 - n2 - n3
    elif o2 == '*':
        result = n1 - n2 * n3
    else:
        result = "Invalid operator o2"
elif o1 == '*':
    if o2 == '+':
        result = n1 * n2 + n3
    elif o2 == '-':
        result = n1 * n2 - n3
    elif o2 == '*':
        result = n1 * n2 * n3
    else:
        result = "Invalid operator o2"
else:
    result = "Invalid operator o1"
print("The result of the expression is:", result)