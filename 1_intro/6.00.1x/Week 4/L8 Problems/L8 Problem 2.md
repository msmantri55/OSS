Below are some short Python programs. For each program, answer the associated question.

Try to answer the questions without running the code. Check your answers, then run the code for the ones you get wrong.

These questions will ask you to write what the code prints out. If an exception is raised that is not handled by the code write "error" (no quotes), in addition to any other text that is output.

The function in the following questions takes a list of integers `numbers` and a position `index`, and divides each entry in the list of numbers by the value at entry `index`.

Write what it prints out, separating what appears on a new line by a comma and a space.

```
def FancyDivide(numbers,index):
    try:
        denom = numbers[index]
        for i in range(len(numbers)):
            numbers[i] /= denom
    except IndexError, e:
        print "-1"
    else:
        print "1"
    finally:
        print "0"
```

What does `FancyDivide([0, 2, 4], 1)` print out?

1, 0

What does `FancyDivide([0, 2, 4], 4)` print out?

-1, 0

What does `FancyDivide([0, 2, 4], 0)` print out?

0, error

```
def FancyDivide(numbers, index):
    try:
        denom = numbers[index]
        for i in range(len(numbers)):
            numbers[i] /= denom
    except IndexError, e:
        FancyDivide(numbers, len(numbers) - 1)
    except ZeroDivisionError, e:
        print "-2"
    else:
        print "1"
    finally:
        print "0"
```
        
What does `FancyDivide([0, 2, 4], 1)` print out?

1, 0

What does `FancyDivide([0, 2, 4], 4)` print out?

1, 0, 0

What does `FancyDivide([0, 2, 4], 0)` print out?

-2, 0

```
def FancyDivide(numbers, index):
    try:
        try:
            denom = numbers[index]
            for i in range(len(numbers)):
                numbers[i] /= denom
        except IndexError, e:
            FancyDivide(numbers, len(numbers) - 1)
        else:
            print "1"
        finally:
            print "0"
    except ZeroDivisionError, e:
        print "-2"
```        

What does `FancyDivide([0, 2, 4], 1)` print out?

1, 0

What does `FancyDivide([0, 2, 4], 4)` print out?

1, 0, 0

What does `FancyDivide([0, 2, 4], 0)` print out?

0, -2

```
def FancyDivide(list_of_numbers, index):
    try:
        try:
            raise Exception("0")
        finally:
            denom = list_of_numbers[index]
            for i in range(len(list_of_numbers)):
                list_of_numbers[i] /= denom
    except Exception, e:
        print e
```


Does this code print 0 when you call `FancyDivide([0, 2, 4], 0)`?


* Yes.
* **No.**

```
def FancyDivide(list_of_numbers, index):
    try:
        try:
            denom = list_of_numbers[index]
            for i in range(len(list_of_numbers)):
                list_of_numbers[i] /= denom
        finally:
            raise Exception("0")
    except Exception, e:
        print e
```     

Does this print 0 when you call `FancyDivide([0, 2, 4], 0)`?

* **Yes.**
* No.