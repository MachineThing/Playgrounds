"""
First, this program creates an iterator called "bitCount"
Then the code inside bitCount is a simple iterator (like the range function)
The __iter__() constructor returns the object itself (the class),
And the __next__() constructor returns the next value

The value is always 2 ** iteratorNumber
"""

class bitCount:
    def __init__(self, ln):
        self.__ln = ln  # Set self.__ln to "Loop Number"
        self.__it = 0   # Set iteratorNumber to 0

    def __iter__(self): # This constructor returns the object itself.
        return self

    def __next__(self):
        self.__it += 1
        if self.__it > self.__ln: # If the iteratorNumber is greater than the loop number...
            raise StopIteration # Stop iteration
        return 2 ** self.__it # Return 2 ** iterator Number

for i in bitCount(10): # Some testing code...
    print(i)
