class Student:
    def __init__(self, Name, Roll_Num, Class):
        self.Name = Name
        self.Roll_Num = Roll_Num
        self.Class = Class
        self.subject = {}     
        self.Mark = None       

    def Report_Card(self):
        print(" Report Card ")
        print(f"Name        : {self.Name}")
        print(f"Roll Number : {self.Roll_Num}")
        print(f"Class       : {self.Class}")
        print(f"Marks       : {self.subject}")
        print(f"Grade       : {self.Mark}")


def average(English, Science, Malayalam, History):
    return (English + Science + Malayalam + History) / 4


def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "D"


def add_marks(student):
    try :
        student.subject["English"] = int(input("English : "))
        student.subject["Science"] = int(input("Science : "))
        student.subject["Malayalam"] = int(input("Malayalam : "))
        student.subject["History"] = int(input("History : "))
    except ValueError  :
        print("Type Only Numbers.")    

    avg = average(
        student.subject["English"],
        student.subject["Science"],
        student.subject["Malayalam"],
        student.subject["History"]
    )
    student.Mark = calculate_grade(avg)

class School:
    def __init__(self):
        self.students = []

    def add_student(self,student):
        self.students.append(student)

    def find_student(self, roll):
        for i in self.students:
            if i.Roll_Num == roll:
                return i

    def view_all_students(self):
        for i in self.students:
            i.Report_Card()

school = School()
teacher_pass = 4321
while True:
    print(""" -------WARNING YOUR MISTAKE WILL BE REST ALL REPORT_CARDS , BE CAREFULL-------- """)
    print("1. Add New Student")
    print("2. Add Marks to Student")
    print("3. View Student Report Card")
    print("4. View All Students")
    print("5. Exit")
    try :
        choice = int(input("Enter choice: "))
    except ValueError  :
        print("Choose Only Numbers.")
        break
    if choice == 1:
        try :
            teacher  = int(input("Enter teacher password : "))
        except ValueError  :
            print("Choose Numbers")
            break
        if teacher == teacher_pass :
            print("Your password is correct ")
            name = str(input("Student Name: "))
            try:    
                roll = int(input("Roll Number: "))
                cls = int(input("Class: "))
                student = Student(name, roll, cls)
                school.add_student(student)
            except ValueError  :
                print("Choose numbers only.")  
                break  
            print("Student added.")
        else : 
            print("Invalid Password Try again")    

    elif choice == 2:
        try :
            teacher  = int(input("Enter teacher password : "))
        except ValueError  :
                print("Choose numbers only.") 
                break       
        if teacher == teacher_pass :
            print("Your password is correct")
            try:
                roll = int(input("Enter Roll Number: "))
            except ValueError  :
                print("Choose numbers only.")      
                break  
            student = school.find_student(roll)
            if student:
                add_marks(student)
                print("Marks Added to the Student.")
            else:
                print("Student not found.")

    elif choice == 3:
        try :
            roll = int(input("Enter Roll Number: "))
        except ValueError  :
                print("Choose numbers only.")     
                break   
        student = school.find_student(roll)
        if student:
            student.Report_Card()
        else:
            print("Student not found.")

    elif choice == 4:
        school.view_all_students()

    elif choice == 5:
        print("Exiting program.")
        break

    else:
        print("The Number You Called is Currently Not Awailable .")
