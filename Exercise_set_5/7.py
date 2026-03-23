'''
7. Create a function change that returns the minimum number of changes needed to
make all characters equal.
Example
change('R') -> 0
change('RGRGR') -> 2
change('GRG') -> 1
'''

def change(s):
    freq = {}

    # count frequency
    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    # find maximum frequency
    max_freq = 0
    for ch in freq:
        if freq[ch] > max_freq:
            max_freq = freq[ch]

    # minimum changes
    return len(s) - max_freq


# -------- USER INPUT --------
s = input("Enter string: ")
print("Minimum changes:", change(s))