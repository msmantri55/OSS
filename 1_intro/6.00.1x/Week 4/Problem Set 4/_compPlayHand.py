def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    # Keep track of the total score
    total = 0

    chosenWord = ''
    while chosenWord != None:
        try:
            if any(val != 0 for val in hand.values()):
                # Display the hand
                print 'Current Hand: ',
                for key in hand:
                    for i in range(hand[key]):
                        # print all on same line
                        print key,

                # print newline
                print

            # choose a word
            chosenWord = compChooseWord(hand, wordList, n)

            # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
            total += getWordScore(chosenWord, n)
            print '"%(in)s" earned %(pts)s points. Total: %(t)s points.\n' % \
                {
                    "in": chosenWord,
                    "pts": str(getWordScore(chosenWord, n)),
                    "t": str(total),
                }
            
            # Update the hand 
            hand = updateHand(hand, chosenWord)
        except TypeError as e:
            print 'Total score: %(total)s points.' % {"total": str(total)}