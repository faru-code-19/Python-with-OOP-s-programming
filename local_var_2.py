class Test():

    def m(self): # definition of instance method m
        a=10 #local variable a
        print(a)
    #def n(self): # definition of instance method n
        #print(a) 
t=Test() # create an instance of Test
t.m() # call instance method m
#t.n() # this will raise an error because 'a' is not defined in this method


