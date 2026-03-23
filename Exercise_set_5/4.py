'''
4. Create a function evenIndexCapital. Capitalize characters at even indices. Raise
UpperCaseException if input contains uppercase letters.
Example
evenIndexCapital('school') -> 'ScHoOl'
'''
class UpperCaseException(Exception):
    pass
def evenIndexCapital(str1):
    s = ""
    
    # check for uppercase letters first
    for ch in str1:
        if 'A' <= ch <= 'Z':
            raise UpperCaseException("Input contains uppercase letters")
        
    # process string
    for i in range(len(str1)):
        if i%2 == 0:
            s += chr(ord(str1[i])-32)
        else:
            s += str1[i]
    return s

# input and handling exception
try:
    str1 = input("Enter a string: ")
    print(evenIndexCapital(str1))
except UpperCaseException as e:
    print(e)