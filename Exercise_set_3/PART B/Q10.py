#Q10. Given a string, print each character and classify it as vowel, consonant, digit, or special character.
n = input("Enter an string : ")
i = 0
while i < len(n):
    ch = ord(n[i])
    if 65 <= ch <= 90 or 97 <= ch <= 122:
        if n[i] in 'aeiouAEIOU':
            print(n[i],"- is a vowel.")
        else:
            print(n[i],"- is a consonant.")
    elif 48 <= ch <= 57:
        print(n[i],"- is a digit.")
    else:
        print(n[i],"- is a special character.")
    i += 1