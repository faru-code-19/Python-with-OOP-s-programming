class P:
    def m1(self):
        print("parent mtd")

class C(P):
    def m1(self):
        super().m1()
       #self.m1()
        print("child mtd")

c=C()
c.m1()