'''
3. Create a function firstLetters that returns the first letter of every word.
Example
firstLetters('bad is nice') -> 'bin'
firstLetters('hello other world') -> 'how'
'''

def firstLetters(str1):
    s = ""
    # first character
    if len(str1) > 0:
        s += str1[0]
    # check for spaces
    for i in range(len(str1)):
        if str1[i] == " " and i+1 < len(str1):
            s += str1[i+1]
    return s

str1 = input("Enter an string : ")
print(firstLetters(str1))