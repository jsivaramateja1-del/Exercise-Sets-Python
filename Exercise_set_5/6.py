def distChar(str1, str2):
    freq = {}
    # mark characters from str1
    for ch in str1:
        freq[ch] = 1

    # process str2
    for ch in str2:
        if ch in freq:
            freq[ch] = 0   # common → remove
        else:
            freq[ch] = 1   # new unique

    # build result
    result = ""
    for ch in freq:
        if freq[ch] == 1:
            result += ch

    # sort result
    return ''.join(sorted(result))


# -------- USER INPUT --------
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

print("Result:", distChar(str1, str2))