Consider the function `Normalize` that takes as input a list of positive `numbers` numbers and returns a list of numbers that are a fraction of the maximum element in the list. Try to answer the questions without running the code. Check your answers, then run the code for the ones you get wrong. You'll learn the most this way, by figuring things out, instead of just running the code and reading off the answers.

```
def Normalize(numbers):
    max_number = max(numbers)
    for i in range(len(numbers)):
        numbers[i] /= float(max_number)
    return numbers   
```

The code below tries to call `Normalize` with one particular input. Answer the next 5 questions based on the following code. 

```
try:
      Normalize([0, 0, 0])
except ZeroDivisionError, e:
      print 'Invalid maximum element'
```

Does the try block throw (also known as raise) an exception?

* **Yes**
* No

What is the name of the exception the code is trying to catch?

ZeroDivisionError

What is the output?

'Invalid maximum element'

Since we are dividing by the maximum element in a list of positive numbers, we know that Normalize will return a value between 0 and 1. What type of condition is this?

* pre condition
* **post condition**

We also know the result is not meaningful when the maximum element is 0, so we want to ensure that the numbers in the list do not violate this. What type of condition is this?

* **pre condition**
* post condition

Now assume the definition of the function Normalize is rewritten as follows

```
def Normalize(numbers):
max_number = max(numbers)
assert(max_number != 0), "Cannot divide by 0"
for i in range(len(numbers)):
    numbers[i]  /= float(max_number)
    assert(0.0 <= numbers[i] <= 1.0), "output not between 0 and 1"
return numbers        
``` 
Answer the next 3 questions based on this code.

Which condition does the line assert(max_number != 0) correspond to?

* **pre condition**
* post condition

Which condition does the line assert(0.0 <= numbers[i] <= 1.0) correspond to?

* pre condition
* **post condition**

What does the function call Normalize([0, 0, 0]) print out?

AssertionError