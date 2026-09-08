# Student Result Manager

class Student: 

    def __init__(self, name, roll_number): 
        self.name = name 
        self.roll_number = roll_number

class Marks: 

    def __init__(self, python, java, maths): 
        self.python = python 
        self.java = java 
        self.maths = maths 

class Result(Student, Marks): 

    def __init__(self, name, roll_number, python, java, maths): 
        Student.__init__(self, name, roll_number)
        Marks.__init__(self, python, java, maths)

    def calculate_result(self): 
        total = self.python + self.java + self.maths
        percentage = total / 3 

        print("----- STUDENT RESULT SHEET -----")
        print("Name:", self.name)
        print("Roll Number:", self.roll_number)
        print("Python Marks:", self.python)
        print("Java Marks:", self.java)
        print("Maths Marks:", self.maths)
        print("Total Marks:", total)
        print("Percentage:", percentage)

        if percentage >= 40: 
            print("Result: PASS")
        else: 
            print("Result: FAIL")

student1 = Result(
    "Jude",
    17,
    94,
    89,
    98
)

student1.calculate_result()