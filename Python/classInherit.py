class topper(): # Superclass of middle class
    print("I\'m the topper class")
class middle(topper): # Superclass of lower class and subclass of topper class
    print("I\'m the middle class")
class lower(middle): # Subclass of middle class
    print("I\'m the lower class")

# Top row of classes seem to immediately print their message

class topper2(): # Superclass of middle2 class
    def __init__(self):
        print("I\'m the topper2 class")
class middle2(topper2): # Superclass of lower class and subclass of topper2 class
    def __init__(self):
        print("I\'m the middle2 class")
class lower2(middle2): # Subclass of middle2 class
    def __init__(self):
        print("I\'m the lower2 class")

test0 = lower() # This seems to not do anything
test1 = lower2() # This seems to only run lower2's __init__ constructor
test2 = lower() # Proof of test0
