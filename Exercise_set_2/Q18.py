'''18. A library charges a fine for late returns:
• First 5 days: 50 paise
• 6–10 days: 1 rupee
• Above 10 days: 5 rupees
If returned after 30 days, membership is canceled. Write a program to display the fine or
the appropriate message.'''
days_late = int(input("Enter the number of days the book is late: "))
if days_late <= 5:
    fine = days_late * 0.50
    print(f"Fine: Rs. {fine:.2f}")
elif 6 <= days_late <= 10:
    fine = (5 * 0.50) + ((days_late - 5) * 1.00)
    print(f"Fine: Rs. {fine:.2f}")
elif 11 <= days_late <= 30:
    fine = (5 * 0.50) + (5 * 1.00) + ((days_late - 10) * 5.00)
    print(f"Fine: Rs. {fine:.2f}")
else:
    print("Membership canceled.")