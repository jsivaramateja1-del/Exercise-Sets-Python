'''
1. A palindrome is a word that reads the same backward as forwards.
Create a function checkPalindrome to check whether the string passed as its argument
is a palindrome.
Example
checkPalindrome('madam') -> True
checkPalindrome('racecar') -> True
checkPalindrome('python') -> False
'''
# using slicing
def checkPalindrome(string):
    if string[::-1] == string:
        return True
    else:
        return False

# using flag variable and for loop
# def checkPalindrome(string):
#     n = len(string)
#     flag = True
#     for i in range(n//2):
#         if string[i] != string[n-i-1]:
#             flag = False
#             break
#     if flag == True:
#         return True
#     else:
#         return False

# using empty string and for loop
# def checkPalindrome(string):
#     rev = ""
#     for ch in string:
#         rev = ch + rev
#     if string == rev:
#         return True
#     else:
#         return False
string = input("Enter the string : ")
print(checkPalindrome(string))
