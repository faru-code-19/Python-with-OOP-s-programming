class PN:
    def m1(self):
        print("pn1")
        print("pn2")
class SN:
    def m2(self):
        print("sn1")
        print("sn2")
class Main_news:
    def __init__(self):
        self.pn=PN()
        self.sn=SN()

    def info(self):
        self.pn.m1() #
        self.sn.m2()

m=Main_news()
m.info()    