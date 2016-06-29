# Python is an MIT student who loves fruits. He carries different types of
# fruits (represented by capital letters) daily from his house to the MIT
# campus to eat on the way. But the way he eats fruits is unique. After each
# fruit he eats (except the last one which he eats just on reaching the campus),
# he takes a 30 second break in which he buys 1 fruit of each type other than
# the one he just had. Cobra, his close friend, one day decided to keep a check
# on Python. He followed him on his way to MIT campus and noted down the type
# of fruit he ate in the form of a string pattern (Eg.: 'AABBBBCA'). Can you
# help Cobra determine the maximum quantity out of the different types of
# fruits that is present with Python when he has reached the campus?

# Write a function nfruits that takes two arguments:

# A non-empty dictionary containing type of fruit and its quantity initially
# with Python when he leaves home (length < 10)

# A string pattern of the fruits eaten by Python on his journey as observed by
# Cobra.

# This function should return the maximum quantity out of the different types
# of fruits that is available with Python when he has reached the campus.

# For example, if the initial quantities are {'A': 1, 'B': 2, 'C': 3} and the
# string pattern is 'AC' then

# 'A' is consumed, updated values are {'A': 0, 'B': 2, 'C': 3}
# Python buys 'B' and 'C', updated values are {'A': 0, 'B': 3, 'C': 4}
# 'C' is consumed, updated values are {'A': 0, 'B': 3, 'C': 3}

# Now Python has reached the campus. So the function will return 3 that is
# maximum of the quantities of the three fruits.

def nfruits(fruits, pattern):
    # loop through indexed pattern
    for i, val in enumerate(pattern):
        # loop through keys in fruits dict
        for key in fruits.keys():
            # check if current iteration is final iteration
            if i != len(pattern) - 1:
                if key == pattern[i]:
                    fruits[key] -= 1
                else:
                    fruits[key] += 1
            else:
                # skip incrementation on final iteration
                if key == pattern[i]:
                    fruits[key] -= 1
    return max(fruits.values())

print nfruits({'H': 6, 'R': 9, 'U': 6, 'N': 10}, 'N')
print nfruits({'F': 10, 'M': 5, 'R': 7, 'T': 7, 'V': 5, 'Y': 10, 'X': 6}, 'VVTM')