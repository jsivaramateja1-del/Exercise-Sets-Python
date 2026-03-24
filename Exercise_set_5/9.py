'''
9. Create a function moveDups that moves duplicate characters to the end with ' '.
Example
moveDups('cartoon') -> 'carton_o'
moveDups('network') -> 'network'
moveDups('aabbcc') -> 'abc_abc'
moveDups('cccbbaaa') -> 'cba_ccbaa'
'''

d = {}
def moveDups(str1):
    s = ""
    for ch in str1:
        if ch not in d:
            s += ch
            d[ch] = 1
        else:
            d[ch] += 1
    s += "_"
    for key in d:
        s += key * (d[key] - 1)
    return s

str1 = input("Enter an number : ")
print(moveDups(str1))