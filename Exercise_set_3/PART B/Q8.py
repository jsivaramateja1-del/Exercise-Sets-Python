#Q8. Given a string, check whether the string contains at least one vowel
n = input("Enter an string : ")
i = 0
found = False
while i < len(n):
    if n[i] in 'aeiouAEIOU':
        found = True
        break
    i += 1
if found:
    print("The given string has atleast one vowel.")
else:
    print("The given string does not have any vowel.")