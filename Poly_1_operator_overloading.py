class Book:
    def __init__(self,pages):
        self.pages=pages

    def __add__(self,other):
        tot_pages=self.pages+other.pages
        return tot_pages 


b1=Book(100)
b2=Book(200)
b3=Book(400)
print(b1+b2)
print(b2+b3)