'''
10. Create a function separate that groups identical characters.
Example
separate('cartoon') -> ['c','a','r','t','oo','n']
separate('network') -> ['n','e','t','w','o','r','k']
separate('aabbcc') -> ['aa','bb','cc']
separate('cccbbaaa') -> ['ccc','bb','aaa']
'''

def separate(str1):
    d = {}
    for ch in str1:
        if ch not in d:
            d[ch] = 1
        else:
            d[ch] += 1
    return [key * value for key, value in d.items()]

str1 = input("Enter an number : ")
print(separate(str1))