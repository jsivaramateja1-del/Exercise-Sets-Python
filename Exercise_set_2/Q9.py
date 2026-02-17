'''9.Write a program that takes as input the cost price and selling price of an item, prints whether
the sale resulted in a profit or a loss, and prints the amount.
'''
cp = float(input("Enter the cost price of the item: "))
sp = float(input("Enter the selling price of the item: "))
if sp > cp:
    profit = sp - cp
    print(f"The sale resulted in a profit of {profit:.2f}")
elif sp < cp:
    loss = cp - sp
    print(f"The sale resulted in a loss of {loss:.2f}")
else:
    print("No profit, no loss.")