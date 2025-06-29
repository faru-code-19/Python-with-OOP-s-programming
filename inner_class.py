class Outer:
    def __init__(self):
        print("Outer class initialized")

    class Inner:
        def __init__(self):
            print("Inner class initialized:")
        
        def m(self):
            print("Method m of Inner class called")

o= Outer()
i=o.Inner()
i.m()

#o=Outer().Inner()  # This will also work.
#o=Outer().Inner().m()  # This will also work.