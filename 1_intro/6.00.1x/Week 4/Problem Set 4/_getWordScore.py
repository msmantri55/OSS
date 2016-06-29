# The function getWordScore should accept as input a string of lowercase letters
# (a word) and return the integer score for that word, using the game's scoring
# rules.

# SCRABBLE_LETTER_VALUES = {
#     'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1,
# 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's':
# 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
# }

from ps4a import SCRABBLE_LETTER_VALUES

def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    lettersum = 0

    # sum up points for letters in the word
    for letter in word:
        lettersum += SCRABBLE_LETTER_VALUES[letter]
    
    # multiply sum by length of word
    lettersum *= len(word)

    # apply bonus if all n letters are used
    if len(word) == n:
        lettersum += 50

    return lettersum

# should return 0
print getWordScore("", 7)

# should return 4
print getWordScore("it", 7)

# should return 18
print getWordScore("was", 7)

# should return 54
print getWordScore("scored", 7)

# should return 155
print getWordScore("waybill", 7)

# should return 127
print getWordScore("outgnaw", 7)

# should return 44
print getWordScore("fork", 7)

# should return 94
print getWordScore("fork", 4)