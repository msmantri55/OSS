# A semordnilap is a word or a phrase that spells a different word when
# backwards ("semordnilap" is a semordnilap of "palindromes"). Here are some
# examples:
#
#     nametag / gateman
#     dog / god
#     live / evil
#     desserts / stressed
#
# Write a recursive program, `semordnilap`, that takes in two words and says if
# they are semordnilap.
#
# This recursive function is not entirely straightforward. There are a few
# things that you need to check the first time you look at the inputs that you
# should not check on subsequent recursive calls: you need to make sure that the
# strings are not single characters, and also you need to be sure that the
# strings are not equal. If you do this check every time you call your function,
# though, this will end up interfering with the recursive base case (which we
# don't want!).
#
# The idea of a wrapper function is really important. You'll see more wrapper
# functions later. To introduce you to the idea, we are providing you with the
# wrapper function; your job is to write the recursive function semordnilap that
# the wrapper function calls. Here is the wrapper function:
#
# def semordnilapWrapper(str1, str2):
#     # A single-length string cannot be semordnilap
#     if len(str1) == 1 or len(str2) == 1:
#         return False
#
#     # Equal strings cannot be semordnilap
#     if str1 == str2:
#         return False
#
#     return semordnilap(str1, str2)

def semordnilap(str1, str2):
    '''
    str1: a string
    str2: a string

    returns: True if str1 and str2 are semordnilap;
             False otherwise.
    '''

    if len(str1) != len(str2):
        return False
    elif str1[0] != str2[-1]:
        return False
    elif str1[0] == str2[-1]:
        return True

    return semordnilap(str1[1:], str2[:-1])