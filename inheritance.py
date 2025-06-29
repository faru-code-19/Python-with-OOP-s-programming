class P:
    a=10

    def __init__(self):
        print("parent constructor")
        self.b=12

    def m1(self):
        print("parent instance mtd")
    
    @classmethod
    def m2(cls):
        print("parent class mtd")

    @staticmethod
    def m3():
        print("parent static mtd")

class C(P):
    pass

c=C()
print(c.a)
print(c.b)
c.m1()
c.m2()
c.m3()