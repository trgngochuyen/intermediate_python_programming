#import string

import scrabble

# print English words without double of a certain letter 
# for letter in string.ascii_lowercase:
#     exists = False
#     for word in scrabble.wordlist:
#         if letter * 2 in word:
#             exists = True
#             break
#     if not exists:
#         print("There are no English words with a double " + letter)

# print English words that contain all vowelss
vowels = "aeiou"

def has_all_vowels(word):
    for vowel in vowels:
        if vowel not in word:
            return False
    return True

for word in scrabble.wordlist:
    if has_all_vowels(word):
        print(word)