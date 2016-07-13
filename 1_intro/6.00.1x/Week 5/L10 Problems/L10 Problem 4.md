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
def search3(L, e):
    if L[0] == e:
        return True
    elif L[0] > e:
        return False
    else:
        return search3(L[1:], e)
```

Which of the following statements is correct? You may assume that each function is tested with a list L whose elements are sorted in increasing order. For simplicity, assume L is a list of integers.

`search` and `search3` return the same answers provided `L` is non-empty and `e` is in `L`. 