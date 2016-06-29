def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # make sure word is in wordlist
    output = False
    try:
        if word in wordList:
            for letter in word:
                if word.count(letter) <= hand[letter]:
                    output = True
                else:
                    return False
        else:
            return False
        return output
    except KeyError:
        return False