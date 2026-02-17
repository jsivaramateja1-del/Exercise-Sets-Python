'''16. Insurance Premium Calculation
A (hypothetical) insurance company wishes to automate its premium calculation and policy
restrictions. The rules are as follows:
(a) If a person’s health is excellent, the person is between 25 and 35 years of age, lives
in a city, and is a male, then the premium is Rs. 4000 per month and the policy
amount cannot exceed Rs. 2 lakhs.
(b) If all the above conditions are satisfied except that the person is female, then the
premium is Rs. 3000 per month and the policy amount cannot exceed Rs. 1.5
lakhs.
(c) If a person’s health is poor, the person is between 25 and 35 years of age, lives in
a village, and is a male, then the premium is Rs. 6000 per month and the policy
amount cannot exceed Rs. 1 lakh.
(d) In all other eligible cases, the premium is Rs. 5000 per month and the policy amount
cannot exceed Rs. 1.25 lakhs.
(e) A person below 25 years of age or above 65 years of age will not be insured.
(f) If the policy value requested is less than the maximum allowed, the monthly premium
amount is proportional to the policy value.'''
age = int(input("Enter age: "))
health = input("Enter health (e - excellent, p - poor): ")
location = input("Enter location (c - city, v - village): ")
gender = input("Enter gender (m - male, f - female): ")
policy_value = float(input("Enter policy amount: "))

if age < 25 or age > 65:
    print("The person will not be insured.")
else:
    if health == 'e' and age >= 25 and age <= 35 and location == 'c' and gender == 'm':
        max_policy = 200000
        premium = 4000

    elif health == 'e' and age >= 25 and age <= 35 and location == 'c' and gender == 'f':
        max_policy = 150000
        premium = 3000

    elif health == 'p' and age >= 25 and age <= 35 and location == 'v' and gender == 'm':
        max_policy = 100000
        premium = 6000

    else:
        max_policy = 125000
        premium = 5000

    if policy_value > max_policy:
        print("Requested policy amount exceeds limit.")
    else:
        final_premium = (policy_value / max_policy) * premium
        print("Monthly premium is Rs.", final_premium)
