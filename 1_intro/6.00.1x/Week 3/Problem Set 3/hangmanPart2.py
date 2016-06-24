# `isWordGuessed` takes in two parameters - a string, `secretWord`, and a list
# of letters, `lettersGuessed` This function returns a boolean - True if
# `secretWord` has been guessed (ie, all the letters of `secretWord` are in
# `lettersGuessed`) and False otherwise.

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

# `getGuessedWord` takes in two parameters - a string, `secretWord`, and a list
# of letters, `lettersGuessed`. This function returns a string that is
# comprised of letters and underscores, based on what letters in
# `lettersGuessed` are in `secretWord`. This shouldn't be too different from
# `isWordGuessed`!

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

# `getAvailableLetters` takes in one parameter - a list of letters,
# `lettersGuessed`. This function returns a string that is comprised of
# lowercase English letters - all lowercase English letters that are not in
# `lettersGuessed`.

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


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    def prompt(guessesMade, availableLetters):
        print '-------------'
        print 'You have %(guesses)i guesses left' % { 'guesses': 8 - guessesMade }
        print 'Available letters: %(letters)s' % { 'letters': availableLetters }

        return raw_input('Please guess a letter: ').lower()
        
    lettersGuessed = []
    guessesMade = 0

    print 'Welcome to the game Hangman!'
    print 'I am thinking of a word that is %(number)i letters long' % \
            { 'number': len(secretWord) }

    while guessesMade < 8:
        availableLetters = getAvailableLetters(lettersGuessed)
        guess = prompt(guessesMade, availableLetters)

        if guess in lettersGuessed:
            print 'Oops! You\'ve already guessed that letter: %(guessedword)s' % \
                { 'guessedword': getGuessedWord(secretWord, lettersGuessed) }
        elif guess not in secretWord:
            lettersGuessed += guess
            print 'Oops! That letter is not in my word: %(guessedword)s' % \
                { 'guessedword': getGuessedWord(secretWord, lettersGuessed) }
            guessesMade += 1
        elif guess in secretWord:
            lettersGuessed += guess
            print 'Good guess: %(guessedword)s' % \
                { 'guessedword': getGuessedWord(secretWord, lettersGuessed) }

        if isWordGuessed(secretWord, lettersGuessed):
            print '-------------'
            print 'Congratulations, you won!'
            return
    
    if guessesMade == 8:
        print '-------------\nSorry, you ran out of guesses. The word was %(word)s' % \
            { 'word': secretWord }