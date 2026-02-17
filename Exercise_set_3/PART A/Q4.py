#Q4.Given a string, print each character and check whether it is a vowel or a consonant.
n = input("Enter an string : ")
for i in n:
    if (ord(i) >= 65 and ord(i) <= 90) or (ord(i) >= 97 and ord(i) <= 122) :
            if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U' :
                print(i,'- vowel')
            else:
                print(i,'- consonant')
    else:
        print(i,"- INVALID INPUT!!!!")