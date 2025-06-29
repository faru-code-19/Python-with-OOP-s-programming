class Test:
    def __init__(self):
        print("Constructor called")
    
    def __del__(self):
        print("Destructor called")
    
l=[Test(), Test(), Test()]
#del l  # Delete the list to trigger the destructor calls
# The destructors will be called for each object in the list
print("end")