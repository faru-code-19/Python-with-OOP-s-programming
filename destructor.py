import time

class Test:
    def __init__(self):
        print("Constructor called")
    
    def __del__(self):
        print("Destructor called")
        
t=Test()
#t=None
time.sleep(5)  # Wait for a while to see the destructor message
#print("End of program")