'''15. Write a program to select one option from the list and display output accordingly.
Example:
Please enter your choice:
1. Check Balance
2. View Offers
3. Special Recharge
Enter 0 to exit
(Display some arbitrary message for each option, e.g., “Your balance is Rs. 500”.)'''
print("Please enter your choice:")
print("1. Check Balance")
print("2. View Offers")
print("3. Special Recharge")
print("Enter 0 to exit")
a = int(input())
while a != 0:
    if a == 1:
        print("Your balance is Rs. 500")
    elif a == 2:
        print("You have 100 SMS and 1GB data left")
    elif a == 3:
        print("Special Recharge of Rs. 199 activated")
    else:
        print("Invalid choice! Please select a valid option.")
    print()
    print("Please enter your choice:")
    print("1. Check Balance")
    print("2. View Offers")
    print("3. Special Recharge")
    print("Enter 0 to exit")
    a = int(input())
print("Exited successfully.")