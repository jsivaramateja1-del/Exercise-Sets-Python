'''
8. Create a function delVowels that removes all vowels.
Example
delVowels('SfgEtfjofubjiekp') -> 'Sfgtfjfbjkp'
delVowels('aEiOu') -> ''
'''


def delVowels(str1):
    s = ""
    for ch in str1:
        if ch not in "aeiouAEIOU":
            s += ch
    return s

str1 = input("Enter an number : ")
print(delVowels(str1))