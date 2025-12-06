class triangle :
    def __init__(self,base ,height,):
        self.base = base
        self.height = height
    def equition (self):
        a = self.base*self.height/2
        print(a)
class square :
    def __init__(self,side):
        self.side = side
    def equition (self):
        a = self.side * self.side    
        print(a)
class rectangle :
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def equition (self):
        a = self.length * self .breadth
        print(a)        


user = str(input("Which shape area you want : ").lower())  
def shape (user):
    if user == "triangle":
        tri = triangle(base = int(input("Enter triangle base : ")),height = int(input("Enter triangle height : ")))
        tri.equition()
    elif user == "square" :
        sq = square(side =  int(input("Enter square side : ")))
        sq.equition()
    elif user == "rectangle" :
        rect = rectangle(length = int(input("Enter rectangle length : ")),breadth = int(input("Enter rectangle breadth : ")))
        rect.equition()
    else :
        print("only type triangle or square or rectangle")

a = shape(user)