'''17. Write a program that takes two 5-letter words as input and finds the sum of the distance
between the respective characters of these words.
Example:
Input:
abcde
abdfe
Distance: 0-0-1-2-0
Output: 3
Input:
pqxzy
qpyax
Distance: 1-1-1-25-1
Output: 29'''
word1 = input("Enter first 5-letter word: ")
word2 = input("Enter second 5-letter word: ")
if len(word1) != 5 or len(word2) != 5:
    print("Both words must be exactly 5 letters long.")
else:
    total = 0
    for i in range(5):
        total += abs(ord(word1[i]) - ord(word2[i]))
    print("Output:", total)