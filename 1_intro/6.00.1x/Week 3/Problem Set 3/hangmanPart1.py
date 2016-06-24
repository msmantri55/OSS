# `isWordGuessed` takes in two parameters - a string, `secretWord`, and a list of letters,
# `lettersGuessed` This function returns a boolean - True if `secretWord` has been guessed (ie,
# all the letters of `secretWord` are in `lettersGuessed`) and False otherwise.

# Example Usage:

# >>> secretWord = 'apple' 
# >>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
# >>> print isWordGuessed(secretWord, lettersGuessed)
# False

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    match = False

    # checks first character in secretWord against each item in lettersGuessed
    for item in lettersGuessed:
        if secretWord[0] == item:
            match = True
            break
        else:
            match = False

    if len(secretWord) == 1 and match == True:
        return match
    elif match == True:
        return isWordGuessed(secretWord[1:], lettersGuessed)
    else:
        return match

# `getGuessedWord` takes in two parameters - a string, `secretWord`, and a list of letters,
# `lettersGuessed`. This function returns a string that is comprised of letters and
# underscores, based on what letters in `lettersGuessed` are in `secretWord`. This shouldn't
# be too different from `isWordGuessed`!

# Example Usage:

# >>> secretWord = 'apple' 
# >>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
# >>> print getGuessedWord(secretWord, lettersGuessed)
# '_ pp_ e'

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guess = []

    for i in range(0, len(secretWord)):
        guess += '_'

        for item in lettersGuessed:
            if secretWord[i] == item:
                guess[i] = item
    
    return ' '.join(guess)

# `getAvailableLetters` takes in one parameter - a list of letters, `lettersGuessed`. This
# function returns a string that is comprised of lowercase English letters - all lowercase
# English letters that are not in `lettersGuessed`.

# Example Usage:

# >>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
# >>> print getAvailableLetters(lettersGuessed)
# abcdfghjlmnoqtuvwxyz

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string

    alphabet = string.ascii_lowercase

    for letter in alphabet:
        if letter in lettersGuessed:
            alphabet = alphabet.replace(letter, '')

    return alphabet

lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print getAvailableLetters(lettersGuessed)