# University Student Management System 

class Student:

    def __init__(self, student_id, name, age): 
        self.student_id = student_id 
        self.name = name 
        self.age = age

    def show_basic_details(self): 
        print("\n----- STUDENT DETAILS -----")
        print("Student ID:", self.student_id)
        print("Name:", self.name)
        print("Age:", self.age)

    def calculate_percentage(self, marks):
        total = sum(marks)
        percentage = total / len(marks)
        return percentage 

    def get_grade(self, percentage): 
        if percentage >= 90: 
            return "A+"
        elif percentage >= 80: 
            return "A"
        elif percentage >= 70: 
            return "B"
        elif percentage >= 60: 
            return "C"
        elif percentage >= 50: 
            return "D"
        else: 
            return "F"

class EngineeringStudent(Student): 

    def calculate_result(self): 
        print("\n----- ENGINEERING RESULT -----")

        python = float(input("Enter Python marks: "))
        maths = float(input("Enter Maths marks: "))
        electronics = float(input("Enter Electronics marks: "))
        physics = float(input("Enter Physics marks: "))
        dataStructures = float(input("Enter Data Structures marks: "))

        marks = [
            python,
            maths,
            electronics,
            physics,
            dataStructures
        ]

        percentage = self.calculate_percentage(marks)
        grade = self.get_grade(percentage)

        print("Percentage:", percentage, "%")
        print("Grade:", grade)

    def show_specialization(self): 
        print("Department: Computer Engineering")

class MedicalStudent(Student): 

    def calculate_result(self): 
        print("\n----- MEDICAL RESULT -----")

        anatomy = float(input("Enter Anatomy marks: "))
        physiology = float(input("Enter Physiology marks: "))
        biology = float(input("Enter Biology marks: "))
        chemistry = float(input("Enter Chemistry marks: "))
        pathology = float(input("Enter Pathology marks: "))

        marks = [
            anatomy, 
            physiology,
            biology,
            chemistry,
            pathology
        ]

        percentage = self.calculate_percentage(marks)
        grade = self.get_grade(percentage)
        
        print("Percentage:", percentage, "%")
        print("Grade:", grade)

    def show_specialization(self): 
        print("Department: Medicine")

class ManagementStudent(Student): 

    def calculate_result(self): 
        print("\n----- MANAGEMENT RESULT -----")

        marketing = float(input("Enter Marketing marks: "))
        finance = float(input("Enter Finance marks: "))
        economics = float(input("Enter Economics marks: "))
        management = float(input("Enter Management marks: "))
        business = float(input("Enter Business marks: "))

        marks = [
            marketing, 
            finance,
            economics,
            management,
            business
        ]

        percentage = self.calculate_percentage(marks)
        grade = self.get_grade(percentage)
        
        print("Percentage:", percentage, "%")
        print("Grade:", grade)

    def show_specialization(self): 
        print("Department: Business Management")

print("===== UNIVERSITY STUDENT MANAGEMENT =====")

student_id = input("Enter Student ID: ")
name = input("Enter name: ")
age = input("Enter age: ")

print("\n1. Engineering")
print("2. Medical")
print("3. Management")

choice = int(input("Select course: "))

if choice == 1: 
    student = EngineeringStudent(student_id, name, age)

elif choice == 2: 
    student = MedicalStudent(student_id, name, age)

elif choice == 3: 
    student = ManagementStudent(student_id, name, age)

else: 
    print("Invalid choice.")
    exit()

student.show_basic_details()
student.show_specialization()
student.calculate_result()