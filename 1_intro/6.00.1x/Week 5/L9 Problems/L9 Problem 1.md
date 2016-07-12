Here is some code from lecture:

```
def linearSearch(L, x):
    for e in L:
        if e == x:
            return True
    return False
```

Choose which of the following inputs to linearSearch would give the best case, average case, or worst case run time.

1. Best Case Run Time

    * linearSearch([14, 15, 6, 27, 13, 16, 25, 11, 7], 15)
    * linearSearch([21, 1, 25, 22, 30, 13, 7, 24, 12], 24)
    * **linearSearch([20, 10, 1, 7, 4, 22, 25, 12, 31], 20)**
    * linearSearch([9, 3, 12, 24, 7, 8, 23, 11, 19], 8)
    * linearSearch([4, 12, 20, 17, 9, 14, 7, 24, 6], 7)
    * linearSearch([13, 9, 22, 3, 10, 17, 11, 2, 12], 26)

2. Worst Case Run Time

    * linearSearch([14, 15, 6, 27, 13, 16, 25, 11, 7], 15)
    * linearSearch([21, 1, 25, 22, 30, 13, 7, 24, 12], 24)
    * linearSearch([20, 10, 1, 7, 4, 22, 25, 12, 31], 20)
    * linearSearch([9, 3, 12, 24, 7, 8, 23, 11, 19], 8)
    * linearSearch([4, 12, 20, 17, 9, 14, 7, 24, 6], 7)
    * **linearSearch([13, 9, 22, 3, 10, 17, 11, 2, 12], 26)**

3. Average Case Run Time

    * linearSearch([14, 15, 6, 27, 13, 16, 25, 11, 7], 15)
    * linearSearch([21, 1, 25, 22, 30, 13, 7, 24, 12], 24)
    * linearSearch([20, 10, 1, 7, 4, 22, 25, 12, 31], 20)
    * **linearSearch([9, 3, 12, 24, 7, 8, 23, 11, 19], 8)**
    * linearSearch([4, 12, 20, 17, 9, 14, 7, 24, 6], 7)
    * linearSearch([13, 9, 22, 3, 10, 17, 11, 2, 12], 26)

4. What is the number of steps it will take to run linearSearch in the best case? Express your answer in terms of n, the number of elements in the list L. Indicate addition and multiplication explicitly, with + and * symbols. Indicate exponentiation with the caret (^) symbol.

`2n + 1`


5. What is the number of steps it will take to run linearSearch in the worst case? Express your answer in terms of n, the number of elements in the list L. Indicate addition and multiplication explicitly, with + and * symbols. Indicate exponentiation with the caret (^) symbol.

`2*n+1`