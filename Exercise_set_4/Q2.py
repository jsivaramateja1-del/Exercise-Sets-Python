'''2. Write and test a function that takes a word as input and prints the number of vowels and
consonants in it.'''
def check_vowels_consonants_count(word):
    vowel_count = 0
    consonant_count = 0
    for ch in word:
        if 65 <= ord(ch) <= 90 or 97 <= ord(ch) <= 122:
            if ch in 'AEIOUaeiou':
                vowel_count += 1
            else:
                consonant_count += 1
    print("Number of vowels:", vowel_count)
    print("Number of consonants:", consonant_count)
word = input("Enter a word = ")
check_vowels_consonants_count(word)