class Person:
    def __init__(self):
        print("Person obj created")
        self.dob=self.DOB() 

    class DOB:
        def __init__(self):
            print("DOB obj created")


p= Person()