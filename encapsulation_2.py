# Student Grade Management System 

class Student: 

    def __init__(self, name, student_id, marks): 
        self.name = name
        self._student_id = student_id 
        self.__marks = 0
        self.set_marks(marks)

    def set_marks(self, marks): 

        if 0 <= marks <= 100: 
            self.__marks = marks 
            print("Marks updated successfully.")

        else: 
            print("Marks must be between 0 and 100.")

    def get_marks(self): 
        return self.__marks

    def calculate_percentage(self): 
        return self.__marks 

    def get_grade(self): 
        if self.__marks >= 90: 
            return "A*"

        elif self.__marks >= 80: 
            return "A"

        elif self.__marks >= 70:
            return "B"

        elif self.__marks >= 60:
            return "C"

        elif self.__marks >= 50:
            return "D"

        else:
            return "F"

    def display_student(self): 

        print("\nStudent Details: ")
        print("------------------------")
        print("Name: ", self.name)
        print("Student ID:", self._student_id)
        print("Marks: ", self.__marks)
        print("Grade: ", self.get_grade())

std = Student("Alex", "S101", 85)
std.display_student()
std.set_marks(95)
std.display_student()
std.set_marks(150)