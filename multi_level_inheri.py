class P:
    def m1(self):
        print("parent class")

class C(P):
    def m2(self):
        print("chile class")

class CC(C):
    def m3(self):
        print("cc class")

c=CC()
c.m1()
c.m2()
c.m3()