class Test:
    sch_name="KV" #static variable

    def __init__(self,name,age):
        self.name=name  #instance variable
        self.age=age    #instance variable

    def info(self):
        x=10 #local variable
        for i in range(x):
            print(i)  # i is a local variable within this method