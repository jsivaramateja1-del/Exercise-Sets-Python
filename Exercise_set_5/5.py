'''
5. Create a function shift that rotates the string left by acount and then right by
ccount.
Example

1

shift('NinjaHattori') -> 'NinjaHattori'
shift('NinjaHattori', acount=3) -> 'jaHattoriNin'
shift('NinjaHattori', ccount=3) -> 'oriNinjaHatt'
shift('NinjaHattori', ccount=3, acount=3) -> 'NinjaHattori'
shift('NinjaHattori', ccount=3, acount=6) -> 'jaHattoriNin'
shift('NinjaHattori', ccount=6, acount=3) -> 'oriNinjaHatt'
'''
def shift(s, acount=0, ccount=0):
    # length of string
    n = len(s)

    # handle empty string case
    if n == 0:
        return s

    # calculate net shift
    # right shift (ccount) - left shift (acount)
    net = (ccount - acount) % n

    # Explanation:
    # if net > 0 → right shift
    # if net == 0 → no change

    # perform right shift using slicing
    # last 'net' characters + remaining part
    result = s[-net:] + s[:-net]

    return result

s = input("Enter string: ")

# take counts (default 0 if empty)
acount = input("Enter left shift (acount): ")
ccount = input("Enter right shift (ccount): ")

# convert to int (handle empty input)
acount = int(acount) if acount else 0
ccount = int(ccount) if ccount else 0

# output
print("Result:", shift(s, acount, ccount))