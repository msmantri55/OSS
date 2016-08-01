# What method is called when an object is created?

* `self`
* `obj.self`
* `init`
* **`__init__`**
* `new`

# If you have an object instance, obj, and you want to call its doSomething() method (assuming it has one), how would you do this? (write the line of code you would use)

`obj.doSomething()`

# True or False? An object's attributes must be defined in the object's __init__ method.

False

# The following code starts the definition of a class called Address. The class needs to have two attributes: number and streetName. Please add in the two lines of code that will create these attributes from the appropriate passed in parameters.

```
class Address(object):
    def __init__(self, number, streetName):
        # Line 1: Creating a number attribute
        # Line 2: Creating a streetName attribute  
```
* What is the correct expression for # Line 1?

`self.number = number`

* What is the correct expression for # Line 2?

`self.streetName = streetName`