Here is the code for selection sort. For simplicity, assume `L` is a list of integers:

```
def selSort(L):
    for i in range(len(L) - 1):
        minIndx = i
        minVal = L[i]
        j = i+1
        while j < len(L):
            if minVal > L[j]:
                minIndx = j
                minVal = L[j]
            j += 1
        if minIndx != i:
            temp = L[i]
            L[i] = L[minIndx]
            L[minIndx] = temp
```

And here is a suggested alternative:

```
def newSort(L):
    for i in range(len(L) - 1):
        j=i+1
        while j < len(L):
            if L[i] > L[j]:
                temp = L[i]
                L[i] = L[j]
                L[j] = temp
            j += 1
```

1. Do these two functions result in the same sorted lists?

* **Yes**
* No

2. Do these two functions execute the same number of assignments of values into entries of the lists?

* Yes. They execute the same number of assignments.
* **No. `newSort` may use more - but never fewer - inserts than `selSort`.**
* No. `selSort` may use more - but never fewer - inserts than `newSort`.
* No. Either function may use more inserts than the other.

3. Is the worst-case order of growth of these functions the same?

* **Yes. `newSort` and `selSort` have the same complexity.**
* No. `newSort` has higher complexity than `selSort`.
* No. `selSort` has higher complexity than `newSort`. 