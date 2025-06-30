class P1:
    def m1(self):
        print("p1 class")

class P2:
    def m1(self):
        print("p2 class")

class c(P2,P1):
    def m3(self):
        print("clas c")

o=c()
o.m1()
o.m3()
