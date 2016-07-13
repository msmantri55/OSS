In lecture, we saw a version of linear search that used the fact that a set of elements is sorted in increasing order. Here is the code from lecture:

```
def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False
```

Consider the following code, which is an alternative version of search.

```
def search1(L, e):
    for i in L:
        if i == e:
            return True
        if i > e:
            return False
    return False
```

Which of the following statements is correct? You may assume that each function is tested with a list L whose elements are sorted in increasing order; for simplicity, assume L is a list of positive integers.

**search and search1 return the same answers.** 