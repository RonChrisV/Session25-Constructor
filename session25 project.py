class Student:
    #creating constructor
    def __init__(self):
        self.student_name = input("\n Enter the students name: ")
        self.student_age = input("\n Enter the students age: ")
        self.student_gender = input("\n Enter the students gender: ")

    def display(self):
        print("Enter the student name: ",self.student_name)
        print("Enter the student age: ",self.student_age)
        print("Enter the student gender: ",self.student_gender)


class Marks:
    def __init__(self):
        self.grade = input("Enter the grade of the student: ")
        print("----- Evaluate Marks per Subject -----")
        self.english = float(input("Mark in Eglish subject: "))
        self.maths  =float(input("Mark in Maths subject: "))
        self.physics = float(input("Mark in Physics subject: "))
        self.chemistry = float(input("Mark in Chemistry subject: "))
        self.computer = float(input("Mark in Computer subject: "))

    def display(self):
        self.total = self.english + self.maths + self.physics + self.chemistry + self.computer
        print("Total Evaluated Marks: ",self.total)

class Data(Student,Marks):
    def __init__(self):
        Student.__init__(self)
        Marks.__init__(self)

    def result(self):
        Marks.display(self)


S1 = Data()
S1.result()
S2 = Data()
S2.result()

print("You can create more objects to add more student data")
