class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self._roll_number = roll_number
        self._marks = marks  

    def calculate_percentage(self):
        return self._marks   

    def get_result(self):
        if self.calculate_percentage() >= 50:
            return "Pass"
        else:
            return "Fail"


class ScholarshipStudent(Student):
    def __init__(self, name, roll_number, marks, scholarship_amount):
        super().__init__(name, roll_number, marks)
        self._scholarship_amount = scholarship_amount 

    def check_scholarship(self):
        if self.calculate_percentage() >= 85:
            return "Qualified"
        else:
            return "Not Qualified"

    def display_details(self):
        print("Name:", self.name)
        print("Roll Number:", self._roll_number)
        print("Marks:", self._marks)  
        print("Scholarship Amount:", self._scholarship_amount)
        print("Percentage:", self.calculate_percentage())
        print("Result:", self.get_result())
        print("Scholarship Status:", self.check_scholarship())


student1 = ScholarshipStudent("Aurora", 13, 94, 5000)
student1.display_details()
