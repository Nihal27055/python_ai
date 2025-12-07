class rectangle :
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth 
    def print(self):
        area = self.length * self.breadth
        print(f"Area of the Rectangle is {area}")

rect = rectangle(int(input("Enter the Length of the Reactangle : ")),int(input("Enter the Breadth of the Reactangle : ")))
rect.print()