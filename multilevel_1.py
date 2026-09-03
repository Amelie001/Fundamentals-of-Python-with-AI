# College Management System 

class Person: 

    def __init__(self, name, age): 
        self.name = name 
        self.age = age

    def show_details(self): 
        print("Name:", self.name)
        print("Age:", self.age)

class Student(Person): 

    def __init__(self, name, age, studentID, course): 
        super().__init__(name, age)
        self.studentID = studentID 
        self.course = course 

    def show_student_details(self): 
        print("Student ID:", self.studentID)
        print("Course:", self.course)

class CollegeStudent(Student): 

    def __init__(self, name, age, studentID, course, branch, semester): 
        super().__init__(name, age, studentID, course)
        self.branch = branch
        self.semester = semester 

    def show_college_details(self): 
        print("Branch:", self.branch)
        print("Semester:", self.semester)


student = CollegeStudent(
    "Alex", 
    18, 
    "CS101", 
    "B.Tech", 
    "Computer Science",
    2
    )

print("------ COLLEGE STUDENT ------")

student.show_details()
student.show_student_details()
student.show_college_details()