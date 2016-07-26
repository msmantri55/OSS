# Consider the following code:

```
class Clock(object):
    def __init__(self, time):
	self.time = time
    def print_time(self):
	time = '6:30'
	print self.time

clock = Clock('5:30')
clock.print_time()
```

What does the code print out? If you aren't sure, create a Python file and run it.

5:30

# Consider the following code:

```
class Clock(object):
    def __init__(self, time):
	self.time = time
    def print_time(self, time):
	print time

clock = Clock('5:30')
clock.print_time('10:30')
```

What does the code print out? If you aren't sure, create a Python file and run it.

10:30

# Consider the following code:

```
class Clock(object):
    def __init__(self, time):
	self.time = time
    def print_time(self):
	print self.time

boston_clock = Clock('5:30')
paris_clock = boston_clock
paris_clock.time = '10:30'
boston_clock.print_time()
```

What does the code print out? If you aren't sure, create a Python file and run it.

10:30

# Are `boston_clock` and `paris_clock` different objects?

No