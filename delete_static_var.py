class Test():

    a=10

    @classmethod
    def m(cls):
        del cls.a
       #del Test.a  # deleting static variable using class name

#Test.m()
del Test.a # deleting static variable using class name outside the class
print(Test.__dict__)
