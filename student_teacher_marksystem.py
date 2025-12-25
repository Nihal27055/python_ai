class Student:
    def __init__(self, name, age, maths, science, english):
        self.name = name
        self.age=   age
        self. maths=  maths
        self. science=  science
        self. english=  english
    def markSum(self):
        sum= self.maths + self.science + self.english 
        print(sum)
class Teacher:
    def __init__(self,name , age ,Experience):
        self.name = name
        self.age =age
        self.Experience =Experience
    def TeacherDetails(self):
        print(f"Name: {self.name}, Age: {self.age}, Experience: {self.Experience}")



Max = Student("Max",21,100,50,45)
Max.markSum()
Rahul = Student("Rahul",21,30,40,50)
Rahul.markSum()
Diya = Teacher("Diya",26,4)
Diya.TeacherDetails()