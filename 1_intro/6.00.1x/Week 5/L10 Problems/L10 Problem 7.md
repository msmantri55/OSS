This problem will walk through some applications of complexity analysis. Suppose you're asked to implement an application. One of the things it has to do is to report whether or not an item, `x`, is in a list `L`. `L`'s contents do not change over time. Below are two possible ways to implement this functionality. Assume that `mergeSort` is implemented as per the lecture.

`L` is a list with `n` items.

* **Application A:**

Every time it's asked to, it performs a linear search through list `L` to find whether it contains x.

* **Application B:**

Sort list `L` once before doing anything else (using mergeSort). Whenever it's asked to find `x` in L, it performs a binary search on L.

1. If the application is asked to find `x` in `L` exactly one time, what is the worst case time complexity for Application A?

O(n)

If the application is asked to find `x` in `L` exactly one time, what is the worst case time complexity for Application B?

O(n log n)

If the application is asked to find `x` in `L` *k* times, what is the worst case time complexity for Application A?

O(kn)

If the application is asked to find `x` in `L` *k* times, what is the worst case time complexity for Application B?

O(n log n + k log n)

What value(s) of *k* would make Application A be faster (i.e., asymptotically grow slower than) Application B?

k = 1

What value(s) of *k* would make Application A grow at the same rate as Application B?

k = log n

Which application should you choose if you know that there are going to be n<sup>3</sup> requests to find `x` in L?

Application B