# Write a function called ndigits, that takes an integer x (either positive or
# negative) as an argument. This function should return the number of digits in
# x.

def ndigits(integer):
    # Ensure we properly count the number of digits
    integer = abs(integer)

    # base case is 1 since the minimum number of digits has to be 1
    counter = 1
    
    if integer == 0:
        return 0
    else:
        return counter + ndigits(integer / 10)

print ndigits(-9090428)