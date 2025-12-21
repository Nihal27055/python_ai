class Student :
    def __init__(self,Name,Roll_Num,Class,Mark):
        self.Name = Name 
        self.Roll_Num = Roll_Num
        self.Class = Class
        self.Mark = Mark
    def Report_Card(self):
        print(f"Name Of the Student : {self.Name}")    
        print(f"Roll_Number         : {self.Roll_Num}")   
        print(f"Class               : {self.Class}")   
        print(f"Grade               : {self.Mark}")   

def average(English,Science,Malayalam,History):
    average = (English + Science + Malayalam + History )/ 4 
    return average

def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "D"

nihal = Student("NIHAL",12,7,84)
user_roll = int(input("Enter Student Roll Number : "))
if user_roll == nihal.Roll_Num :
    nihal_Eng = int(input(f"Enter {nihal.Name} Mark In English Subject : "))
    nihal_Sci = int(input(f"Enter {nihal.Name} Mark In Science Subject : "))
    nihal_Mala = int(input(f"Enter {nihal.Name} Mark In Malayalayam Subject : "))
    nihal_Hist = int(input(f"Enter {nihal.Name} Mark In History Subject : "))
else : 
    print("Roll number not exisist in the records ")
English = nihal_Eng
Science = nihal_Sci
Malayalam = nihal_Mala
History = nihal_Hist

avg = average(English, Science, Malayalam, History)
nihal.Mark = calculate_grade(avg)


nihal.Report_Card()
