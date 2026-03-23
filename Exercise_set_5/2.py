'''
2. Create a function minIndexFirstString that takes two strings str1 and str2. Return
the largest index of a character in str1 that is also present in str2. If none exist return
-1.
Example
minIndexFirstString("tiger", "integer") -> 4
minIndexFirstString("integer", "tiger") -> 6
'''
def minIndexFirstString(str1,str2):
    for i in range(len(str1)-1,-1,-1):
        if str1[i] in str2:
            return i
    return -1

str1 = input("Enter an string : ")
str2 = input("Enter an string : ")
print(minIndexFirstString(str1,str2))