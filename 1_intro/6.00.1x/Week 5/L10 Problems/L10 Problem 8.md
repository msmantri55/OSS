This problem aims to walk you through the basics of hashing.

Let's perform some basic hashing. We'll begin with a very simple hash function:

```
def hash(s):
    return len(s)
```

To get a sense of what a hash function does, sort the following list of words into one of the 5 buckets below.

![L10 Problem 8.1](http://i.imgur.com/Gjk4xoo.png)

The previous problem shows the benefits of having a good hash function. Hashing on length of word is very problematic. In English, there are only two words - 'a' and 'I' - that are one letter long. However there are thousands that are 5 letters long - in words.txt (from PS4, which had a very limited set of words) there are 8938 5-letter words.

Ideally we'd like to pick a hash function that uniformly distributes values over a set of buckets. The next part of this problem will ask you to determine if a hash function is good or bad.

A good hash function will uniformly distribute words in the English language across a set of buckets. A bad one will - like hashing on word length - be skewed (ie some buckets will be MUCH more common than others). Note that for this problem we will be asking about valid words in the English language, not random strings of characters.

Read more about the properties of good hash functions over at Wikipedia.

1. Hash function:

```
def hash(s):
    return string.ascii_lowercase.index(s[0])
```

Number of buckets: 26

* Good hash function
* **Bad hash function**

2. Hash function:

```
def hash(s):
    return string.ascii_lowercase.index(s[-1])
```

Number of buckets: 26

* Good hash function
* **Bad hash function**

3. Hash function:

```
def hash(s):
    total = 0
    for char in s:
        total += string.ascii_lowercase.index(char)
    return total % 26
```

Number of buckets: 26

* **Good hash function**
* Bad hash function 