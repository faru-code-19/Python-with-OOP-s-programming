import sys
class Test:
    pass

t1=Test()
print("t1:", sys.getrefcount(t1))  # Reference count for t1

