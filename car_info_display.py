class student :
    def __init__(self,name,age,grade,gender,birth,):
        self.name = name
        self.age = age
        self.grade = grade
        self.gender = gender
        self.birth = birth
    
    def detail(self):
        print(f"name = {self.name}")
        print(f"age = {self.age}")
        print(f"grade = {self.grade}")
        print(f"gender = {self.gender}")
        print(f"birth = {self.birth}")

std_name = student(str(input("Enter Student Name : ")),int(input("Enter Student age : ")),int(input("Enter Student grade : ")),str(input("Enter Student gender : ")),(input("Enter Student birth : ")).capitalize)
std_name.detail()

