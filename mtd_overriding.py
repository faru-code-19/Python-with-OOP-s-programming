class P:
    def m1(self):
        print("fv")

    
class C(P):
    def m1(self):
        #super().m1()
        print("vf")

c=C()
c.m1()