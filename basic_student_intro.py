class student :
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade 

name = student("nihal",7)

print(f"Hi I am {name.name} studying in {name.grade} ")