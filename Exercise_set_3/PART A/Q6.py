#Q6.Given a string, replace all vowels with the character * and print the modified string.
n = input("Enter an string : ")
for i in n:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U' :
        print('*',end='')
    else:
        print(i,end='')