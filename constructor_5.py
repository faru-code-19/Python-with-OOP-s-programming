class Test:
    def __init__(self):
        print("0 arguments constructor")
    def __init__(self, n):
        print("1 argument constructor", n)

t1 = Test(10)  # This will call the second __init__ method
#t2 = Test()  # This will raise an error because the first __init__ method is overridden
# Uncommenting the above line will result in a TypeError since Test() expects 1 argument