'''20.A distributor supplies mobile phones based on stock availability and payment status. Write
a program to implement the given policy and print appropriate messages'''
stock = int(input("Enter the number of phones in stock: "))
payment_status = input("Enter payment status (p-paid,u-unpaid): ")
if payment_status != "p" and payment_status != "u":
    print("Invalid payment status.")
else:
    if stock > 0 and payment_status == "p":
        print("Phone will be delivered.")
    elif stock > 0 and payment_status == "u":
        print("Payment pending. Phone will be delivered after payment.")
    else:
        print("Phone is out of stock.")