algorithm: method for solving a problem
data structure: method to store information

steps to developing a usable algorithm
* model the problem
* find an algorithm to solve it
* fast enough? fits in memory?
* if not, figure out why
* find a way to address the problem
* iterate until satisfied

## dynamic connectivity

given a set of N objects
* union command: connect 2 objects
* find/connected query: is there a path connecting the two objects?

## quick find

data structure:
* integer array `id[]` of size N
* interpretation: `p` and `q` are connected if and only if they have the same id

find: check if `p` and `q` have the same id

union: To merge components containing `p` and `q`, change all entries whose id equals `id[p]` to `id[q]`

```
public class QuickFindUF {
    private int[] id;

    public QuickFindUF(int N) {
        id = new int[N];

        // set id of each object to itself (N array accesses)
        for (int i = 0; i < N; i++) {
            id[i] = i;
        }
    }

    // check whether p and q are in the same component (2 array accesses)
    public boolean connected(int p, int q) { return id[p] == id[q]; }

    public void union (int p, int q) {
        int pid = id[p];
        int qid = id[q];
        for (int i = 0; i < id.length; i++) {
            // change all entries with id[p] to id[q] (at most 2N + 2 array accesses)
            if (int i = 0; i < id.length; i++) {
                if (id[i] == pid) id[i] = qid;
            }
        }
    }
}
```

quick find is too slow

operates on quadratic time `N^2`

## quick union

data structure:
* integer array `id[]` of size `N`
* interpretation: `id[i]` is parent of `i`
* Root of `i` is `id[id[id[...id[i]...]]]` <-- keep going until it doesn't change (algorithm ensures no cycles)

find: Check if `p` and `q` have the same root

union: To merge components containing `p` and `q`, set the id of `p`'s root to the id of `q`'s root

---

suppose that in a quick union data structure on 10 elements that the id[] array is

`0 9 6 5 4 2 1 0 5`

what are the roots of 3 and 7, respectively?

`6 and 6`

The root of 3 is 6: 3 -> 5 -> 2 -> 6

The root of 7 is 6: 7 -> 1 -> 9 -> 5 -> 2 -> 6

---

```
public class QuickUnionUF {
    private int[] id;

    public QuickUnionUF(int N) {
        // set id of each object to itself (N array accesses)
        id = new int[N];
        for (int i = 0; i < N; i++) id[i] = 1;
    }

    private int root(int i) {
        // chase parent pointers until reach root (depth of i array accesses)
        while (i != id[i]) id = id[i];
        return i;
    }

    public boolean connected(int p, int q) {
        // check if p and q have same root (depth of p and q array accesses)
        return root(p) == root(q);
    }

    public void union(int p, int q) {
        // change root of p to point to root of q (depth of p and q array accesses)
        int i = root(p);
        int j = root(q);
        id[i] = j;
    }
}
```

quick union is also too slow

cost model: number of array accesses (for read or write)

quick-find defect:
* union too expensive (`N` array accesses)
* trees are flat, but too expensive to keep flat

quick-union defect:
* trees can get tall
* find too expensive (could be `N` array accesses)

## quick union improvements

### weighting

weighted quick union:
* modify quick union to avoid tall trees
* keep track of size of each tree (number of objects)
* balance by linking root of smaller tree to root of larger tree (reasonable alternatives: union by height or "rank")

Java implementation

data structure: same as quick union, but maintain extra array `sz[i]` to count number of objects in the tree rooted at `i`

find: identical to quick union (`return root(p) === root(q);`)

union: modify quick union to
* link root of smaller tree to root of larger tree
* update the `sz[]` array

```
int i = root(p);
int j = root(q);
if (i == j) return;
if (sz[i] < sz[j]) { id[i] = j; sz[j] += sz[i]; }
else               { id[j] = i; sz[i] += sz[j]; }
```

running time:
* find: takes time proportional to depth of `p` and `q`
* union: takes constant time, given roots

proposition: depth of any node `x` is at most `lg N` (lg = base 2 algorithm)

### path compression

quick union with path compression: just after computing the root of `p` set the id of each examined node to point to that root

Java implementation

two pass implementation: add second loop to `root()` to set the `id[]` of each examined node to the root

simpler one-pass variant: make every other node in path point to its grandparent (thereby halving path length)

```
private int root(int i) {
    while (i != id[i]) {
        id[i] = id[id[i]];
        id = id[i];
    }

    return i;
}
```

in practice: no reason not to! keeps tree almost completely flat

## union find applications
* percolation
* games (go, hex)
* dynamic connectivity
* least common ancestor
* equivalence of finite state automata
* Hoshen-Kopelman algorithm in physics
* Hinley-Milner polymorphic type inference
* Kruskal's minimum spanning tree algorithm
* compiling equivalence statements in Fortran
* morphological attribute openings and closings
* Matlab's `bwlabel()` function in image processing
