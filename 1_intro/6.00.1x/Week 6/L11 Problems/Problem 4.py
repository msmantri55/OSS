# Your task is to define the following two methods for the Coordinate class:

# Add an __eq__ method that returns True if coordinates refer to same point in
# the plane (i.e., have the same x and y coordinate).

# Define __repr__, a special method that returns a string that looks like a
# valid Python expression that could be used to recreate an object with the
# same value. In other words, eval(repr(c)) == c given the definition of __eq__
# from part 1.

class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'

    def __eq__(c1, c2):
        if c1.x == c2.x and c1.y == c2.y:
            return True
        else:
            return False
    
    def __repr__(self):
        return 'Coordinate(%(x1)d, %(y1)d)' % {'x1': self.x, 'y1': self.y}