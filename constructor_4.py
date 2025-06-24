class Test:
    def __init__(self):
        print("constructor")
t=Test() #calling constructor implicitly
t.__init__()
t.__init__()
t.__init__() #calling constructor explicitly