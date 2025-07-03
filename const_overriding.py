class P:
    def __init__(self):
        print("fv")

    
class C(P):
    def __init__(self):
        #super().__init__()
        print("vf")

c=C()