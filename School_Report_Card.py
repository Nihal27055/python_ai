class Student :
    def __init__(self,Name,Number,Class,English,Maths,Science,Malayalam,History,Total_Marks):
        self.Name = Name 
        self.Number = Number
        self.Class = Class
        self.English = English
        self.Maths = Maths
        self.Science = Science
        self.Malayalam = Malayalam
        self.History = History
        self.Total_Marks = Total_Marks
    def subject(self,average):
        English = self.English
        Maths = self.Maths
        Science = self.Science
        Malayalam = self.Malayalam
        average = self.English + self.Maths + self.Science + self.Malayalam / 5
        return average()
average = 0
Nihal = Student("Nihal",12,7,56,68,68,75,65,average)    

Nihal.subject(0)
