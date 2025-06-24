# Movie System using OOP in Python
# This code defines a class for movies and allows users to create movie objects with title, year, and hero attributes.
# It collects multiple movie entries and displays their information.




class Movies:
    "this is a class for movies"

    def __init__(self,title,year,hero):
        self.title=title
        self.year=year
        self.hero=hero

    def info(self):
        print(f"Title:{self.title}")
        print(f"Year:{self.year}")
        print(f'Hero:{self.hero}')

movie_list=[]

while True:
    title=input("enter the title:")
    year=int(input("enter the year:"))
    hero=input("enter the hero:")
    m=Movies(title,year,hero) #movies object creation
    movie_list.append(m)
    ch=input("want to add more movies? [yes/no]:")
    if ch.lower()=='no':
        break

print("Movies are:")
for movie in movie_list:
    movie.info() #info method calling