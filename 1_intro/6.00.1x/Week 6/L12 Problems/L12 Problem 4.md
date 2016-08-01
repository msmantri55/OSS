This problem will ask some questions about the previous problem. You will want to refer to the Hand class from L12_hand.py.

1. There are two ways to write the Hand.update method: you could write this method in a way that gets rid of the key letter in the attribute hand dictionary when the frequency of the letter falls to 0, or write it in a way that leaves the key letter in the attribute hand dictionary even when the frequency of the letter falls to 0. Will the two different implementations of the Hand.update method lead to Hand objects having different hand internal attributes?

Yes, depending on what happened during the update call

2. There are two ways to write the Hand.update method: you could write this method in a way that gets rid of the key letter in the attribute hand dictionary when the frequency of the letter falls to 0, or write it in a way that leaves the key letter in the attribute hand dictionary even when the frequency of the letter falls to 0. Does the calculateLen method, as defined, return different values for the two different implementations of the update method?

No