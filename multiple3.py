# Job Application Tracker 

class Applicant: 

    def __init__(self, name, qualification): 
        self.name = name 
        self.qualification = qualification 

class Job: 

    def __init__(self, job_title, company, salary): 
        self.job_title = job_title
        self.company = company 
        self.salary = salary 

class Application(Applicant, Job): 

    def __init__(
            self, 
            name,
            qualification,
            job_title,
            company,
            salary
    ): 

        Applicant.__init__(
            self,
            name,
            qualification
        )

        Job.__init__(
            self,
            job_title,
            company,
            salary
        )

    def display_application(self): 

        print("----- JOB APPLICATION -----")
        print("Applicant:", self.name)
        print("Qualification:", self.qualification)
        print("Job:", self.job_title)
        print("Company:", self.company)
        print("Expected Salary: £",self.salary)


application1 = Application(
    "Aarav",
    "B.Tech Computer Science",
    "Python Developer",
    "Tech Solutions",
    60000
)

application1.display_application()