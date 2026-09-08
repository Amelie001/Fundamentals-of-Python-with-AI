# Hospital Management System 

class Person: 

    def __init__(self, name, age): 
        self.name = name
        self.age = age 

class MedicalStaff(Person): 

    def __init__(self, name, age, employee_id, department, salary): 
        super().__init__(name, age)
        self.employee_id = employee_id 
        self.department = department 
        self.salary = salary 

class Doctor(MedicalStaff): 

    def __init__(
            self, 
            name, 
            age, 
            employee_id, 
            department, 
            salary, 
            specialization, 
            consultation_fee, 
            number_of_patients
            ): 
        super().__init__(name, age, employee_id, department, salary)
        self.specialization = specialization 
        self.consultation_fee = consultation_fee 
        self.number_of_patients = number_of_patients 

    def display_profile(self): 
        print("----- DOCTOR'S PROFILE -----")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.employee_id)
        print("Department:", self.department)
        print("Salary: £", self.salary)
        print("Specialization:", self.specialization)
        print("Consultation fee: £", self.consultation_fee) 
        print("Number of patients:", self.number_of_patients)

    def daily_consultation_earnings(self): 
        daily_earnings = self.consultation_fee * self.number_of_patients 
        print("Daily consultation earnings: £", daily_earnings)

doctor1 = Doctor(
    "Dr Jane",
    32,
    "D101",
    "Cardiology",
    65000,
    "Heart Specialist",
    120,
    8
)

doctor1.display_profile()
doctor1.daily_consultation_earnings()