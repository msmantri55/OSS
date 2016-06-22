# Define a function isVowel2(char) that returns True if char is a vowel ('a',
# 'e', 'i', 'o', or 'u'), and False otherwise. You can assume that char is a
# single letter of any case (ie, 'A' and 'a' are both valid).

def isVowel2(char):
    charIsVowel = False
    for vowel in 'AaEeIiOoUu':
        if char == vowel:
            charIsVowel = True
    return charIsVowel