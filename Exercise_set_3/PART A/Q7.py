#Q7.Write a program to check whether a string contains more vowels or more consonants
n = input("Enter an string : ")
v_count = 0
c_count = 0
for i in n:
    x = ord(i)
    if (x >= 65 and x <= 90) or (x >= 97 and x <= 122) :
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U' :
            v_count += 1
        else:
            c_count += 1
print("Vowel Count = %d"%(v_count))
print("Consonant Count = %d"%(c_count))
if v_count > c_count:
    print("The string contains %d more vowels."%(v_count - c_count))
elif v_count == c_count:
    print("The string contains equal number of vowels and consonants")
else:
    print("The string contains %d more consonants."%(c_count - v_count))