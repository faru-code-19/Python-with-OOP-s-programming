class Num:
    def __init__(self,name,num):
        self.name=name
        self.num=num

    def __ge__(self,other):
        return self.num>=other.num

s1=Num('a',100)
s2=Num('b',20)
print(s1>=s2)    
print(s1<=s2)
