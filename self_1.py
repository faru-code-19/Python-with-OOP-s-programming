class Test:
    'this is a test class'

    def __init__(self):
        print("address of self is:",id(self))

t=Test()
print("adress of t is:",id(t))

#self and t both refer to the same object
