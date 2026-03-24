'''
11. Create a function minOp to compute minimum edit operations between two strings.
Example
minOp('python','pythons') -> 1
minOp('abc','') -> 3
minOp('abc','def') -> 3
minOp('ab','def') -> 3
'''

def minOp(s1, s2):
    i = 0
    count = 0

    # find smaller length manually
    l1 = 0
    for _ in s1:
        l1 += 1

    l2 = 0
    for _ in s2:
        l2 += 1

    # compare common part
    while i < l1 and i < l2:
        if s1[i] != s2[i]:
            count += 1
        i += 1

    # add extra characters (insert/delete)
    if l1 > l2:
        count += (l1 - l2)
    else:
        count += (l2 - l1)

    return count

s1 = input("Enter first string : ")
s2 = input("Enter second string : ")
print(minOp(s1, s2))