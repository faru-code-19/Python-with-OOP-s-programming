'''class Birds:
    wings=2

    @classmethod
    def fly(cls,name):
        print(f"{name} can fly with{cls.wings} wings")

Birds.fly("sparrow")'''  # Calling the class method directly using the class name

class Test:

    count=0

    def __init__(self):
        Test.count= Test.count+1
    @classmethod
    def getCount(cls):
        print(cls.count)

Test.getCount()  # Calling the class method to get the count
t1= Test()  # Creating an instance of Test
t2= Test()  # Creating another instance of Test
t3=Test()  # Creating yet another instance of Test
Test.getCount()  # Calling the class method again to get the updated count
    