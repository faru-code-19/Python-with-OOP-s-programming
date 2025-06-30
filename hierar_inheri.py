class P:
    def m1(self):
        print("p class")

class c1(P):
    def child(self):
        print('ff')

class c2(P):
    def child2(self):
        print("fff")
    
c=c1()
d=c2()
c.m1()
c.child()
print()
d.child2()
d.m1()
