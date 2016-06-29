def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    sum = 0;

    for key in hand:
        sum += hand[key]
    
    return sum